import streamlit as st
st.header("📝 Plano de Ensino Individualizado (PEI)")
if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral.")
    st.stop()
st.info(f"Criando PEI para: **{st.session_state.nome_aprendiz_ativo}**")
# O código da BNCC e do PEI virá aqui
