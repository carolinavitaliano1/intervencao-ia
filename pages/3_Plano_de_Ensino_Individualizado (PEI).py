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
    # (Função da IA como definida anteriormente)
    dados_cadastro = dados_aprendiz.get("cadastro", {})
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    if not avaliacoes:
        return None, "Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro."
    # ... (restante da lógica da função)
    return "Prompt de exemplo", None # Mantendo a lógica anterior

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
            st.session_state.adapt_sala_gerados = "1. Utilizar material dourado e ábaco nas aulas de matemática.\n2. Apresentar instruções em etapas (uma de cada vez)."
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
        
        etapa_ensino = st.selectbox("1. Selecione a Etapa de Ensino:", list(BNCC_DATABASE.keys()), key="etapa_ensino")
        
        lista_de_habilidades = []
        label_multiselect = "Marque as Habilidades que deseja trabalhar:"
        
        if etapa_ensino == "Educação Infantil":
            grupos_etarios = list(BNCC_DATABASE[etapa_ensino].keys())
            grupo_selecionado = st.selectbox("2. Selecione o Grupo Etário (Faixa Etária):", grupos_etarios, key="infantil_grupo")
            campos_exp = list(BNCC_DATABASE[etapa_ensino][grupo_selecionado].keys())
            campo_selecionado = st.selectbox("3. Selecione o Campo de Experiência:", campos_exp, key="infantil_campo")
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][grupo_selecionado][campo_selecionado]
            label_multiselect = "4. Marque os Objetivos de Aprendizagem que deseja trabalhar:"

        elif etapa_ensino == "Ensino Fundamental":
            anos_disponiveis = list(BNCC_DATABASE[etapa_ensino].keys())
            ano_selecionado = st.selectbox("2. Selecione o Ano Escolar:", anos_disponiveis, key="fundamental_ano")
            componentes_disponiveis = list(BNCC_DATABASE[etapa_ensino][ano_selecionado].keys())
            componente_selecionado = st.selectbox("3. Selecione o Componente Curricular (Matéria):", componentes_disponiveis, key="fundamental_componente")
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][ano_selecionado][componente_selecionado]
            label_multiselect = "4. Marque as Habilidades que deseja trabalhar:"

        elif etapa_ensino == "Ensino Médio":
            areas_conhecimento = list(BNCC_DATABASE[etapa_ensino].keys())
            area_selecionada = st.selectbox("2. Selecione a Área de Conhecimento:", areas_conhecimento, key="medio_area")
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][area_selecionada].get("Habilidades", [])
            label_multiselect = "3. Marque as Habilidades que deseja trabalhar:"

        opcoes_formatadas = [f"({h['codigo']}) {h['descricao']}" for h in lista_de_habilidades]
        habilidades_lookup = {f"({h['codigo']}) {h['descricao']}": h for h in lista_de_habilidades}
        habilidades_marcadas_formatadas = st.multiselect(label_multiselect, options=opcoes_formatadas, key="selecao_habilidades")
        
        st.markdown("---")
        # (Restante da Etapa 2 para detalhar as habilidades)
        
    # (Etapa 3 e botão Salvar)
    submitted = st.form_submit_button("Salvar PEI Completo")
    if submitted:
        # Lógica de salvamento...
        st.success("PEI Salvo com sucesso!")
