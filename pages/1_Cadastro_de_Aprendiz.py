import streamlit as st
import datetime
from database_utils import salvar_dados_cadastro, excluir_aprendiz

# --- CONFIGURAÇÃO DA PÁGINA E ESTADO ---
st.set_page_config(layout="wide", page_title="Prontuário do Aprendiz")

if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

if not st.session_state.get("nome_aprendiz_ativo"):
    st.session_state.edit_mode = True

# --- FUNÇÃO AUXILIAR PARA RADIO BUTTONS ---
def get_radio_index(options_list, value):
    try:
        return options_list.index(value)
    except (ValueError, TypeError):
        return len(options_list) - 1

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
                data_nasc_str = dados_cadastro.get('data_nascimento', '2015-08-30')
                data_nascimento = st.date_input("Data de Nascimento", value=datetime.datetime.strptime(data_nasc_str, '%Y-%m-%d').date())
                principal_responsavel = st.text_input("Principal responsável", value=dados_cadastro.get("principal_responsavel", ""))
                nome_escola = st.text_input("Nome da escola", value=dados_cadastro.get("nome_escola", ""))
            with col2:
                grau_parentesco = st.text_input("Grau de parentesco do responsável", value=dados_cadastro.get("grau_parentesco", ""))
                ano_escolar = st.text_input("Ano escolar", value=dados_cadastro.get("ano_escolar", "5º"))
                tempo_escola = st.text_input("Estuda nessa escola há quanto tempo", value=dados_cadastro.get("tempo_escola", ""))

        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            col1, col2 = st.columns(2)
            with col1:
                diagnostico = st.text_input("Diagnóstico", value=dados_cadastro.get("diagnostico", ""))
            with col2:
                comorbidades = st.text_input("Comorbidades", value=dados_cadastro.get("comorbidades", ""))
            terapias = st.text_area("Terapias", value=dados_cadastro.get("terapias", ""))

        with st.expander("ESCOLA E EQUIPE"):
            st.subheader("Contatos dos Profissionais")
            col1, col2 = st.columns(2)
            with col1:
                prof_principal = st.text_input("Professor Principal", value=dados_cadastro.get("prof_principal", ""))
                prof_principal_contato = st.text_input("Telefone/WhatsApp (Prof. Principal)", value=dados_cadastro.get("prof_principal_contato", ""))
                prof_principal_email = st.text_input("E-mail (Prof. Principal)", value=dados_cadastro.get("prof_principal_email", ""))
            with col2:
                acomp_escolar = st.text_input("Acompanhante escolar", value=dados_cadastro.get("acomp_escolar", ""))
                acomp_escolar_contato = st.text_input("Telefone/WhatsApp (Acomp. Escolar)", value=dados_cadastro.get("acomp_escolar_contato", ""))
                acomp_escolar_email = st.text_input("E-mail (Acomp. Escolar)", value=dados_cadastro.get("acomp_escolar_email", ""))
            st.markdown("---")
            col3, col4 = st.columns(2)
            with col3:
                coord_pedagogica = st.text_input("Coordenação Pedagógica", value=dados_cadastro.get("coord_pedagogica", ""))
                coord_pedagogica_contato = st.text_input("Telefone/WhatsApp (Coordenação)", value=dados_cadastro.get("coord_pedagogica_contato", ""))
                coord_pedagogica_email = st.text_input("E-mail (Coordenação)", value=dados_cadastro.get("coord_pedagogica_email", ""))
            with col4:
                sala_recursos = st.text_input("Sala de recursos/AEE", value=dados_cadastro.get("sala_recursos", ""))
                resp_sala_recursos = st.text_input("Responsável (Sala de Recursos)", value=dados_cadastro.get("resp_sala_recursos", ""))
                resp_sala_recursos_contato = st.text_input("Contato (Sala de Recursos)", value=dados_cadastro.get("resp_sala_recursos_contato", ""))
        
        with st.expander("AVALIAÇÃO"):
            anexos = st.file_uploader("Enviar anexos de avaliação", accept_multiple_files=True)

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
                    "data_nascimento": data_nascimento.strftime('%Y-%m-%d'), "principal_responsavel": principal_responsavel,
                    "grau_parentesco": grau_parentesco, "nome_escola": nome_escola, "ano_escolar": ano_escolar, "tempo_escola": tempo_escola,
                    "diagnostico": diagnostico, "comorbidades": comorbidades, "terapias": terapias,
                    "prof_principal": prof_principal, "prof_principal_contato": prof_principal_contato, "prof_principal_email": prof_principal_email,
                    "acomp_escolar": acomp_escolar, "acomp_escolar_contato": acomp_escolar_contato, "acomp_escolar_email": acomp_escolar_email,
                    "coord_pedagogica": coord_pedagogica, "coord_pedagogica_contato": coord_pedagogica_contato, "coord_pedagogica_email": coord_pedagogica_email,
                    "sala_recursos": sala_recursos, "resp_sala_recursos": resp_sala_recursos, "resp_sala_recursos_contato": resp_sala_recursos_contato
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
        col2.metric("Escola", dados_cadastro.get('nome_escola') or "Não informado")
        col1.metric("Ano Escolar", dados_cadastro.get('ano_escolar') or "Não informado")

    with st.container(border=True):
        st.subheader("Desenvolvimento e Saúde")
        col1, col2 = st.columns(2)
        col1.metric("Diagnóstico", dados_cadastro.get('diagnostico') or "Não informado")
        col2.metric("Comorbidades", dados_cadastro.get('comorbidades') or "Não informado")
        st.write("**Terapias:**")
        st.info(dados_cadastro.get('terapias') or "Nenhuma informação.")
        
    with st.container(border=True):
        st.subheader("Escola e Equipe")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Professor Principal:** {dados_cadastro.get('prof_principal') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('prof_principal_contato') or 'N/A'}  |  ✉️ {dados_cadastro.get('prof_principal_email') or 'N/A'}")
        with col2:
            st.write(f"**Acompanhante Escolar:** {dados_cadastro.get('acomp_escolar') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('acomp_escolar_contato') or 'N/A'}  |  ✉️ {dados_cadastro.get('acomp_escolar_email') or 'N/A'}")
        st.markdown("---")
        col3, col4 = st.columns(2)
        with col3:
            st.write(f"**Coordenação Pedagógica:** {dados_cadastro.get('coord_pedagogica') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('coord_pedagogica_contato') or 'N/A'}  |  ✉️ {dados_cadastro.get('coord_pedagogica_email') or 'N/A'}")
        with col4:
            st.write(f"**Responsável Sala de Recursos:** {dados_cadastro.get('resp_sala_recursos') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('resp_sala_recursos_contato') or 'N/A'}")

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
