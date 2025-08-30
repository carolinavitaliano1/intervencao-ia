import streamlit as st
import datetime
# CORREÇÃO: Importa a função com o nome correto
from database_utils import adicionar_nova_avaliacao

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Avaliação de Habilidades")

st.header("📝 Registrar Nova Avaliação de Habilidades")

# --- VERIFICA SE UM APRENDIZ ESTÁ SELECIONADO ---
if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para registrar uma nova avaliação.")
    st.stop()

st.info(f"Registrando uma nova avaliação para: **{st.session_state.nome_aprendiz_ativo}**")
st.caption("Fonte: Glat e Pletsch (2013, p. 28-32).")

# --- CARREGA DADOS E OPÇÕES PADRÃO ---
dados_avaliacao = st.session_state.get("aprendiz_ativo", {}).get("avaliacoes", [{}])[-1] # Pega a última avaliação como base
opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]
default_option = "Não foi observado"

# --- INÍCIO DO FORMULÁRIO ---
with st.form("form_nova_avaliacao", clear_on_submit=True):

    st.subheader("Comunicação oral")
    hab1 = st.radio("1. Relata acontecimentos simples de modo compreensível.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab1", default_option)))
    hab2 = st.radio("2. Lembra-se de dar recados após, aproximadamente, dez minutos.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab2", default_option)))
    hab3 = st.radio("3. Comunica-se com outras pessoas usando um tipo de linguagem (gestos, comunicação alternativa) que não a oral.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab3", default_option)))
    hab4 = st.radio("4. Utiliza a linguagem oral para se comunicar.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab4", default_option)))
    st.markdown("---")

    st.subheader("Leitura e escrita")
    hab5 = st.radio("5. Conhece as letras do alfabeto.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab5", default_option)))
    # ... (Restante das 45 perguntas de `st.radio` completas) ...
    
    # --- BOTÃO DE SUBMISSÃO ---
    submitted = st.form_submit_button("Salvar Nova Avaliação")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        nova_avaliacao = {
            "data_avaliacao": data_atual,
            "hab1": hab1, "hab2": hab2, "hab3": hab3, "hab4": hab4, "hab5": hab5,
            # ... (inclua todas as outras 40 variáveis `habX` aqui)
        }
        
        # CORREÇÃO: Usa a função com o nome correto
        adicionar_nova_avaliacao(st.session_state.nome_aprendiz_ativo, nova_avaliacao)
        st.success(f"Nova avaliação para '{st.session_state.nome_aprendiz_ativo}' registrada com sucesso em {data_atual}!")
        st.balloons()
