import streamlit as st
from auth import enforce_login
enforce_login()
st.header("🎨 Gerador de Atividades Adaptadas")
if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral.")
    st.stop()
st.info(f"Gerando atividades para: **{st.session_state.nome_aprendiz_ativo}**")
# O código do gerador virá aqui
