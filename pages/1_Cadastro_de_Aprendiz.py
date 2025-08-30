import streamlit as st
import datetime
from database_utils import salvar_dados_cadastro, excluir_aprendiz
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide", page_title="Prontuário do Aprendiz")

if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

# Se não houver aprendiz ativo e não estivermos em modo de criação, avisa o usuário
if not st.session_state.get("nome_aprendiz_ativo") and not st.session_state.edit_mode:
    st.info("Clique em 'Cadastrar Novo Aprendiz' na barra lateral para começar.")
    st.stop()

# --- MODO DE CRIAÇÃO/EDIÇÃO ---
if st.session_state.edit_mode or not st.session_state.get("nome_aprendiz_ativo"):
    st.header("📝 Dados do Aprendiz")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})
    nome_preenchido = st.session_state.get("nome_aprendiz_ativo", "")

    with st.form("form_cadastro"):
        nome_aluno = st.text_input("Nome Completo do Aluno*", value=nome_preenchido)
        # ... Todos os seus campos de cadastro aqui ...
        data_nasc = st.date_input("Data de Nascimento")
        escola = st.text_input("Escola")
        diagnosticos = st.text_area("Diagnósticos e Observações")
        contato_familia = st.text_area("Contato e Observações da Família")

        submitted = st.form_submit_button("Salvar Prontuário")
        if submitted:
            if not nome_aluno:
                st.error("O nome do aluno é obrigatório!")
            else:
                novos_dados_cadastro = {
                    "data_nascimento": data_nasc.strftime("%d/%m/%Y"),
                    "escola": escola,
                    "diagnosticos": diagnosticos,
                    "contato_familia": contato_familia
                }
                salvar_dados_cadastro(nome_aluno, novos_dados_cadastro)
                st.session_state.nome_aprendiz_ativo = nome_aluno # Atualiza o nome ativo
                st.session_state.edit_mode = False
                st.success(f"Prontuário de '{nome_aluno}' salvo com sucesso!")
                st.rerun()

# --- MODO DE VISUALIZAÇÃO ---
else:
    st.header("Alunos Cadastrados")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})
    
    with st.container(border=True):
        st.subheader(st.session_state.nome_aprendiz_ativo)
        st.write(f"**Data de Nascimento:** {dados_cadastro.get('data_nascimento', 'Não informado')}")
        st.write(f"**Escola:** {dados_cadastro.get('escola', 'Não informado')}")
        st.write("**Diagnósticos e Observações:**")
        st.info(dados_cadastro.get('diagnosticos') or "Nenhuma observação.")
        st.write("**Contato e Observações da Família:**")
        st.info(dados_cadastro.get('contato_familia') or "Nenhum contato.")
    
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📝 Editar Prontuário"):
            st.session_state.edit_mode = True
            st.rerun()
    with col2:
        if st.button("➕ Novo Plano (PEI)"):
            switch_page("Plano de Ensino Individualizado (PEI)")
    with col3:
        if st.button("❌ Excluir Aluno", type="primary"):
            if excluir_aprendiz(st.session_state.nome_aprendiz_ativo):
                st.success(f"Aprendiz '{st.session_state.nome_aprendiz_ativo}' excluído.")
                st.session_state.nome_aprendiz_ativo = None
                st.session_state.aprendiz_ativo = None
                st.rerun()
