import streamlit as st
import datetime
from database_utils import salvar_dados_cadastro, excluir_aprendiz

st.set_page_config(layout="wide", page_title="Prontuário do Aprendiz")

if 'edit_mode' not in st.session_state: st.session_state.edit_mode = False
if not st.session_state.get("nome_aprendiz_ativo"): st.session_state.edit_mode = True

def get_radio_index(options_list, value):
    try: return options_list.index(value)
    except: return len(options_list) - 1

if st.session_state.edit_mode:
    st.header("📝 Dados do Aprendiz")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {}) if st.session_state.get("aprendiz_ativo") else {}
    nome_preenchido = st.session_state.get("nome_aprendiz_ativo", "")

    with st.form("form_cadastro"):
        nome_aluno = st.text_input("Nome Completo do Aluno*", value=nome_preenchido)
        with st.expander("DADOS DO ESTUDANTE", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                data_nasc_str = dados_cadastro.get('data_nascimento', '2015-08-30')
                data_nascimento = st.date_input("Data de Nascimento", value=datetime.datetime.strptime(data_nasc_str, '%Y-%m-%d').date(), min_value=datetime.date(1970, 1, 1), max_value=datetime.date.today())
                idade = st.text_input("Idade (preenchimento manual)", value=dados_cadastro.get("idade", ""))
                principal_responsavel = st.text_input("Principal responsável", value=dados_cadastro.get("principal_responsavel", ""))
            with col2:
                grau_parentesco = st.text_input("Grau de parentesco do responsável", value=dados_cadastro.get("grau_parentesco", ""))
                nome_escola = st.text_input("Nome da escola", value=dados_cadastro.get("nome_escola", ""))
                ano_escolar = st.text_input("Ano escolar", value=dados_cadastro.get("ano_escolar", ""))

        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            col1, col2 = st.columns(2)
            with col1: diagnostico = st.text_input("Diagnóstico", value=dados_cadastro.get("diagnostico", ""))
            with col2: comorbidades = st.text_input("Comorbidades", value=dados_cadastro.get("comorbidades", ""))
            terapias = st.text_area("Terapias", value=dados_cadastro.get("terapias", ""))

        with st.expander("AUTONOMIA"):
            radio_opts_sim_nao = ["Sim", "Não"]
            comunicacao = st.text_area("Formas de Comunicação", value=dados_cadastro.get("comunicacao", ""))
            comunicacao_alt = st.radio("Utiliza comunicação alternativa?", radio_opts_sim_nao, horizontal=True, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("comunicacao_alt")))
            costuma_crises = st.radio("Costuma ter crises?", ["Sim", "Não", "Raramente"], horizontal=True, index=get_radio_index(["Sim", "Não", "Raramente"], dados_cadastro.get("costuma_crises")))

        with st.expander("AVALIAÇÃO GERAL"):
            col1, col2 = st.columns(2)
            with col1: dificuldades = st.text_area("Principais Dificuldades (restrições)", value=dados_cadastro.get("dificuldades", ""))
            with col2: potencialidades = st.text_area("Principais Potencialidades (o que gosta)", value=dados_cadastro.get("potencialidades", ""))
        
        submitted = st.form_submit_button("✅ Salvar Prontuário")
        if submitted:
            if not nome_aluno: st.error("O nome do aluno é obrigatório!")
            else:
                novos_dados_cadastro = {
                    "data_nascimento": data_nascimento.strftime('%Y-%m-%d'), "idade": idade, "principal_responsavel": principal_responsavel,
                    "grau_parentesco": grau_parentesco, "nome_escola": nome_escola, "ano_escolar": ano_escolar,
                    "diagnostico": diagnostico, "comorbidades": comorbidades, "terapias": terapias,
                    "comunicacao": comunicacao, "comunicacao_alt": comunicacao_alt, "costuma_crises": costuma_crises,
                    "dificuldades": dificuldades, "potencialidades": potencialidades,
                }
                salvar_dados_cadastro(nome_aluno, novos_dados_cadastro)
                st.session_state.nome_aprendiz_ativo = nome_aluno
                st.session_state.edit_mode = False
                st.success(f"Prontuário de '{nome_aluno}' salvo com sucesso!")
                st.rerun()
else:
    if not st.session_state.get("nome_aprendiz_ativo"):
        st.info("Clique em 'Cadastrar Novo Aprendiz' na barra lateral para começar ou selecione um aprendiz na lista.")
        st.stop()
    st.header(f"Prontuário: {st.session_state.nome_aprendiz_ativo}")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})
    with st.container(border=True):
        st.subheader("Dados do Estudante")
        # ... visualização
    # ... outros containers de visualização ...
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
            # ... lógica de exclusão
            pass
