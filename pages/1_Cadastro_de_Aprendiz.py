import streamlit as st
import datetime
import os
from database_utils import salvar_dados_aprendiz

st.set_page_config(layout="wide", page_title="Cadastro de Aprendiz")
st.header("👤 Cadastro de Aprendiz")

dados_cadastro = {}
nome_preenchido = ""
if st.session_state.get("aprendiz_ativo"):
    st.info(f"Visualizando/editando dados de: **{st.session_state.nome_aprendiz_ativo}**")
    dados_cadastro = st.session_state.aprendiz_ativo.get("cadastro", {})
    nome_preenchido = st.session_state.nome_aprendiz_ativo
else:
    st.info("Preencha os campos abaixo para um novo cadastro.")

with st.form("form_cadastro"):
    nome_aluno = st.text_input("Nome do Aluno (obrigatório)", value=nome_preenchido)
    
    with st.expander("DADOS DO ESTUDANTE", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            principal_responsavel = st.text_input("Principal responsável:", value=dados_cadastro.get("principal_responsavel", ""))
            nome_escola = st.text_input("Nome da escola:", value=dados_cadastro.get("nome_escola", ""))
        with col2:
            parentesco_responsavel = st.text_input("Grau de parentesco do responsável:", value=dados_cadastro.get("parentesco_responsavel", ""))
            ano_escolar = st.text_input("Ano escolar:", value=dados_cadastro.get("ano_escolar", ""))

    with st.expander("AVALIAÇÃO E POTENCIALIDADES"):
        col1, col2 = st.columns(2)
        with col1:
            dificuldades = st.text_area("Principais Dificuldades (restrições):", value=dados_cadastro.get("dificuldades", ""))
        with col2:
            potencialidades = st.text_area("Principais Potencialidades (o que gosta):", value=dados_cadastro.get("potencialidades", ""))
        
        radio_opts = ["Sim", "Não"]
        aval_multi = st.radio("Possui avaliação da equipe multi?", radio_opts, horizontal=True, index=radio_opts.index(dados_cadastro.get("aval_multi", "Não")))
        disciplinas_apoio = st.text_area("Disciplinas que necessita de maior apoio:", value=dados_cadastro.get("disciplinas_apoio", ""))
        anexos = st.file_uploader("Anexar Documentos", accept_multiple_files=True)

    submitted = st.form_submit_button("Salvar Dados Cadastrais")
    if submitted:
        if not nome_aluno:
            st.error("O nome do aluno é obrigatório!")
        else:
            novos_dados_cadastro = {
                "principal_responsavel": principal_responsavel, "nome_escola": nome_escola,
                "parentesco_responsavel": parentesco_responsavel, "ano_escolar": ano_escolar,
                "dificuldades": dificuldades, "potencialidades": potencialidades, "aval_multi": aval_multi,
                "disciplinas_apoio": disciplinas_apoio,
            }
            salvar_dados_aprendiz(nome_aluno, novos_dados_cadastro, "cadastro")
            st.success(f"Dados cadastrais de '{nome_aluno}' salvos com sucesso!")
            st.balloons()
