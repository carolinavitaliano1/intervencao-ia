import streamlit as st
import datetime
from database_utils import salvar_dados_cadastro, excluir_aprendiz

# --- CONFIGURAÇÃO DA PÁGINA E ESTADO ---
st.set_page_config(layout="wide", page_title="Prontuário do Aprendiz")

if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

if not st.session_state.get("nome_aprendiz_ativo"):
    st.session_state.edit_mode = True

# --- FUNÇÃO AUXILIAR ---
def get_radio_index(options_list, value):
    try:
        return options_list.index(value)
    except (ValueError, TypeError):
        return len(options_list) - 1

# --- MODO DE CRIAÇÃO/EDIÇÃO ---
if st.session_state.edit_mode:
    st.header("📝 Dados do Aprendiz")
    
    if st.session_state.get("aprendiz_ativo"):
        dados_cadastro = st.session_state.aprendiz_ativo.get("cadastro", {})
    else:
        dados_cadastro = {}
        
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
            with col1:
                diagnostico = st.text_input("Diagnóstico", value=dados_cadastro.get("diagnostico", ""))
            with col2:
                comorbidades = st.text_input("Comorbidades", value=dados_cadastro.get("comorbidades", ""))
            terapias = st.text_area("Terapias", value=dados_cadastro.get("terapias", ""))
            col1, col2 = st.columns(2)
            with col1:
                medico_responsavel = st.text_input("Médico responsável", value=dados_cadastro.get("medico_responsavel", ""))
            with col2:
                contato_medico = st.text_input("Contato (Médico)", value=dados_cadastro.get("contato_medico", ""))
            col1, col2, col3 = st.columns(3)
            with col1:
                medicacao_atual = st.text_input("Medicação atual", value=dados_cadastro.get("medicacao_atual", ""))
            with col2:
                horario_medicacao = st.text_input("Horário", value=dados_cadastro.get("horario_medicacao", ""))
            with col3:
                objetivo_medicacao = st.text_input("Objetivo", value=dados_cadastro.get("objetivo_medicacao", ""))
            alergia = st.text_area("Alergia", value=dados_cadastro.get("alergia", ""))

        with st.expander("ESCOLA E EQUIPE"):
            col1, col2 = st.columns(2)
            with col1:
                prof_principal = st.text_input("Professor Principal", value=dados_cadastro.get("prof_principal", ""))
                prof_principal_contato = st.text_input("Contato (Prof. Principal)", value=dados_cadastro.get("prof_principal_contato", ""))
            with col2:
                acomp_escolar = st.text_input("Acompanhante escolar", value=dados_cadastro.get("acomp_escolar", ""))
                acomp_escolar_contato = st.text_input("Contato (Acomp. Escolar)", value=dados_cadastro.get("acomp_escolar_contato", ""))

        with st.expander("AUTONOMIA"):
            radio_opts_sim_nao = ["Sim", "Não"]
            comunicacao = st.text_area("Formas de Comunicação", value=dados_cadastro.get("comunicacao", ""))
            comunicacao_alt = st.radio("Utiliza comunicação alternativa?", radio_opts_sim_nao, horizontal=True, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("comunicacao_alt")))
            col1, col2 = st.columns(2)
            with col1:
                fica_sozinho = st.radio("Consegue ficar em sala de aula sozinho(a)?", radio_opts_sim_nao, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("fica_sozinho")))
                usa_banheiro = st.radio("Consegue utilizar o banheiro sozinho(a)?", radio_opts_sim_nao, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("usa_banheiro")))
            with col2:
                bebe_agua = st.radio("Consegue beber água sozinho(a)?", radio_opts_sim_nao, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("bebe_agua")))
                mobilidade_reduzida = st.radio("Possui mobilidade reduzida?", radio_opts_sim_nao, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("mobilidade_reduzida")))
            costuma_crises = st.radio("Costuma ter crises?", ["Sim", "Não", "Raramente"], horizontal=True, index=get_radio_index(["Sim", "Não", "Raramente"], dados_cadastro.get("costuma_crises")))
            col1, col2 = st.columns(2)
            with col1:
                principais_gatilhos = st.text_area("Principais gatilhos", value=dados_cadastro.get("principais_gatilhos", ""))
            with col2:
                como_regula = st.text_area("Como se regula", value=dados_cadastro.get("como_regula", ""))

        with st.expander("AVALIAÇÃO GERAL"):
            col1, col2 = st.columns(2)
            with col1:
                dificuldades = st.text_area("Principais Dificuldades (restrições)", value=dados_cadastro.get("dificuldades", ""))
            with col2:
                potencialidades = st.text_area("Principais Potencialidades (o que gosta)", value=dados_cadastro.get("potencialidades", ""))
            st.markdown("---")
            radio_opts_sim_nao = ["Sim", "Não"]
            aval_multi = st.radio("Possui avaliação da equipe multi?", radio_opts_sim_nao, horizontal=True, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("aval_multi")))
            dev_habilidades = st.radio("Precisa desenvolver habilidades básicas?", radio_opts_sim_nao, horizontal=True, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("dev_habilidades")))
            adapt_materiais = st.radio("Possui necessidade de adaptação de materiais?", radio_opts_sim_nao, horizontal=True, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("adapt_materiais")))
            adapt_curriculo = st.radio("Possui necessidade de adaptação de currículo?", radio_opts_sim_nao, horizontal=True, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("adapt_curriculo")))
            disciplinas_apoio = st.text_area("Disciplinas que necessita de maior apoio", value=dados_cadastro.get("disciplinas_apoio", ""))
            anexos = st.file_uploader("Enviar anexos de avaliação anterior", accept_multiple_files=True)

        col_submit, col_cancel = st.columns(2)
        with col_submit:
            submitted = st.form_submit_button("✅ Salvar Prontuário")
        with col_cancel:
            if st.form_submit_button("❌ Cancelar"):
                st.session_state.edit_mode = False
                st.rerun()

        if submitted:
            if not nome_aluno:
                st.error("O nome do aluno é obrigatório!")
            else:
                novos_dados_cadastro = {
                    "data_nascimento": data_nascimento.strftime('%Y-%m-%d'), "idade": idade, "principal_responsavel": principal_responsavel, "grau_parentesco": grau_parentesco,
                    "nome_escola": nome_escola, "ano_escolar": ano_escolar, "diagnostico": diagnostico, "comorbidades": comorbidades, "terapias": terapias,
                    "medico_responsavel": medico_responsavel, "contato_medico": contato_medico, "medicacao_atual": medicacao_atual, "horario_medicacao": horario_medicacao,
                    "objetivo_medicacao": objetivo_medicacao, "alergia": alergia, "prof_principal": prof_principal,
                    "prof_principal_contato": prof_principal_contato, "acomp_escolar": acomp_escolar, "acomp_escolar_contato": acomp_escolar_contato,
                    "comunicacao": comunicacao, "comunicacao_alt": comunicacao_alt, "fica_sozinho": fica_sozinho, "usa_banheiro": usa_banheiro,
                    "bebe_agua": bebe_agua, "mobilidade_reduzida": mobilidade_reduzida, "costuma_crises": costuma_crises, "principais_gatilhos": principais_gatilhos,
                    "como_regula": como_regula, "dificuldades": dificuldades, "potencialidades": potencialidades, "aval_multi": aval_multi,
                    "dev_habilidades": dev_habilidades, "adapt_materiais": adapt_materiais, "adapt_curriculo": adapt_curriculo, "disciplinas_apoio": disciplinas_apoio,
                }
                salvar_dados_cadastro(nome_aluno, novos_dados_cadastro)
                
                if st.session_state.get("aprendiz_ativo") is None:
                    st.session_state.aprendiz_ativo = {}
                st.session_state.aprendiz_ativo['cadastro'] = novos_dados_cadastro
                st.session_state.nome_aprendiz_ativo = nome_aluno
                
                st.session_state.edit_mode = False
                st.success(f"Prontuário de '{nome_aluno}' salvo com sucesso!")
                st.rerun()

