import streamlit as st
import datetime
import os
from database_utils import salvar_dados_cadastro

st.set_page_config(layout="wide", page_title="Cadastro de Aprendiz")
st.header("👤 Prontuário do Aprendiz")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para visualizar o prontuário.")
    st.stop()

st.info(f"Visualizando dados de: **{st.session_state.nome_aprendiz_ativo}**")
dados_cadastro = st.session_state.get("aprendiz_ativo", {}).get("cadastro", {})

# Expander para editar os dados cadastrais
with st.expander("Editar Dados Cadastrais"):
    with st.form("form_cadastro"):
        nome_aluno = st.text_input("Nome do Aluno", value=st.session_state.nome_aprendiz_ativo, disabled=True)
        
        # --- SEUS CAMPOS DE CADASTRO AQUI ---
        col1, col2 = st.columns(2)
        with col1:
            principal_responsavel = st.text_input("Principal responsável:", value=dados_cadastro.get("principal_responsavel", ""))
            nome_escola = st.text_input("Nome da escola:", value=dados_cadastro.get("nome_escola", ""))
        with col2:
            parentesco_responsavel = st.text_input("Grau de parentesco do responsável:", value=dados_cadastro.get("parentesco_responsavel", ""))
            ano_escolar = st.text_input("Ano escolar:", value=dados_cadastro.get("ano_escolar", ""))

        submitted = st.form_submit_button("Salvar Alterações no Cadastro")
        if submitted:
            novos_dados_cadastro = {
                "principal_responsavel": principal_responsavel, "nome_escola": nome_escola,
                "parentesco_responsavel": parentesco_responsavel, "ano_escolar": ano_escolar,
            }
            salvar_dados_cadastro(nome_aluno, novos_dados_cadastro)
            st.success(f"Dados cadastrais de '{nome_aluno}' atualizados com sucesso!")
            # Atualiza o estado da sessão
            st.session_state.aprendiz_ativo["cadastro"] = novos_dados_cadastro

st.markdown("---")

# --- NOVA SEÇÃO: HISTÓRICO DE AVALIAÇÕES ---
st.subheader("Histórico de Avaliações")

lista_avaliacoes = st.session_state.get("aprendiz_ativo", {}).get("avaliacoes", [])

if not lista_avaliacoes:
    st.info("Nenhuma avaliação foi registrada para este aprendiz.")
else:
    # Mostra as avaliações da mais recente para a mais antiga
    for avaliacao in reversed(lista_avaliacoes):
        data = avaliacao.get("data_avaliacao", "Data não registrada")
        with st.expander(f"**Avaliação realizada em: {data}**"):
            st.write("---")
            st.write("**Comunicação Oral**")
            st.write(f"1. Relata acontecimentos simples: **{avaliacao.get('hab1')}**")
            # Adicione aqui outros campos importantes que você queira ver no resumo
            
            st.write("---")
            st.write("**Observação Acadêmica (Português)**")
            st.info(f"{avaliacao.get('portugues_acad', 'Nenhuma observação.')}")
