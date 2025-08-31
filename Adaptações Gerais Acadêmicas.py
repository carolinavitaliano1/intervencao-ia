import streamlit as st
import datetime
from database_utils import adicionar_plano_adaptacoes

st.set_page_config(layout="wide", page_title="Adaptações Gerais")
st.header("ETAPA 1: Adaptações Gerais")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral.")
    st.stop()

st.info(f"Criando plano de adaptações para: **{st.session_state.nome_aprendiz_ativo}**")

if st.button("🤖 Gerar Sugestões com IA"):
    with st.spinner("Aguarde, a IA está analisando os dados..."):
        st.session_state.objetivos_gerados = "1. Exemplo de objetivo gerado pela IA."
        st.session_state.adapt_sala_gerados = "1. Exemplo de adaptação em sala gerado pela IA."
        st.session_state.adapt_avaliacoes_gerados = "1. Exemplo de adaptação em avaliação gerado pela IA."
    st.success("Sugestões geradas!")

with st.form("form_adaptacoes"):
    objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=st.session_state.get("objetivos_gerados", ""), height=150)
    st.subheader("Adaptações Gerais Acadêmicas")
    col1, col2 = st.columns(2)
    with col1:
        adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=st.session_state.get("adapt_sala_gerados", ""), height=200)
    with col2:
        adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=st.session_state.get("adapt_avaliacoes_gerados", ""), height=200)

    submitted = st.form_submit_button("Salvar Adaptações")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        novo_plano = {
            "data_criacao": data_atual,
            "objetivos_gerais": objetivos_gerais,
            "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes,
        }
        adicionar_plano_adaptacoes(st.session_state.nome_aprendiz_ativo, novo_plano)
        
        if 'objetivos_gerados' in st.session_state: del st.session_state.objetivos_gerados
        if 'adapt_sala_gerados' in st.session_state: del st.session_state.adapt_sala_gerados
        if 'adapt_avaliacoes_gerados' in st.session_state: del st.session_state.adapt_avaliacoes_gerados
        
        st.success(f"Plano de Adaptações para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
