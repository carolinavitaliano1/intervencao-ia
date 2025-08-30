import streamlit as st
import datetime
import os
from database_utils import salvar_dados_cadastro, excluir_aprendiz
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide", page_title="Prontuário do Aprendiz")

# --- GERENCIAMENTO DE ESTADO ---
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

# Se a página for carregada sem um aprendiz selecionado, força o modo de edição/criação
if not st.session_state.get("nome_aprendiz_ativo"):
    st.session_state.edit_mode = True

# --- INÍCIO DA RENDERIZAÇÃO DA PÁGINA ---

# --- MODO DE CRIAÇÃO/EDIÇÃO ---
if st.session_state.edit_mode:
    st.header("📝 Dados do Aprendiz")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})
    nome_preenchido = st.session_state.get("nome_aprendiz_ativo", "")

    with st.form("form_cadastro"):
        nome_aluno = st.text_input("Nome Completo do Aluno*", value=nome_preenchido)

        with st.expander("DADOS DO ESTUDANTE", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                principal_responsavel = st.text_input("Principal responsável:", value=dados_cadastro.get("principal_responsavel", ""))
                nome_escola = st.text_input("Nome da escola:", value=dados_cadastro.get("nome_escola", ""))
            with col2:
                parentesco_responsavel = st.text_input("Grau de parentesco do responsável:", value=dados_cadastro.get("parentesco_responsavel", ""))
                ano_escolar = st.text_input("Ano escolar:", value=dados_cadastro.get("ano_escolar", ""))
        
        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            col1, col2, col3 = st.columns(3)
            with col1:
                diagnostico = st.text_input("Diagnóstico:", value=dados_cadastro.get("diagnostico", ""))
            with col2:
                comorbidades = st.text_input("Comorbidades:", value=dados_cadastro.get("comorbidades", ""))
            with col3:
                data_diag_str = dados_cadastro.get("data_diagnostico", datetime.date.today().strftime('%Y-%m-%d'))
                data_diagnostico = st.date_input("Data do diagnóstico:", value=datetime.datetime.strptime(data_diag_str, '%Y-%m-%d').date())
            alergia = st.text_area("Alergia:", value=dados_cadastro.get("alergia", ""))

        with st.expander("AVALIAÇÃO E POTENCIALIDADES"):
            col1, col2 = st.columns(2)
            with col1:
                dificuldades = st.text_area("Principais Dificuldades (restrições):", value=dados_cadastro.get("dificuldades", ""))
            with col2:
                potencialidades = st.text_area("Principais Potencialidades (o que gosta):", value=dados_cadastro.get("potencialidades", ""))
            disciplinas_apoio = st.text_area("Disciplinas que necessita de maior apoio:", value=dados_cadastro.get("disciplinas_apoio", ""))
            anexos = st.file_uploader("Anexar Documentos", accept_multiple_files=True)
        
        col_submit, col_cancel = st.columns(2)
        with col_submit:
            submitted = st.form_submit_button("✅ Salvar Prontuário")
        with col_cancel:
            if st.form_submit_button("❌ Cancelar Edição"):
                st.session_state.edit_mode = False
                st.rerun()

        if submitted:
            if not nome_aluno:
                st.error("O nome do aluno é obrigatório!")
            else:
                novos_dados_cadastro = {
                    "principal_responsavel": principal_responsavel, "nome_escola": nome_escola,
                    "parentesco_responsavel": parentesco_responsavel, "ano_escolar": ano_escolar,
                    "diagnostico": diagnostico, "comorbidades": comorbidades,
                    "data_diagnostico": data_diagnostico.strftime('%Y-%m-%d'),
                    "alergia": alergia, "dificuldades": dificuldades, "potencialidades": potencialidades,
                    "disciplinas_apoio": disciplinas_apoio,
                }
                salvar_dados_cadastro(nome_aluno, novos_dados_cadastro)
                st.session_state.nome_aprendiz_ativo = nome_aluno
                st.session_state.edit_mode = False
                st.success(f"Prontuário de '{nome_aluno}' salvo com sucesso!")
                st.rerun()

# --- MODO DE VISUALIZAÇÃO ---
else:
    st.header(f"Prontuário: {st.session_state.nome_aprendiz_ativo}")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})
    
    with st.container(border=True):
        st.subheader("Dados do Estudante")
        col1, col2 = st.columns(2)
        col1.metric("Responsável", dados_cadastro.get('principal_responsavel') or "Não informado")
        col2.metric("Parentesco", dados_cadastro.get('parentesco_responsavel') or "Não informado")
        col1.metric("Escola", dados_cadastro.get('escola') or "Não informado")
        col2.metric("Ano Escolar", dados_cadastro.get('ano_escolar') or "Não informado")
    
    with st.container(border=True):
        st.subheader("Desenvolvimento e Saúde")
        col1, col2 = st.columns(2)
        col1.metric("Diagnóstico", dados_cadastro.get('diagnostico') or "Não informado")
        col2.metric("Comorbidades", dados_cadastro.get('comorbidades') or "Não informado")
        st.write("**Alergias:**")
        st.info(dados_cadastro.get('alergia') or "Nenhuma informação.")

    with st.container(border=True):
        st.subheader("Avaliação e Potencialidades")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Principais Dificuldades:**")
            st.info(dados_cadastro.get('dificuldades') or "Nenhuma informação.")
        with col2:
            st.write("**Principais Potencialidades:**")
            st.info(dados_cadastro.get('potencialidades') or "Nenhuma informação.")
        st.write("**Disciplinas com maior necessidade de apoio:**")
        st.info(dados_cadastro.get('disciplinas_apoio') or "Nenhuma informação.")

    st.write("")
    col1, col2, col3 = st.columns([1,1,1.1]) # Ajuste de largura
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
