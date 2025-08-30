import streamlit as st
from database_utils import carregar_dados

st.set_page_config(
    layout="wide",
    page_title="INTERVENÇÃO IA",
    page_icon="🧠"
)

# --- INICIALIZAÇÃO DO ESTADO DA SESSÃO ---
if 'aprendiz_ativo' not in st.session_state:
    st.session_state.aprendiz_ativo = None
    st.session_state.nome_aprendiz_ativo = None

# --- MENU LATERAL DE NAVEGAÇÃO ---
with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA")
    
    # Botão para iniciar um novo cadastro
    if st.button("➕ Cadastrar Novo Aprendiz"):
        st.session_state.aprendiz_ativo = None
        st.session_state.nome_aprendiz_ativo = None
        # Correção: Usa a função nativa st.switch_page
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

# --- CONTEÚDO DA PÁGINA INICIAL ---
st.title("Bem-vindo(a) à Plataforma INTERVENÇÃO IA!")
st.subheader("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")
st.markdown("---")

if st.session_state.get("nome_aprendiz_ativo"):
    st.success(f"**Aprendiz selecionado:** {st.session_state.nome_aprendiz_ativo}")
else:
    st.warning("Nenhum aprendiz selecionado. Clique em 'Cadastrar Novo Aprendiz' ou selecione um na lista.")

st.markdown("""
### Como usar:
1.  **Cadastre um Novo Aprendiz** ou **Selecione um existente** na barra lateral.
2.  Navegue para a página **Cadastro de Aprendiz** para ver o prontuário.
3.  Vá para **Avaliação de Habilidades** para registrar uma nova avaliação detalhada.
4.  Use o **Plano de Ensino Individualizado (PEI)** para definir metas e estratégias.
""")
