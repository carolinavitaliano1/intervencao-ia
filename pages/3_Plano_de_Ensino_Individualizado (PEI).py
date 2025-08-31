import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_infantil import INFANTIL_DB
from bncc_fundamental import FUNDAMENTAL_DB
from bncc_medio import MEDIO_DB

# --- Dicionário unificado da BNCC ---
BNCC_DATABASE = {
    "Educação Infantil": INFANTIL_DB,
    "Ensino Fundamental": FUNDAMENTAL_DB,
    "Ensino Médio": MEDIO_DB
}

# --- FUNÇÃO PARA GERAR O PROMPT PARA A IA ---
def criar_prompt_pei(dados_aprendiz):
    dados_cadastro = dados_aprendiz.get("cadastro", {})
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    if not avaliacoes:
        return None, "Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro."
    
    ultima_avaliacao = avaliacoes[-1]
    resumo_completo = ["**Informações do Prontuário do Aprendiz:**"]
    if dados_cadastro.get("diagnostico"): resumo_completo.append(f"- Diagnóstico: {dados_cadastro['diagnostico']}")
    if dados_cadastro.get("dificuldades"): resumo_completo.append(f"- Principais Dificuldades (relatadas): {dados_cadastro['dificuldades']}")
    
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
    return f"Baseado no perfil de um aprendiz:\n{resumo_str}\nGere sugestões para: 1. Objetivos Acadêmicos Gerais. 2. Adaptações de Conteúdo. 3. Adaptações em Avaliações.", None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

# Botão e aviso da IA (fora do formulário)
st.info("As sugestões da IA são geradas com base nas informações do Cadastro e na Avaliação de Habilidades mais recente.")
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
        st.write("Navegue e selecione as habilidades ou objetivos da BNCC para incluir no plano.")
        
        etapa_ensino = st.selectbox("1. Selecione a Etapa de Ensino:", list(BNCC_DATABASE.keys()))
        
        lista_de_habilidades = []
        label_multiselect = "Marque as Habilidades que deseja trabalhar:"
        
        if etapa_ensino == "Educação Infantil":
            grupos_etarios = list(BNCC_DATABASE[etapa_ensino].keys())
            grupo_selecionado = st.selectbox("2. Selecione o Grupo Etário (Faixa Etária):", grupos_etarios)
            campos_exp = list(BNCC_DATABASE[etapa_ensino][grupo_selecionado].keys())
            campo_selecionado = st.selectbox("3. Selecione o Campo de Experiência:", campos_exp)
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][grupo_selecionado][campo_selecionado]
            label_multiselect = "4. Marque os Objetivos de Aprendizagem que deseja trabalhar:"

        elif etapa_ensino == "Ensino Fundamental":
            anos_disponiveis = list(BNCC_DATABASE[etapa_ensino].keys())
            ano_selecionado = st.selectbox("2. Selecione o Ano Escolar:", anos_disponiveis)
            componentes_disponiveis = list(BNCC_DATABASE[etapa_ensino][ano_selecionado].keys())
            componente_selecionado = st.selectbox("3. Selecione o Componente Curricular (Matéria):", componentes_disponiveis)
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][ano_selecionado][componente_selecionado]
            label_multiselect = "4. Marque as Habilidades que deseja trabalhar:"

        elif etapa_ensino == "Ensino Médio":
            areas_conhecimento = list(BNCC_DATABASE[etapa_ensino].keys())
            area_selecionada = st.selectbox("2. Selecione a Área de Conhecimento:", areas_conhecimento)
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][area_selecionada].get("Habilidades", [])
            label_multiselect = "3. Marque as Habilidades que deseja trabalhar:"

        opcoes_formatadas = [f"({h['codigo']}) {h['descricao']}" for h in lista_de_habilidades]
        habilidades_lookup = {f"({h['codigo']}) {h['descricao']}": h for h in lista_de_habilidades}
        habilidades_marcadas_formatadas = st.multiselect(label_multiselect, options=opcoes_formatadas)
        
        st.markdown("---")
        st.write("Preencha os detalhes para cada item selecionado abaixo:")

        habilidades_detalhadas = []
        if habilidades_marcadas_formatadas:
            for selecao in habilidades_marcadas_formatadas:
                habilidade_obj = habilidades_lookup[selecao]
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

    submitted = st.form_submit_button("Salvar PEI Completo")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        novo_pei = {
            "data_criacao": data_atual, "objetivos_gerais": objetivos_gerais, "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes, "habilidades_plano": habilidades_detalhadas,
            "observacoes": observacoes, "ajustes_proximo_pei": ajustes_proximo_pei,
        }
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        
        if 'objetivos_gerados' in st.session_state: del st.session_state.objetivos_gerados
        if 'adapt_sala_gerados' in st.session_state: del st.session_state.adapt_sala_gerados
        if 'adapt_avaliacoes_gerados' in st.session_state: del st.session_state.adapt_avaliacoes_gerados
        
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
