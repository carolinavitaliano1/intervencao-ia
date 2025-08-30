import streamlit as st
import datetime
import os
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
            # ... (código desta seção como antes)
            pass

        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            # ... (código desta seção como antes)
            pass
        
        with st.expander("ESCOLA E EQUIPE"):
            # ... (código desta seção como antes)
            pass

        with st.expander("AUTONOMIA"):
            # ... (código desta seção como antes)
            pass

        with st.expander("GENERALIZAÇÃO E METAS DE AVDs (Atividades de Vida Diária)"):
            st.info("Descreva as metas e os níveis de ajuda para AVDs como Limpar-se, Escovar os dentes, Lanchar com independência, etc. ")
            metas_avd = st.text_area("Metas de Generalização e Estratégias", value=dados_cadastro.get("metas_avd", ""), height=200)

        with st.expander("AVALIAÇÃO, DIFICULDADES E POTENCIALIDADES"):
            col1, col2 = st.columns(2)
            with col1:
                dificuldades = st.text_area("Principais Dificuldades (restrições)", value=dados_cadastro.get("dificuldades", ""))
            with col2:
                potencialidades = st.text_area("Principais Potencialidades (o que gosta)", value=dados_cadastro.get("potencialidades", ""))
            
            st.markdown("---")
            radio_opts = ["Sim", "Não"]
            aval_multi = st.radio("Possui avaliação da equipe multi?", radio_opts, horizontal=True, index=get_radio_index(radio_opts, dados_cadastro.get("aval_multi")))
            dev_habilidades = st.radio("Precisa desenvolver habilidades básicas?", radio_opts, horizontal=True, index=get_radio_index(radio_opts, dados_cadastro.get("dev_habilidades")))
            adapt_materiais = st.radio("Possui necessidade de adaptação de materiais?", radio_opts, horizontal=True, index=get_radio_index(radio_opts, dados_cadastro.get("adapt_materiais")))
            adapt_curriculo = st.radio("Possui necessidade de adaptação de currículo?", radio_opts, horizontal=True, index=get_radio_index(radio_opts, dados_cadastro.get("adapt_curriculo")))
            
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
                # O dicionário 'novos_dados_cadastro' deve ser populado com todas as variáveis do formulário
                novos_dados_cadastro = {
                    "metas_avd": metas_avd,
                    "dificuldades": dificuldades,
                    "potencialidades": potencialidades,
                    "aval_multi": aval_multi,
                    "dev_habilidades": dev_habilidades,
                    "adapt_materiais": adapt_materiais,
                    "adapt_curriculo": adapt_curriculo,
                    "disciplinas_apoio": disciplinas_apoio,
                    # Adicione aqui todas as outras variáveis das outras seções (Estudante, Saúde, etc.)
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
    
    # Adicione aqui os containers para visualizar os novos dados
    with st.container(border=True):
        st.subheader("Generalização e Metas de AVDs")
        st.info(dados_cadastro.get('metas_avd') or "Nenhuma meta definida.")

    with st.container(border=True):
        st.subheader("Avaliação, Dificuldades e Potencialidades")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Principais Dificuldades:**")
            st.warning(dados_cadastro.get('dificuldades') or "Nenhuma informação.")
        with col2:
            st.write("**Principais Potencialidades:**")
            st.success(dados_cadastro.get('potencialidades') or "Nenhuma informação.")
        
        st.write(f"**Possui avaliação da equipe multi?** {dados_cadastro.get('aval_multi') or 'Não informado'}")
        st.write(f"**Necessita desenvolver habilidades básicas?** {dados_cadastro.get('dev_habilidades') or 'Não informado'}")
        st.write(f"**Necessita de adaptação de materiais?** {dados_cadastro.get('adapt_materiais') or 'Não informado'}")
        st.write(f"**Necessita de adaptação de currículo?** {dados_cadastro.get('adapt_curriculo') or 'Não informado'}")

    # ... outros containers de visualização ...

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
