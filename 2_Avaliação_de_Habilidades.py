import streamlit as st
import datetime
from database_utils import adicionar_nova_avaliacao

st.set_page_config(layout="wide", page_title="Avaliação de Habilidades")
st.header("📝 Registrar Nova Avaliação de Habilidades")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para registrar uma nova avaliação.")
    st.stop()

st.info(f"Registrando uma nova avaliação para: **{st.session_state.nome_aprendiz_ativo}**")
st.caption("Fonte: Glat e Pletsch (2013, p. 28-32).")

opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]

with st.form("form_nova_avaliacao", clear_on_submit=True):
    # O formulário completo que já criamos antes
    st.subheader("Comunicação oral")
    hab1 = st.radio("1. Relata acontecimentos simples de modo compreensível.", opcoes, horizontal=True)
    # ... Coloque todas as outras 44 perguntas aqui ...
    
    st.markdown("---")
    st.subheader("Avaliação / Observação Acadêmica")
    portugues_acad = st.text_area("Português")
    # ... Coloque as outras áreas aqui ...

    submitted = st.form_submit_button("Salvar Nova Avaliação")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        nova_avaliacao = {
            "data_avaliacao": data_atual,
            "hab1": hab1,
            # ... inclua todas as outras 44 variáveis `habX` aqui ...
            "portugues_acad": portugues_acad,
            # ... inclua as outras áreas aqui ...
        }
        adicionar_nova_avaliacao(st.session_state.nome_aprendiz_ativo, nova_avaliacao)
        st.success(f"Nova avaliação para '{st.session_state.nome_aprendiz_ativo}' registrada com sucesso em {data_atual}!")
        st.balloons()
