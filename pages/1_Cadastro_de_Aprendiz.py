import streamlit as st
import datetime
from database_utils import salvar_dados_cadastro, excluir_aprendiz

# --- CONFIGURAÇÃO DA PÁGINA E ESTADO ---
st.set_page_config(layout="wide", page_title="Prontuário do Aprendiz")

if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

if not st.session_state.get("nome_aprendiz_ativo"):
    st.session_state.edit_mode = True

# --- FUNÇÕES AUXILIARES ---
def get_radio_index(options_list, value):
    try:
        return options_list.index(value)
    except (ValueError, TypeError):
        return len(options_list) - 1

def calcular_idade(data_nascimento):
    if isinstance(data_nascimento, str):
        try:
            data_nascimento = datetime.datetime.strptime(data_nascimento, '%Y-%m-%d').date()
        except ValueError:
            return "Inválida"
    hoje = datetime.date.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

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
                idade = calcular_idade(data_nascimento)
                st.text_input("Idade", value=f"{idade} anos", disabled=True)
                grau_parentesco = st.text_input("Grau de parentesco do responsável", value=dados_cadastro.get("grau_parentesco", ""))
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

        with st.expander("ESCOLA E EQUIPE"):
            st.subheader("Contatos dos Profissionais")
            col1, col2 = st.columns(2)
            with col1:
                prof_principal = st.text_input("Professor Principal", value=dados_cadastro.get("prof_principal", ""))
                prof_principal_contato = st.text_input("Contato (Prof. Principal)", value=dados_cadastro.get("prof_principal_contato", ""))
            with col2:
                acomp_escolar = st.text_input("Acompanhante escolar", value=dados_cadastro.get("acomp_escolar", ""))
                acomp_escolar_contato = st.text_input("Contato (Acomp. Escolar)", value=dados_cadastro.get("acomp_escolar_contato", ""))
            st.markdown("---")
            col3, col4 = st.columns(2)
            with col3:
                coord_pedagogica = st.text_input("Coordenação Pedagógica", value=dados_cadastro.get("coord_pedagogica", ""))
                coord_pedagogica_contato = st.text_input("Contato (Coordenação)", value=dados_cadastro.get("coord_pedagogica_contato", ""))
            with col4:
                acomp_terapeutico = st.text_input("Acompanhante terapêutico", value=dados_cadastro.get("acomp_terapeutico", ""))
                acomp_terapeutico_contato = st.text_input("Contato (Acomp. Terapêutico)", value=dados_cadastro.get("acomp_terapeutico_contato", ""))
            prof_especialistas = st.text_area("Outros Professores Especialistas", value=dados_cadastro.get("prof_especialistas", ""))

        with st.expander("AUTONOMIA"):
            #... (código da seção Autonomia)
            pass

        with st.expander("AVALIAÇÃO GERAL"):
            #... (código da seção Avaliação)
            pass

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
                    "data_nascimento": data_nascimento.strftime('%Y-%m-%d'), "principal_responsavel": principal_responsavel, "grau_parentesco": grau_parentesco,
                    "nome_escola": nome_escola, "ano_escolar": ano_escolar,
                    "diagnostico": diagnostico, "comorbidades": comorbidades, "terapias": terapias, "medico_responsavel": medico_responsavel, "contato_medico": contato_medico,
                    "prof_principal": prof_principal, "prof_principal_contato": prof_principal_contato,
                    "acomp_escolar": acomp_escolar, "acomp_escolar_contato": acomp_escolar_contato,
                    "coord_pedagogica": coord_pedagogica, "coord_pedagogica_contato": coord_pedagogica_contato,
                    "acomp_terapeutico": acomp_terapeutico, "acomp_terapeutico_contato": acomp_terapeutico_contato,
                    "prof_especialistas": prof_especialistas
                    # Adicione aqui as variáveis das outras seções (Autonomia, Avaliação, etc.)
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
        # ... (visualização dos dados do estudante)
    
    with st.container(border=True):
        st.subheader("Desenvolvimento e Saúde")
        # ... (visualização dos dados de saúde)

    with st.container(border=True):
        st.subheader("Escola e Equipe")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Professor Principal:** {dados_cadastro.get('prof_principal') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('prof_principal_contato') or 'Não informado'}")
        with col2:
            st.write(f"**Acompanhante Escolar:** {dados_cadastro.get('acomp_escolar') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('acomp_escolar_contato') or 'Não informado'}")
        st.markdown("---")
        col3, col4 = st.columns(2)
        with col3:
            st.write(f"**Coordenação Pedagógica:** {dados_cadastro.get('coord_pedagogica') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('coord_pedagogica_contato') or 'Não informado'}")
        with col4:
            st.write(f"**Acompanhante Terapêutico:** {dados_cadastro.get('acomp_terapeutico') or 'N/A'}")
            st.caption(f"📞 {dados_cadastro.get('acomp_terapeutico_contato') or 'Não informado'}")
        st.write("**Outros Professores Especialistas:**")
        st.info(dados_cadastro.get('prof_especialistas') or "Nenhuma informação.")

    # ... (outros containers de visualização)

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
