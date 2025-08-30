import streamlit as st
import datetime
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
# Pega a última avaliação como base para preenchimento, se houver, senão usa um dicionário vazio
avaliacoes_anteriores = st.session_state.get("aprendiz_ativo", {}).get("avaliacoes", [])
dados_base = avaliacoes_anteriores[-1] if avaliacoes_anteriores else {}

opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]
default_option = "Não foi observado"

# --- INÍCIO DO FORMULÁRIO ---
with st.form("form_nova_avaliacao", clear_on_submit=True):

    with st.expander("**Comunicação oral**", expanded=True):
        hab1 = st.radio("1. Relata acontecimentos simples de modo compreensível.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab1", default_option)))
        hab2 = st.radio("2. Lembra-se de dar recados após, aproximadamente, dez minutos.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab2", default_option)))
        hab3 = st.radio("3. Comunica-se com outras pessoas usando um tipo de linguagem (gestos, comunicação alternativa) que não a oral.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab3", default_option)))
        hab4 = st.radio("4. Utiliza a linguagem oral para se comunicar.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab4", default_option)))

    with st.expander("**Leitura e escrita**", expanded=True):
        hab5 = st.radio("5. Conhece as letras do alfabeto.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab5", default_option)))
        hab6 = st.radio("6. Reconhece a diferença entre letras e números.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab6", default_option)))
        hab7 = st.radio("7. Domina sílabas simples.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab7", default_option)))
        hab8 = st.radio("8. Ouve histórias com atenção.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab8", default_option)))
        hab9 = st.radio("9. Consegue compreender e reproduzir histórias.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab9", default_option)))
        hab10 = st.radio("10. Participa de jogos, atendendo às regras.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab10", default_option)))
        hab11 = st.radio("11. Utiliza vocabulário adequado para a faixa etária.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab11", default_option)))
        hab12 = st.radio("12. Sabe soletrar.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab12", default_option)))
        hab13 = st.radio("13. Consegue escrever palavras simples.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab13", default_option)))
        hab14 = st.radio("14. É capaz de assinar seu nome.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab14", default_option)))
        hab15 = st.radio("15. Escreve endereços (com o objetivo de saber aonde chegar).", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab15", default_option)))
        hab16 = st.radio("16. Escreve pequenos textos e/ou bilhetes.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab16", default_option)))
        hab17 = st.radio("17. Escreve sob ditado.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab17", default_option)))
        hab18 = st.radio("18. Lê com compreensão pequenos textos.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab18", default_option)))
        hab19 = st.radio("19. Lê e segue instruções impressas, por exemplo, em transportes públicos.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab19", default_option)))
        hab20 = st.radio("20. Utiliza habilidade de leitura para obter informações, por exemplo, em jornais ou revistas.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab20", default_option)))

    with st.expander("**Raciocínio lógico-matemático**", expanded=True):
        hab21 = st.radio("21. Relaciona quantidade ao número.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab21", default_option)))
        hab22 = st.radio("22. Soluciona problemas simples.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab22", default_option)))
        hab23 = st.radio("23. Reconhece os valores dos preços dos produtos.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab23", default_option)))
        hab24 = st.radio("24. Identifica o valor do dinheiro.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab24", default_option)))
        hab25 = st.radio("25. Diferencia notas e moedas.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab25", default_option)))
        hab26 = st.radio("26. Sabe agrupar o dinheiro para formar valores.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab26", default_option)))
        hab27 = st.radio("27. Dá troco, quando necessário, nas atividades realizadas em sala de aula.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab27", default_option)))
        hab28 = st.radio("28. Possui conceitos como cor, tamanho, formas geométricas, posição direita e esquerda, antecessor e sucessor.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab28", default_option)))
        hab29 = st.radio("29. Reconhece a relação entre número e dias do mês (localização temporal).", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab29", default_option)))
        hab30 = st.radio("30. Identifica dias da semana.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab30", default_option)))
        hab31 = st.radio("31. Reconhece horas.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab31", default_option)))
        hab32 = st.radio("32. Reconhece horas em relógio digital.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab32", default_option)))
        hab33 = st.radio("33. Reconhece horas exatas em relógio com ponteiros.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab33", default_option)))
        hab34 = st.radio("34. Reconhece horas não exatas (meia hora ou sete minutos, por exemplo) em relógio digital.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab34", default_option)))
        hab35 = st.radio("35. Reconhece horas não exatas em relógio com ponteiros.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab35", default_option)))
        hab36 = st.radio("36. Associa horários aos acontecimentos.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab36", default_option)))
        hab37 = st.radio("37. Reconhece as medidas de tempo (ano, hora, minuto, dia, semana etc.).", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab37", default_option)))
        hab38 = st.radio("38. Compreende conceitos matemáticos, como dobro e metade.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab38", default_option)))
        hab39 = st.radio("39. Resolve operações matemáticas (adição ou subtração) com apoio de material concreto.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab39", default_option)))
        hab40 = st.radio("40. Resolve operações matemáticas (adição ou subtração) sem apoio de material concreto.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab40", default_option)))
        hab41 = st.radio("41. Demonstra curiosidade. Pergunta sobre o funcionamento das coisas.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab41", default_option)))
        hab42 = st.radio("42. Gosta de jogos envolvendo lógica, como quebra-cabeças e charadas, entre outros.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab42", default_option)))
        hab43 = st.radio("43. Organiza figuras em ordem lógica.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab43", default_option)))

    with st.expander("**Informática na escola**", expanded=True):
        hab44 = st.radio("44. Usa o computador com relativa autonomia (liga, desliga, acessa arquivos e programas).", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab44", default_option)))
        hab45 = st.radio("45. Sabe usar o computador e a internet quando disponibilizados na escola.", opcoes, horizontal=True, index=opcoes.index(dados_base.get("hab45", default_option)))

    with st.expander("**Avaliação / Observação Acadêmica**", expanded=True):
        portugues_acad = st.text_area("Português", value=dados_base.get("portugues_acad", ""))
        matematica_acad = st.text_area("Matemática", value=dados_base.get("matematica_acad", ""))
        ciencias_acad = st.text_area("Ciências", value=dados_base.get("ciencias_acad", ""))
        historia_acad = st.text_area("História", value=dados_base.get("historia_acad", ""))
        geografia_acad = st.text_area("Geografia", value=dados_base.get("geografia_acad", ""))
        artes_acad = st.text_area("Artes", value=dados_base.get("artes_acad", ""))
        ingles_acad = st.text_area("Inglês", value=dados_base.get("ingles_acad", ""))
        ed_fisica_acad = st.text_area("Educação Física", value=dados_base.get("ed_fisica_acad", ""))
    
    submitted = st.form_submit_button("Salvar Nova Avaliação")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        nova_avaliacao = {
            "data_avaliacao": data_atual,
            "hab1": hab1, "hab2": hab2, "hab3": hab3, "hab4": hab4, "hab5": hab5, "hab6": hab6, "hab7": hab7, "hab8": hab8, "hab9": hab9, "hab10": hab10,
            "hab11": hab11, "hab12": hab12, "hab13": hab13, "hab14": hab14, "hab15": hab15, "hab16": hab16, "hab17": hab17, "hab18": hab18, "hab19": hab19, "hab20": hab20,
            "hab21": hab21, "hab22": hab22, "hab23": hab23, "hab24": hab24, "hab25": hab25, "hab26": hab26, "hab27": hab27, "hab28": hab28, "hab29": hab29, "hab30": hab30,
            "hab31": hab31, "hab32": hab32, "hab33": hab33, "hab34": hab34, "hab35": hab35, "hab36": hab36, "hab37": hab37, "hab38": hab38, "hab39": hab39, "hab40": hab40,
            "hab41": hab41, "hab42": hab42, "hab43": hab43, "hab44": hab44, "hab45": hab45,
            "portugues_acad": portugues_acad, "matematica_acad": matematica_acad, "ciencias_acad": ciencias_acad, "historia_acad": historia_acad,
            "geografia_acad": geografia_acad, "artes_acad": artes_acad, "ingles_acad": ingles_acad, "ed_fisica_acad": ed_fisica_acad
        }
        
        adicionar_nova_avaliacao(st.session_state.nome_aprendiz_ativo, nova_avaliacao)
        st.success(f"Nova avaliação para '{st.session_state.nome_aprendiz_ativo}' registrada com sucesso em {data_atual}!")
        st.balloons()
        
        # Atualiza o estado da sessão localmente para refletir a nova avaliação
        if "avaliacoes" not in st.session_state.aprendiz_ativo:
            st.session_state.aprendiz_ativo["avaliacoes"] = []
        st.session_state.aprendiz_ativo["avaliacoes"].append(nova_avaliacao)