# --- MODO DE VISUALIZAÇÃO ---
else:
    if not st.session_state.get("nome_aprendiz_ativo"):
        st.info("Clique em 'Cadastrar Novo Aprendiz' na barra lateral para começar ou selecione um aprendiz na lista.")
        st.stop()
        
    st.header(f"Prontuário: {st.session_state.nome_aprendiz_ativo}")
    dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})
    
    with st.container(border=True):
        st.subheader("Dados do Estudante")
        col1, col2, col3 = st.columns(3)
        data_nasc_str = dados_cadastro.get('data_nascimento')
        col1.metric("Idade", dados_cadastro.get('idade') or "Não informada")
        if data_nasc_str:
            col2.metric("Data de Nasc.", datetime.datetime.strptime(data_nasc_str, '%Y-%m-%d').strftime("%d/%m/%Y"))
        else:
            col2.metric("Data de Nasc.", "N/A")
        col3.metric("Ano Escolar", dados_cadastro.get('ano_escolar') or "Não informado")

    with st.container(border=True):
        st.subheader("Desenvolvimento e Saúde")
        col1, col2 = st.columns(2)
        col1.metric("Diagnóstico", dados_cadastro.get('diagnostico') or "Não informado")
        col2.metric("Comorbidades", dados_cadastro.get('comorbidades') or "Não informado")

    # ... (Adicione aqui os containers para visualizar TODAS as outras seções)

    st.write("")
    col1, col2, col3 = st.columns([1,1.2,1])
    with col1:
        if st.button("📝 Editar Prontuário"):
            st.session_state.edit_mode = True
            st.rerun()
    with col2:
        if st.button("➕ Novo Plano (PEI)"):
            st.switch_page("pages/3_Plano_de_Ensino_Individualizado (PEI).py")
    with col3:
        if st.button("❌ Excluir Aluno", type="primary"):
            if excluir_aprendiz(st.session_state.nome_aprendiz_ativo):
                st.success(f"Aprendiz '{st.session_state.nome_aprendiz_ativo}' excluído.")
                st.session_state.nome_aprendiz_ativo = None
                st.session_state.aprendiz_ativo = None
                st.rerun()
