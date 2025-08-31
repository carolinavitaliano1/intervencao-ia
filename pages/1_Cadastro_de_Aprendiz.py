import streamlit as st
import datetime
from database_utils import salvar_dados_cadastro, excluir_aprendiz

st.set_page_config(layout="wide", page_title="Prontuário do Aprendiz")

if 'edit_mode' not in st.session_state: st.session_state.edit_mode = False
if not st.session_state.get("nome_aprendiz_ativo"): st.session_state.edit_mode = True

def get_radio_index(options_list, value):
    try: return options_list.index(value)
    except (ValueError, TypeError): return len(options_list) - 1

if st.session_state.edit_mode:
    st.header("📝 Dados do Aprendiz")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {}) if st.session_state.get("aprendiz_ativo") else {}
    nome_preenchido = st.session_state.get("nome_aprendiz_ativo", "")

    with st.form("form_cadastro"):
        nome_aluno = st.text_input("Nome Completo do Aluno*", value=nome_preenchido)
        with st.expander("DADOS DO ESTUDANTE", expanded=True):
            # ... (código completo da seção)
            pass
        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            # ... (código completo da seção)
            pass
        with st.expander("ESCOLA E EQUIPE"):
            # ... (código completo da seção)
            pass
        with st.expander("AUTONOMIA"):
            # ... (código completo da seção)
            pass
        with st.expander("AVALIAÇÃO GERAL"):
            # ... (código completo da seção)
            pass
        
        submitted = st.form_submit_button("✅ Salvar Prontuário")
        if submitted:
            # ... (lógica de salvamento completa)
            pass
else:
    if not st.session_state.get("nome_aprendiz_ativo"):
        st.info("Clique em 'Cadastrar Novo Aprendiz' na barra lateral para começar ou selecione um aprendiz na lista.")
        st.stop()
    st.header(f"Prontuário: {st.session_state.nome_aprendiz_ativo}")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})
    
    with st.container(border=True):
        st.subheader("Dados do Estudante")
        # ... (visualização completa)
    with st.container(border=True):
        st.subheader("Desenvolvimento e Saúde")
        # ... (visualização completa)
    with st.container(border=True):
        st.subheader("Escola e Equipe")
        # ... (visualização completa)
    with st.container(border=True):
        st.subheader("Autonomia")
        # ... (visualização completa)
    with st.container(border=True):
        st.subheader("Avaliação Geral")
        # ... (visualização completa)
    with st.container(border=True):
        st.subheader("Histórico de Planos de Adaptações")
        # ... (visualização completa)

    st.write("")
    col1, col2, col3 = st.columns([1,1.8,1])
    with col1:
        if st.button("📝 Editar Prontuário"):
            st.session_state.edit_mode = True
            st.rerun()
    with col2:
        if st.button("➕ Novo Plano de Adaptações"):
            st.switch_page("pages/3_Adaptações_Gerais.py")
    with col3:
        if st.button("❌ Excluir Aluno", type="primary"):
            # ... (lógica de exclusão)
            pass
