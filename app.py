import streamlit as st
from database_utils import carregar_dados
from auth import enforce_login

st.set_page_config(
    layout="wide",
    page_title="INTERVENÇÃO IA",
    page_icon="🧠"
)

# Proteção por login
enforce_login()

if 'aprendiz_ativo' not in st.session_state:
    st.session_state.aprendiz_ativo = None
    st.session_state.nome_aprendiz_ativo = None

with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA")
    
    if st.button("➕ Cadastrar Novo Aprendiz"):
        st.session_state.aprendiz_ativo = None
        st.session_state.nome_aprendiz_ativo = None
        st.switch_page("pages/1_Cadastro_de_Aprendiz.py")

    st.markdown("---")
    
    aprendizes_cadastrados = carregar_dados()
    lista_nomes = [""] + list(aprendizes_cadastrados.keys())
    
    index = 0
    if st.session_state.get("nome_aprendiz_ativo") in lista_nomes:
        index = lista_nomes.index(st.session_state.nome_aprendiz_ativo)

    aprendiz_selecionado = st.selectbox(
        "Selecione um Aprendiz:",
        options=lista_nomes,
        index=index,
        key="seletor_principal",
        label_visibility="collapsed",
        placeholder="Selecione um Aprendiz"
    )

    if aprendiz_selecionado and st.session_state.get("nome_aprendiz_ativo") != aprendiz_selecionado:
        st.session_state.aprendiz_ativo = aprendizes_cadastrados[aprendiz_selecionado]
        st.session_state.nome_aprendiz_ativo = aprendiz_selecionado
        st.rerun()
        
    st.sidebar.markdown("---")
    st.info("Navegue pelas páginas ao lado para gerenciar o aprendiz selecionado.")

st.title("Bem-vindo(a) à Plataforma INTERVENÇÃO IA!")
st.subheader("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")
st.markdown("---")

if st.session_state.get("nome_aprendiz_ativo"):
    st.success(f"**Aprendiz selecionado:** {st.session_state.nome_aprendiz_ativo}")
else:
    st.warning("Nenhum aprendiz selecionado. Clique em 'Cadastrar Novo Aprendiz' ou selecione um na lista.")
