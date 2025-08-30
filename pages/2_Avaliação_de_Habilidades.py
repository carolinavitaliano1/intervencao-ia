import streamlit as st
from database_utils import salvar_dados_aprendiz

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Avaliação de Habilidades")

st.header("📝 Modelo de Avaliação de Habilidades")

# --- VERIFICA SE UM APRENDIZ ESTÁ SELECIONADO ---
if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para preencher ou visualizar a avaliação.")
    st.stop() # Interrompe a execução da página se nenhum aprendiz for selecionado

st.info(f"Preenchendo ou visualizando a avaliação para: **{st.session_state.nome_aprendiz_ativo}**")
[cite_start]st.caption("Fonte: Glat e Pletsch (2013, p. 28-32). [cite: 6]")

# --- CARREGA DADOS E OPÇÕES PADRÃO ---
dados_avaliacao = st.session_state.get("aprendiz_ativo", {}).get("avaliacao", {})
opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]
default_option = "Não foi observado"

# --- INÍCIO DO FORMULÁRIO ---
with st.form("form_avaliacao"):

    # --- HABILIDADES DE COMUNICAÇÃO ORAL ---
    st.subheader("Comunicação Oral")
    [cite_start]hab1 = st.radio("1. Relata acontecimentos simples de modo compreensível. [cite: 2]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab1", default_option)))
    [cite_start]hab2 = st.radio("2. Lembra-se de dar recados após, aproximadamente, dez minutos. [cite: 2]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab2", default_option)))
    [cite_start]hab3 = st.radio("3. Comunica-se com outras pessoas usando um tipo de linguagem (gestos, comunicação alternativa) que não a oral. [cite: 2]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab3", default_option)))
    [cite_start]hab4 = st.radio("4. Utiliza a linguagem oral para se comunicar. [cite: 2]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab4", default_option)))
    st.markdown("---")

    # --- HABILIDADES DE LEITURA E ESCRITA ---
    st.subheader("Leitura e Escrita")
    [cite_start]hab5 = st.radio("5. Conhece as letras do alfabeto. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab5", default_option)))
    [cite_start]hab6 = st.radio("6. Reconhece a diferença entre letras e números. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab6", default_option)))
    [cite_start]hab7 = st.radio("7. Domina sílabas simples. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab7", default_option)))
    [cite_start]hab8 = st.radio("8. Ouve histórias com atenção. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab8", default_option)))
    [cite_start]hab9 = st.radio("9. Consegue compreender e reproduzir histórias. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab9", default_option)))
    [cite_start]hab10 = st.radio("10. Participa de jogos, atendendo às regras. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab10", default_option)))
    [cite_start]hab11 = st.radio("11. Utiliza vocabulário adequado para a faixa etária. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab11", default_option)))
    [cite_start]hab12 = st.radio("12. Sabe soletrar. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab12", default_option)))
    [cite_start]hab13 = st.radio("13. Consegue escrever palavras simples. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab13", default_option)))
    [cite_start]hab14 = st.radio("14. É capaz de assinar seu nome. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab14", default_option)))
    [cite_start]hab15 = st.radio("15. Escreve endereços (com o objetivo de saber aonde chegar). [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab15", default_option)))
    [cite_start]hab16 = st.radio("16. Escreve pequenos textos e/ou bilhetes. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab16", default_option)))
    [cite_start]hab17 = st.radio("17. Escreve sob ditado. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab17", default_option)))
    [cite_start]hab18 = st.radio("18. Lê com compreensão pequenos textos. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab18", default_option)))
    [cite_start]hab19 = st.radio("19. Lê e segue instruções impressas, por exemplo, em transportes públicos. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab19", default_option)))
    [cite_start]hab20 = st.radio("20. Utiliza habilidade de leitura para obter informações, por exemplo, em jornais ou revistas. [cite: 3]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab20", default_option)))
    st.markdown("---")

    # --- HABILIDADES DE RACIOCÍNIO LÓGICO-MATEMÁTICO ---
    st.subheader("Raciocínio Lógico-Matemático")
    [cite_start]hab21 = st.radio("21. Relaciona quantidade ao número. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab21", default_option)))
    [cite_start]hab22 = st.radio("22. Soluciona problemas simples. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab22", default_option)))
    [cite_start]hab23 = st.radio("23. Reconhece os valores dos preços dos produtos. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab23", default_option)))
    [cite_start]hab24 = st.radio("24. Identifica o valor do dinheiro. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab24", default_option)))
    [cite_start]hab25 = st.radio("25. Diferencia notas e moedas. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab25", default_option)))
    [cite_start]hab26 = st.radio("26. Sabe agrupar o dinheiro para formar valores. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab26", default_option)))
    [cite_start]hab27 = st.radio("27. Dá troco, quando necessário, nas atividades realizadas em sala de aula. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab27", default_option)))
    [cite_start]hab28 = st.radio("28. Possui conceitos como cor, tamanho, formas geométricas, posição direita e esquerda, antecessor e sucessor. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab28", default_option)))
    [cite_start]hab29 = st.radio("29. Reconhece a relação entre número e dias do mês (localização temporal). [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab29", default_option)))
    [cite_start]hab30 = st.radio("30. Identifica dias da semana. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab30", default_option)))
    [cite_start]hab31 = st.radio("31. Reconhece horas. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab31", default_option)))
    [cite_start]hab32 = st.radio("32. Reconhece horas em relógio digital. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab32", default_option)))
    [cite_start]hab33 = st.radio("33. Reconhece horas exatas em relógio com ponteiros. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab33", default_option)))
    [cite_start]hab34 = st.radio("34. Reconhece horas não exatas (meia hora ou sete minutos, por exemplo) em relógio digital. [cite: 4]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab34", default_option)))
    [cite_start]hab35 = st.radio("35. Reconhece horas não exatas em relógio com ponteiros. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab35", default_option)))
    [cite_start]hab36 = st.radio("36. Associa horários aos acontecimentos. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab36", default_option)))
    [cite_start]hab37 = st.radio("37. Reconhece as medidas de tempo (ano, hora, minuto, dia, semana etc.). [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab37", default_option)))
    [cite_start]hab38 = st.radio("38. Compreende conceitos matemáticos, como dobro e metade. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab38", default_option)))
    [cite_start]hab39 = st.radio("39. Resolve operações matemáticas (adição ou subtração) com apoio de material concreto. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab39", default_option)))
    [cite_start]hab40 = st.radio("40. Resolve operações matemáticas (adição ou subtração) sem apoio de material concreto. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab40", default_option)))
    [cite_start]hab41 = st.radio("41. Demonstra curiosidade. Pergunta sobre o funcionamento das coisas. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab41", default_option)))
    [cite_start]hab42 = st.radio("42. Gosta de jogos envolvendo lógica, como quebra-cabeças e charadas, entre outros. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab42", default_option)))
    [cite_start]hab43 = st.radio("43. Organiza figuras em ordem lógica. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab43", default_option)))
    st.markdown("---")

    # --- HABILIDADES DE INFORMÁTICA ---
    st.subheader("Informática na Escola")
    [cite_start]hab44 = st.radio("44. Usa o computador com relativa autonomia (liga, desliga, acessa arquivos e programas). [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab44", default_option)))
    [cite_start]hab45 = st.radio("45. Sabe usar o computador e a internet quando disponibilizados na escola. [cite: 5]", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab45", default_option)))
    st.markdown("---")

    # --- SEÇÃO ACADÊMICO ---
    st.subheader("Avaliação / Observação Acadêmica")
    [cite_start]portugues_acad = st.text_area("Português [cite: 8]", value=dados_avaliacao.get("portugues_acad", ""))
    [cite_start]matematica_acad = st.text_area("Matemática [cite: 8]", value=dados_avaliacao.get("matematica_acad", ""))
    [cite_start]ciencias_acad = st.text_area("Ciências [cite: 8]", value=dados_avaliacao.get("ciencias_acad", ""))
    [cite_start]historia_acad = st.text_area("História [cite: 8]", value=dados_avaliacao.get("historia_acad", ""))
    [cite_start]geografia_acad = st.text_area("Geografia [cite: 8]", value=dados_avaliacao.get("geografia_acad", ""))
    [cite_start]artes_acad = st.text_area("Artes [cite: 8]", value=dados_avaliacao.get("artes_acad", ""))
    [cite_start]ingles_acad = st.text_area("Inglês [cite: 8]", value=dados_avaliacao.get("ingles_acad", ""))
    [cite_start]ed_fisica_acad = st.text_area("Educação Física [cite: 8]", value=dados_avaliacao.get("ed_fisica_acad", ""))
    
    # --- BOTÃO DE SUBMISSÃO ---
    submitted = st.form_submit_button("Salvar Avaliação de Habilidades")
    if submitted:
        novos_dados_avaliacao = {
            "hab1": hab1, "hab2": hab2, "hab3": hab3, "hab4": hab4, "hab5": hab5, "hab6": hab6, "hab7": hab7, "hab8": hab8, "hab9": hab9, "hab10": hab10,
            "hab11": hab11, "hab12": hab12, "hab13": hab13, "hab14": hab14, "hab15": hab15, "hab16": hab16, "hab17": hab17, "hab18": hab18, "hab19": hab19, "hab20": hab20,
            "hab21": hab21, "hab22": hab22, "hab23": hab23, "hab24": hab24, "hab25": hab25, "hab26": hab26, "hab27": hab27, "hab28": hab28, "hab29": hab29, "hab30": hab30,
            "hab31": hab31, "hab32": hab32, "hab33": hab33, "hab34": hab34, "hab35": hab35, "hab36": hab36, "hab37": hab37, "hab38": hab38, "hab39": hab39, "hab40": hab40,
            "hab41": hab41, "hab42": hab42, "hab43": hab43, "hab44": hab44, "hab45": hab45,
            "portugues_acad": portugues_acad, "matematica_acad": matematica_acad, "ciencias_acad": ciencias_acad, "historia_acad": historia_acad,
            "geografia_acad": geografia_acad, "artes_acad": artes_acad, "ingles_acad": ingles_acad, "ed_fisica_acad": ed_fisica_acad
        }
        salvar_dados_aprendiz(st.session_state.nome_aprendiz_ativo, novos_dados_avaliacao, "avaliacao")
        st.success(f"Avaliação de '{st.session_state.nome_aprendiz_ativo}' salva com sucesso!")
        
        if "avaliacao" not in st.session_state.aprendiz_ativo:
            st.session_state.aprendiz_ativo["avaliacao"] = {}
        st.session_state.aprendiz_ativo["avaliacao"].update(novos_dados_avaliacao)
