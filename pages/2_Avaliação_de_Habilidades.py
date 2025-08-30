import streamlit as st
from database_utils import salvar_dados_aprendiz

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Avaliação de Habilidades")

st.header("📝 Avaliação de Habilidades")

# --- VERIFICA SE UM APRENDIZ ESTÁ SELECIONADO ---
if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para preencher ou visualizar a avaliação.")
    st.stop()

st.info(f"Preenchendo ou visualizando a avaliação para: **{st.session_state.nome_aprendiz_ativo}**")
st.caption("Fonte: Glat e Pletsch (2013, p. 28-32).")

# --- CARREGA DADOS E OPÇÕES PADRÃO ---
dados_avaliacao = st.session_state.get("aprendiz_ativo", {}).get("avaliacao", {})
opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]
default_option = "Não foi observado"

# --- INÍCIO DO FORMULÁRIO ---
with st.form("form_avaliacao"):

    # --- HABILIDADES DE COMUNICAÇÃO ORAL ---
    st.subheader("Comunicação oral")
    hab1 = st.radio("1. Relata acontecimentos simples de modo compreensível.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab1", default_option)))
    hab2 = st.radio("2. Lembra-se de dar recados após, aproximadamente, dez minutos.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab2", default_option)))
    hab3 = st.radio("3. Comunica-se com outras pessoas usando um tipo de linguagem (gestos, comunicação alternativa) que não a oral.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab3", default_option)))
    hab4 = st.radio("4. Utiliza a linguagem oral para se comunicar.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab4", default_option)))
    st.markdown("---")

    # --- HABILIDADES DE LEITURA E ESCRITA ---
    st.subheader("Leitura e escrita")
    hab5 = st.radio("5. Conhece as letras do alfabeto.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab5", default_option)))
    hab6 = st.radio("6. Reconhece a diferença entre letras e números.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab6", default_option)))
    hab7 = st.radio("7. Domina sílabas simples.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab7", default_option)))
    hab8 = st.radio("8. Ouve histórias com atenção.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab8", default_option)))
    hab9 = st.radio("9. Consegue compreender e reproduzir histórias.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab9", default_option)))
    hab10 = st.radio("10. Participa de jogos, atendendo às regras.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab10", default_option)))
    hab11 = st.radio("11. Utiliza vocabulário adequado para a faixa etária.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab11", default_option)))
    hab12 = st.radio("12. Sabe soletrar.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab12", default_option)))
    hab13 = st.radio("13. Consegue escrever palavras simples.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab13", default_option)))
    hab14 = st.radio("14. É capaz de assinar seu nome.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab14", default_option)))
    hab15 = st.radio("15. Escreve endereços (com o objetivo de saber aonde chegar).", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab15", default_option)))
    hab16 = st.radio("16. Escreve pequenos textos e/ou bilhetes.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab16", default_option)))
    hab17 = st.radio("17. Escreve sob ditado.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab17", default_option)))
    hab18 = st.radio("18. Lê com compreensão pequenos textos.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab18", default_option)))
    hab19 = st.radio("19. Lê e segue instruções impressas, por exemplo, em transportes públicos.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab19", default_option)))
    hab20 = st.radio("20. Utiliza habilidade de leitura para obter informações, por exemplo, em jornais ou revistas.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab20", default_option)))
    st.markdown("---")

    # --- HABILIDADES DE RACIOCÍNIO LÓGICO-MATEMÁTICO ---
    st.subheader("Raciocínio lógico-matemático")
    hab21 = st.radio("21. Relaciona quantidade ao número.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab21", default_option)))
    hab22 = st.radio("22. Soluciona problemas simples.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab22", default_option)))
    hab23 = st.radio("23. Reconhece os valores dos preços dos produtos.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab23", default_option)))
    hab24 = st.radio("24. Identifica o valor do dinheiro.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab24", default_option)))
    hab25 = st.radio("25. Diferencia notas e moedas.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab25", default_option)))
    hab26 = st.radio("26. Sabe agrupar o dinheiro para formar valores.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab26", default_option)))
    hab27 = st.radio("27. Dá troco, quando necessário, nas atividades realizadas em sala de aula.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab27", default_option)))
    hab28 = st.radio("28. Possui conceitos como cor, tamanho, formas geométricas, posição direita e esquerda, antecessor e sucessor.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab28", default_option)))
    hab29 = st.radio("29. Reconhece a relação entre número e dias do mês (localização temporal).", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab29", default_option)))
    hab30 = st.radio("30. Identifica dias da semana.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab30", default_option)))
    hab31 = st.radio("31. Reconhece horas.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab31", default_option)))
    hab32 = st.radio("32. Reconhece horas em relógio digital.", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab32", default_option)))
    hab33 = st.
