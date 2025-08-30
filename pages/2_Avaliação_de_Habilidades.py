import streamlit as st
from database_utils import salvar_dados_aprendiz

st.set_page_config(layout="wide", page_title="Avaliação de Habilidades")
st.header("📝 Avaliação de Habilidades")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para preencher ou visualizar a avaliação.")
    st.stop()

st.info(f"Preenchendo ou visualizando a avaliação para: **{st.session_state.nome_aprendiz_ativo}**")
st.caption("Fonte: Glat e Pletsch (2013, p. 28-32).")

dados_avaliacao = st.session_state.get("aprendiz_ativo", {}).get("avaliacao", {})
opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]
default_option = "Não foi observado"

with st.form("form_avaliacao"):
    st.subheader("Comunicação oral")
    hab1 = st.radio("1. Relata acontecimentos simples de modo compreensível.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab1", default_option)))
    # ... (COLE AQUI TODAS AS 45 PERGUNTAS DE `st.radio` QUE EU TE ENVIEI ANTES)
    # Exemplo:
    # hab2 = st.radio("2. Lembra-se de dar recados...", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab2", default_option)))
    
    st.markdown("---")
    st.subheader("ACADÊMICO")
    portugues_acad = st.text_area("Português", value=dados_avaliacao.get("portugues_acad", ""))
    
    submitted = st.form_submit_button("Salvar Avaliação de Habilidades")
    if submitted:
        novos_dados_avaliacao = {
            "hab1": hab1,
            # "hab2": hab2,
            # ... (inclua todas as 45 variáveis `habX` aqui)
            "portugues_acad": portugues_acad,
        }
        salvar_dados_aprendiz(st.session_state.nome_aprendiz_ativo, novos_dados_avaliacao, "avaliacao")
        st.success(f"Avaliação de '{st.session_state.nome_aprendiz_ativo}' salva com sucesso!")
        if "avaliacao" not in st.session_state.aprendiz_ativo:
            st.session_state.aprendiz_ativo["avaliacao"] = {}
        st.session_state.aprendiz_ativo["avaliacao"].update(novos_dados_avaliacao)
