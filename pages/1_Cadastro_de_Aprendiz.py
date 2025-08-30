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

        with st.expander("GENERALIZAÇÃO E METAS DE AVDs (Atividades de Vida Diária)"):
            st.info("Descreva as metas e os níveis de ajuda para AVDs, inspirado no modelo (1ª Ajuda Física, 2ª Gestual, 3º Independente).")
            avd_higiene = st.text_area("Metas e Estratégias para Higiene (Limpar-se, Escovar os dentes, etc.)", value=dados_cadastro.get("avd_higiene", ""))
            avd_alimentacao = st.text_area("Metas e Estratégias para Alimentação (Lanchar com independência, etc.)", value=dados_cadastro.get("avd_alimentacao", ""))

        # Botões de ação
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
                    "comunicacao": comunicacao, "comunicacao_alt": comunicacao_alt, "fica_sozinho": fica_sozinho, "usa_banheiro": usa_banheiro,
                    "bebe_agua": bebe_agua, "mobilidade_reduzida": mobilidade_reduzida, "costuma_crises": costuma_crises, "principais_gatilhos": principais_gatilhos,
                    "como_regula": como_regula, "avd_higiene": avd_higiene, "avd_alimentacao": avd_alimentacao,
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
        idade = "N/A"
        if data_nasc_str:
            idade = calcular_idade(data_nasc_str)
            col2.metric("Data de Nasc.", datetime.datetime.strptime(data_nasc_str, '%Y-%m-%d').strftime("%d/%m/%Y"))
        else:
            col2.metric("Data de Nasc.", "N/A")
        col1.metric("Idade", f"{idade} anos" if isinstance(idade, int) else "N/A")
        col3.metric("Ano Escolar", dados_cadastro.get('ano_escolar') or "Não informado")

    with st.container(border=True):
        st.subheader("Autonomia")
        st.write(f"**Formas de Comunicação:** {dados_cadastro.get('comunicacao') or 'Não informado'}")
        st.write(f"**Utiliza comunicação alternativa?** {dados_cadastro.get('comunicacao_alt') or 'Não informado'}")
        # Adicione outros campos de autonomia para visualização se desejar

    with st.container(border=True):
        st.subheader("Generalização e Metas de AVDs")
        st.write("**Metas para Higiene:**")
        st.info(dados_cadastro.get('avd_higiene') or "Nenhuma meta definida.")
        st.write("**Metas para Alimentação:**")
        st.info(dados_cadastro.get('avd_alimentacao') or "Nenhuma meta definida.")

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
