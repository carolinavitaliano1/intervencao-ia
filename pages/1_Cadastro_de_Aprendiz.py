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
        data_nascimento = datetime.datetime.strptime(data_nascimento, '%Y-%m-%d').date()
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
                tempo_escola = st.text_input("Estuda nessa escola há quanto tempo", value=dados_cadastro.get("tempo_escola", ""))

        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            col1, col2, col3 = st.columns(3)
            with col1:
                diagnostico = st.text_input("Diagnóstico", value=dados_cadastro.get("diagnostico", ""))
            with col2:
                comorbidades = st.text_input("Comorbidades", value=dados_cadastro.get("comorbidades", ""))
            with col3:
                data_diag_str = dados_cadastro.get('data_diagnostico', datetime.date.today().strftime('%Y-%m-%d'))
                data_diagnostico = st.date_input("Data do diagnóstico", value=datetime.datetime.strptime(data_diag_str, '%Y-%m-%d').date())
            
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
            alteracao_sensorial = st.text_area("Alteração sensorial", value=dados_cadastro.get("alteracao_sensorial", ""))
            gatilhos_crises = st.text_area("Gatilhos para crises", value=dados_cadastro.get("gatilhos_crises", ""))
            outras_infos_saude = st.text_area("Outras informações relevantes", value=dados_cadastro.get("outras_infos_saude", ""))

        with st.expander("AUTONOMIA"):
            radio_opts_sim_nao = ["Sim", "Não"]
            comunicacao = st.text_area("Formas de Comunicação", value=dados_cadastro.get("comunicacao", ""))
            comunicacao_alt = st.radio("Utiliza comunicação alternativa?", radio_opts_sim_nao, horizontal=True, index=get_radio_index(radio_opts_sim_nao, dados_cadastro.get("comunicacao_alt")))
            # ... (demais campos de autonomia)

        with st.expander("AVALIAÇÃO GERAL"):
            # ... (campos de avaliação)
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
                    "data_nascimento": data_nascimento.strftime('%Y-%m-%d'), "principal_responsavel": principal_responsavel,
                    "grau_parentesco": grau_parentesco, "nome_escola": nome_escola, "ano_escolar": ano_escolar, "tempo_escola": tempo_escola,
                    "diagnostico": diagnostico, "comorbidades": comorbidades, "data_diagnostico": data_diagnostico.strftime('%Y-%m-%d'),
                    "terapias": terapias, "medico_responsavel": medico_responsavel, "contato_medico": contato_medico,
                    "medicacao_atual": medicacao_atual, "horario_medicacao": horario_medicacao, "objetivo_medicacao": objetivo_medicacao,
                    "alergia": alergia, "alteracao_sensorial": alteracao_sensorial, "gatilhos_crises": gatilhos_crises, "outras_infos_saude": outras_infos_saude,
                    "comunicacao": comunicacao, "comunicacao_alt": comunicacao_alt,
                    # ... inclua aqui todas as outras variáveis do formulário para salvar
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
        col1, col2, col3 = st.columns(3)
        data_nasc_str = dados_cadastro.get('data_nascimento')
        if data_nasc_str:
            idade = calcular_idade(data_nasc_str)
            col1.metric("Idade", f"{idade} anos")
            col2.metric("Data de Nasc.", datetime.datetime.strptime(data_nasc_str, '%Y-%m-%d').strftime("%d/%m/%Y"))
        else:
            col1.metric("Idade", "N/A")
            col2.metric("Data de Nasc.", "N/A")
        
        col3.metric("Ano Escolar", dados_cadastro.get('ano_escolar') or "Não informado")

    with st.container(border=True):
        st.subheader("Desenvolvimento e Saúde")
        # ... Adicione aqui a visualização para os campos restaurados
    
    # ... Adicione o container de visualização para a seção AUTONOMIA

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
