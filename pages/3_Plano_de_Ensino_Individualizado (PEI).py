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
            # Simulação da resposta da IA
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
        etapa_ensino = st.selectbox("1. Selecione a Etapa de Ensino:", list(BNCC_DATABASE.keys()))
        
        lista_de_habilidades = []
        if etapa_ensino == "Educação Infantil":
            # Lógica para Ed. Infantil
            pass
        elif etapa_ensino == "Ensino Fundamental":
            anos_disponiveis = list(BNCC_DATABASE[etapa_ensino].keys())
            ano_selecionado = st.selectbox("2. Selecione o Ano Escolar:", anos_disponiveis)
            componentes_disponiveis = list(BNCC_DATABASE[etapa_ensino][ano_selecionado].keys())
            componente_selecionado = st.selectbox("3. Selecione o Componente Curricular (Matéria):", componentes_disponiveis)
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][ano_selecionado][componente_selecionado]
        elif etapa_ensino == "Ensino Médio":
            # Lógica para Ensino Médio
            pass

        opcoes_formatadas = [f"({h['codigo']}) {h['descricao']}" for h in lista_de_habilidades]
        habilidades_lookup = {f"({h['codigo']}) {h['descricao']}": h for h in lista_de_habilidades}
        habilidades_marcadas_formatadas = st.multiselect("4. Marque as habilidades que deseja trabalhar:", options=opcoes_formatadas)
        
        habilidades_detalhadas = []
        if habilidades_marcadas_formatadas:
            # ... (lógica para detalhar habilidades)
            pass

    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        observacoes = st.text_area("Observações Gerais", height=200)
        ajustes_proximo_pei = st.text_area("Ajustes para o Próximo PEI", height=200)

    submitted = st.form_submit_button("Salvar PEI Completo")
    if submitted:
        # ... (lógica de salvamento)
        st.success("PEI salvo com sucesso!")
