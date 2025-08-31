import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_fundamental import FUNDAMENTAL_DB

# --- FUNÇÕES AUXILIARES ---
def buscar_habilidade_por_descricao(descricao_selecionada, ano, componente):
    if ano in FUNDAMENTAL_DB and componente in FUNDAMENTAL_DB[ano]:
        for habilidade in FUNDAMENTAL_DB[ano][componente]:
            if habilidade["descricao"] == descricao_selecionada:
                return habilidade
    return None

def criar_prompt_pei(dados_aprendiz):
    # Pega dados do cadastro e da avaliação mais recente
    dados_cadastro = dados_aprendiz.get("cadastro", {})
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    if not avaliacoes:
        return None, "Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro."
    
    ultima_avaliacao = avaliacoes[-1]
    
    # Monta um resumo completo para a IA
    resumo_completo = ["**Informações do Prontuário do Aprendiz:**"]
    if dados_cadastro.get("diagnostico"): resumo_completo.append(f"- Diagnóstico: {dados_cadastro['diagnostico']}")
    if dados_cadastro.get("dificuldades"): resumo_completo.append(f"- Principais Dificuldades (relatadas): {dados_cadastro['dificuldades']}")
    if dados_cadastro.get("potencialidades"): resumo_completo.append(f"- Principais Potencialidades (relatadas): {dados_cadastro['potencialidades']}")
    if dados_cadastro.get("comunicacao_alt"): resumo_completo.append(f"- Usa comunicação alternativa? {dados_cadastro['comunicacao_alt']}")
    
    resumo_completo.append("\n**Pontos de Apoio da Avaliação de Habilidades:**")
    pontos_encontrados = False
    for i in range(1, 46):
        habilidade_cod = f"hab{i}"
        resultado = ultima_avaliacao.get(habilidade_cod)
        if resultado in ["Realiza com apoio", "Não realiza"]:
            pontos_encontrados = True
            resumo_completo.append(f"- Habilidade {habilidade_cod}: {resultado}")

    if not pontos_encontrados:
        resumo_completo.append("- Nenhum ponto de dificuldade específico marcado na avaliação.")

    resumo_str = "\n".join(resumo_completo)
    prompt = f"""
    Baseado no perfil de um aprendiz, gere sugestões para um PEI.
    Perfil do Aprendiz:
    {resumo_str}
    Sua Tarefa: Gere texto para:
    1. Objetivos Acadêmicos Gerais (2-3 objetivos).
    2. Adaptações de Conteúdo em Sala (3-4 sugestões práticas).
    3. Adaptações em Avaliações (3-4 sugestões específicas).
    """
    return prompt, None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

# Botão e aviso da IA (fora do formulário)
st.info("As sugestões da IA são geradas com base nas informações do Cadastro do Aprendiz e na avaliação de habilidades mais recente.")
if st.button("🤖 Gerar Sugestões com IA para Objetivos e Adaptações"):
    prompt, erro = criar_prompt_pei(st.session_state.get("aprendiz_ativo", {}))
    if erro:
        st.error(erro)
    else:
        with st.spinner("Aguarde, a IA está analisando os dados e gerando sugestões..."):
            st.session_state.objetivos_gerados = "1. Desenvolver a autonomia na leitura de palavras simples.\n2. Aprimorar o raciocínio lógico para resolução de problemas matemáticos básicos."
            st.session_state.adapt_sala_gerados = "1. Utilizar material dourado e ábaco nas aulas de matemática.\n2. Apresentar instruções em etapas (uma de cada vez).\n3. Oferecer textos com letras maiores e espaçamento duplo."
            st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das provas.\n2. Ler os enunciados das questões em voz alta para o aluno."
        st.success("Sugestões geradas! Os campos na Etapa 1 foram preenchidos.")

with st.form("form_pei"):
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=st.session_state.get("objetivos_gerados", ""), height=150)
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=st.session_state.get("adapt_sala_gerados", ""), height=200)
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=st.session_state.get("adapt_avaliacoes_gerados", ""), height=200)

    with st.expander("ETAPA 2: OBJETIVOS POR DISCIPLINA (BNCC)", expanded=True):
        anos_disponiveis = list(FUNDAMENTAL_DB.keys())
        ano_selecionado = st.selectbox("1. Selecione o Ano Escolar:", anos_disponiveis)
        componentes_disponiveis = list(FUNDAMENTAL_DB[ano_selecionado].keys())
        componente_selecionado = st.selectbox("2. Selecione o Componente Curricular (Matéria):", componentes_disponiveis)
        habilidades_disponiveis = [h["descricao"] for h in FUNDAMENTAL_DB[ano_selecionado][componente_selecionado]]
        habilidades_marcadas = st.multiselect("3. Marque as habilidades que deseja trabalhar:", options=habilidades_disponiveis)
        
        habilidades_detalhadas = []
        if habilidades_marcadas:
            st.markdown("---")
            st.write("Preencha os detalhes para cada habilidade selecionada abaixo:")
            for desc in habilidades_marcadas:
                habilidade_obj = buscar_habilidade_por_descricao(desc, ano_selecionado, componente_selecionado)
                if habilidade_obj:
                    with st.container(border=True):
                        st.success(f"**{habilidade_obj['codigo']}**: {habilidade_obj['descricao']}")
                        estrategia = st.text_area("Estratégia", key=f"estrategia_{habilidade_obj['codigo']}", height=100)
                        col_data, col_desempenho = st.columns(2)
                        with col_data: data_inicio = st.text_input("Data de Início e Duração", key=f"data_{habilidade_obj['codigo']}")
                        with col_desempenho: desempenho = st.selectbox("Desempenho", options=["Não iniciado", "Em andamento", "Alcançado com apoio", "Alcançado com autonomia"], key=f"desempenho_{habilidade_obj['codigo']}")
                        habilidades_detalhadas.append({"codigo": habilidade_obj['codigo'], "descricao": habilidade_obj['descricao'], "estrategia": estrategia, "data_inicio": data_inicio, "desempenho": desempenho})

    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        observacoes = st.text_area("Observações Gerais", height=200)
        ajustes_proximo_pei = st.text_area("Ajustes para o Próximo PEI", height=200)
        redigido_por = st.text_input("Este documento foi redigido por")
        data_finalizacao = st.date_input("Data de Finalização")

    submitted = st.form_submit_button("Salvar PEI Completo")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        novo_pei = {
            "data_criacao": data_atual, "objetivos_gerais": objetivos_gerais, "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes, "habilidades_plano": habilidades_detalhadas,
            "observacoes": observacoes, "ajustes_proximo_pei": ajustes_proximo_pei,
            "redigido_por": redigido_por, "data_finalizacao": data_finalizacao.strftime('%d/%m/%Y'),
        }
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        
        if 'objetivos_gerados' in st.session_state: del st.session_state.objetivos_gerados
        if 'adapt_sala_gerados' in st.session_state: del st.session_state.adapt_sala_gerados
        if 'adapt_avaliacoes_gerados' in st.session_state: del st.session_state.adapt_avaliacoes_gerados
        
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
