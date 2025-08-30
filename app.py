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
    
    aprendizes_cadastrados = carregar_dados()
    lista_nomes = ["-- Novo Cadastro --"] + list(aprendizes_cadastrados.keys())
    
    index = 0
    if st.session_state.get("nome_aprendiz_ativo") in lista_nomes:
        index = lista_nomes.index(st.session_state.nome_aprendiz_ativo)

    aprendiz_selecionado = st.selectbox(
        "Selecione o Aprendiz:",
        options=lista_nomes,
        index=index,
        key="seletor_principal"
    )

    if aprendiz_selecionado != "-- Novo Cadastro --":
        if st.session_state.get("nome_aprendiz_ativo") != aprendiz_selecionado:
            st.session_state.aprendiz_ativo = aprendizes_cadastrados[aprendiz_selecionado]
            st.session_state.nome_aprendiz_ativo = aprendiz_selecionado
            st.rerun()
    else:
        st.session_state.aprendiz_ativo = None
        st.session_state.nome_aprendiz_ativo = None
        
    st.sidebar.markdown("---")
    st.info("Navegue pelas páginas ao lado para gerenciar o aprendiz selecionado.")

# --- CONTEÚDO DA PÁGINA INICIAL ---
st.title("Bem-vindo(a) à Plataforma INTERVENÇÃO IA!")
st.subheader("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")
st.markdown("---")

if st.session_state.get("nome_aprendiz_ativo"):
    st.success(f"**Aprendiz selecionado:** {st.session_state.nome_aprendiz_ativo}")
else:
    st.warning("Nenhum aprendiz selecionado. Selecione um na barra lateral ou cadastre um novo na página 'Cadastro de Aprendiz'.")

st.markdown("""
### Como usar:
1.  **Selecione um Aprendiz** na caixa de seleção na barra lateral. Para criar um novo, deixe a opção `-- Novo Cadastro --`.
2.  Navegue para a página **Cadastro de Aprendiz** para inserir ou editar as informações cadastrais.
3.  Vá para **Avaliação de Habilidades** para preencher o formulário de avaliação detalhado.
4.  Use o **Plano de Ensino Individualizado (PEI)** para definir metas e estratégias baseadas na BNCC.
""")
