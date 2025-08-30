# app.py
import streamlit as st
import datetime
import json
import os

# --- IMPORTAÇÃO DOS DADOS MODULARIZADOS ---
from bncc_infantil import INFANTIL_DB
from bncc_fundamental import FUNDAMENTAL_DB
from bncc_medio import MEDIO_DB

# --- MONTAGEM DO BANCO DE DADOS PRINCIPAL ---
BNCC_DATABASE = {
    "Educação Infantil": INFANTIL_DB,
    "Ensino Fundamental": FUNDAMENTAL_DB,
    "Ensino Médio": MEDIO_DB
}

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide",
    page_title="INTERVENÇÃO IA Final",
    page_icon="🧠"
)

# --- FUNÇÕES PARA SALVAR E CARREGAR DADOS ---
DB_FILE = "aprendizes.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)
        return {}
    
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def salvar_dados(dados_aprendiz):
    """Salva um novo aprendiz no arquivo JSON."""
    aprendizes = carregar_dados()
    nome_aluno = dados_aprendiz.get("nome_aluno")
    if nome_aluno:
        aprendizes[nome_aluno] = dados_aprendiz
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(aprendizes, f, ensure_ascii=False, indent=4)
        return True
    return False

# --- BANCOS DE DADOS ADICIONAIS ---
estrategias_por_funcao = {
    "Atenção Sustentada": ["Dividir tarefas longas em blocos menores com pausas programadas (Técnica Pomodoro).", "Usar timers visuais para marcar a duração da tarefa.", "Reduzir estímulos distratores no ambiente.", "Utilizar o 'sussurrofone' para a criança ouvir a própria voz durante a leitura."],
    "Memória de Trabalho (Operacional)": ["Fornecer instruções em etapas, uma de cada vez.", "Ensinar o uso de checklists e organizadores gráficos.", "Praticar jogos de memorização.", "Permitir o uso de tabuadas de apoio ou calculadora para focar no raciocínio."],
    "Controle Inibitório": ["Utilizar sinais de 'Pare e Pense' antes de responder.", "Praticar jogos que exigem espera e troca de turno.", "Estabelecer rotinas claras e previsíveis.", "Antecipar mudanças na rotina."],
    "Flexibilidade Cognitiva": ["Jogos que exigem mudança de regras.", "Apresentar o mesmo problema com diferentes formas de resolução.", "Criar histórias com finais alternativos.", "Incentivar o 'brainstorming' de ideias."],
    "Processamento Fonológico": ["Atividades lúdicas com rimas, aliterações e segmentação de sílabas/fonemas.", "Utilizar o método fônico multissensorial.", "Jogos de 'bingo de sons'.", "Uso de softwares focados em consciência fonológica."],
    "Processamento Visoespacial": ["Utilizar papel quadriculado para alinhar números e letras.", "Montagem de quebra-cabeças e LEGO seguindo modelos.", "Jogos de labirinto e 'encontre os 7 erros'.", "Destacar linhas ou usar réguas de leitura."]
}


# --- MENU LATERAL DE NAVEGAÇÃO ---
with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA")
    st.caption("Versão Final e Organizada")
    # MODIFICAÇÃO: Adicionada a nova página "Avaliação de Habilidades"
    pagina_selecionada = st.radio(
        "Navegue pelos Módulos:",
        ["Página Inicial", "Cadastro de Aprendiz", "Avaliação de Habilidades", "Plano de Ensino Individualizado (PEI)", "Gerador de Atividades Adaptadas"],
        captions=["Visão geral", "Registre informações do aluno", "Avalie as habilidades do aprendiz", "Crie metas e estratégias", "Adapte materiais pedagógicos"]
    )
    st.sidebar.markdown("---")
    st.info("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")


# --- LÓGICA DAS PÁGINAS ---

if pagina_selecionada == "Página Inicial":
    st.title("Bem-vinda à Versão Final da INTERVENÇÃO IA!")
    st.subheader("Plataforma estável, com código modular e busca aprimorada.")
    st.markdown("---")
    st.success("Tudo pronto! Adicionamos uma nova seção para Avaliação de Habilidades.", icon="🚀")
    st.markdown("""
        **Navegue pelo menu à esquerda para acessar as ferramentas:**
        - **Cadastro de Aprendiz:** Um guia estruturado para coletar e salvar informações cruciais.
        - **Avaliação de Habilidades:** Um formulário detalhado para avaliar o desenvolvimento do aprendiz.
        - **PEI com Inteligência Clínica:** Navegue pela BNCC completa e use a busca aprimorada por palavras-chave.
        - **Gerador de Atividades Adaptadas:** Crie materiais acessíveis com base nos princípios do DUA.
    """)

elif pagina_selecionada == "Cadastro de Aprendiz":
    st.header("👤 Cadastro de Aprendiz")

    with st.form("cadastro_form", clear_on_submit=True):
        # --- SEÇÃO DADOS DO ESTUDANTE ---
        with st.expander("DADOS DO ESTUDANTE", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                nome_aluno = st.text_input("Nome do aluno:")
                principal_responsavel = st.text_input("Principal responsável:")
                nome_escola = st.text_input("Nome da escola:")
                data_pei = st.date_input("Data da elaboração do PEI:")
                tipo_documento = st.text_input("Tipo de documento:")
            with col2:
                data_nascimento = st.date_input("Data de Nascimento:", min_value=datetime.date(1990, 1, 1))
                parentesco_responsavel = st.text_input("Grau de parentesco do responsável:")
                ano_escolar = st.text_input("Ano escolar:", value="5º")
                duracao_pei = st.text_input("Duração do PEI:")
                elaborado_por = st.text_input("Elaborado por:")

            avaliacao_habilidades = st.text_area("Avaliação das habilidades:")
            relatorio_multidisciplinar = st.text_area("Relatório da equipe multidisciplinar:")
        
        # ... (as outras seções do cadastro continuam aqui, como antes)
        
        # Botão para salvar
        submitted = st.form_submit_button("Salvar Cadastro do Aprendiz")
        if submitted:
            if not nome_aluno:
                st.error("O campo 'Nome do aluno' é obrigatório para salvar!")
            else:
                dados_para_salvar = { "nome_aluno": nome_aluno, } # Adicione os outros campos para salvar
                
                if salvar_dados(dados_para_salvar):
                    st.success(f"Aprendiz '{nome_aluno}' cadastrado com sucesso!")
                    st.balloons()
                else:
                    st.error("Ocorreu um erro ao salvar o cadastro.")


# --- NOVA PÁGINA DE AVALIAÇÃO DE HABILIDADES ---
elif pagina_selecionada == "Avaliação de Habilidades":
    st.header("📝 Avaliação de Habilidades")
    st.info("Modelo de avaliação baseado em Glat e Pletsch (2013, p. 28-32).")

    opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]

    # --- COMUNICAÇÃO ORAL ---
    st.subheader("Comunicação Oral")
    st.radio("1. Relata acontecimentos simples de modo compreensível.", opcoes, horizontal=True, key="hab1")
    st.radio("2. Lembra-se de dar recados após, aproximadamente, dez minutos.", opcoes, horizontal=True, key="hab2")
    st.radio("3. Comunica-se com outras pessoas usando um tipo de linguagem (gestos, comunicação alternativa) que não a oral.", opcoes, horizontal=True, key="hab3")
    st.radio("4. Utiliza a linguagem oral para se comunicar.", opcoes, horizontal=True, key="hab4")
    st.markdown("---")

    # --- LEITURA E ESCRITA ---
    st.subheader("Leitura e Escrita")
    st.radio("5. Conhece as letras do alfabeto.", opcoes, horizontal=True, key="hab5")
    st.radio("6. Reconhece a diferença entre letras e números.", opcoes, horizontal=True, key="hab6")
    st.radio("7. Domina sílabas simples.", opcoes, horizontal=True, key="hab7")
    st.radio("8. Ouve histórias com atenção.", opcoes, horizontal=True, key="hab8")
    st.radio("9. Consegue compreender e reproduzir histórias.", opcoes, horizontal=True, key="hab9")
    st.radio("10. Participa de jogos, atendendo às regras.", opcoes, horizontal=True, key="hab10")
    st.radio("11. Utiliza vocabulário adequado para a faixa etária.", opcoes, horizontal=True, key="hab11")
    st.radio("12. Sabe soletrar.", opcoes, horizontal=True, key="hab12")
    st.radio("13. Consegue escrever palavras simples.", opcoes, horizontal=True, key="hab13")
    st.radio("14. É capaz de assinar seu nome.", opcoes, horizontal=True, key="hab14")
    st.radio("15. Escreve endereços (com o objetivo de saber aonde chegar).", opcoes, horizontal=True, key="hab15")
    st.radio("16. Escreve pequenos textos e/ou bilhetes.", opcoes, horizontal=True, key="hab16")
    st.radio("17. Escreve sob ditado.", opcoes, horizontal=True, key="hab17")
    st.radio("18. Lê com compreensão pequenos textos.", opcoes, horizontal=True, key="hab18")
    st.radio("19. Lê e segue instruções impressas, por exemplo, em transportes públicos.", opcoes, horizontal=True, key="hab19")
    st.radio("20. Utiliza habilidade de leitura para obter informações, por exemplo, em jornais ou revistas.", opcoes, horizontal=True, key="hab20")
    st.markdown("---")

    # --- RACIOCÍNIO LÓGICO-MATEMÁTICO ---
    st.subheader("Raciocínio Lógico-Matemático")
    st.radio("21. Relaciona quantidade ao número.", opcoes, horizontal=True, key="hab21")
    st.radio("22. Soluciona problemas simples.", opcoes, horizontal=True, key="hab22")
    st.radio("23. Reconhece os valores dos preços dos produtos.", opcoes, horizontal=True, key="hab23")
    st.radio("24. Identifica o valor do dinheiro.", opcoes, horizontal=True, key="hab24")
    st.radio("25. Diferencia notas e moedas.", opcoes, horizontal=True, key="hab25")
    st.radio("26. Sabe agrupar o dinheiro para formar valores.", opcoes, horizontal=True, key="hab26")
    st.radio("27. Dá troco, quando necessário, nas atividades realizadas em sala de aula.", opcoes, horizontal=True, key="hab27")
    st.radio("28. Possui conceitos como cor, tamanho, formas geométricas, posição direita e esquerda, antecessor e sucessor.", opcoes, horizontal=True, key="hab28")
    st.radio("29. Reconhece a relação entre número e dias do mês (localização temporal).", opcoes, horizontal=True, key="hab29")
    st.radio("30. Identifica dias da semana.", opcoes, horizontal=True, key="hab30")
    st.radio("31. Reconhece horas.", opcoes, horizontal=True, key="hab31")
    st.radio("32. Reconhece horas em relógio digital.", opcoes, horizontal=True, key="hab32")
    st.radio("33. Reconhece horas exatas em relógio com ponteiros.", opcoes, horizontal=True, key="hab33")
    st.radio("34. Reconhece horas não exatas (meia hora ou sete minutos, por exemplo) em relógio digital.", opcoes, horizontal=True, key="hab34")
    st.radio("35. Reconhece horas não exatas em relógio com ponteiros.", opcoes, horizontal=True, key="hab35")
    st.radio("36. Associa horários aos acontecimentos.", opcoes, horizontal=True, key="hab36")
    st.radio("37. Reconhece as medidas de tempo (ano, hora, minuto, dia, semana etc.).", opcoes, horizontal=True, key="hab37")
    st.radio("38. Compreende conceitos matemáticos, como dobro e metade.", opcoes, horizontal=True, key="hab38")
    st.radio("39. Resolve operações matemáticas (adição ou subtração) com apoio de material concreto.", opcoes, horizontal=True, key="hab39")
    st.radio("40. Resolve operações matemáticas (adição ou subtração) sem apoio de material concreto.", opcoes, horizontal=True, key="hab40")
    st.radio("41. Demonstra curiosidade. Pergunta sobre o funcionamento das coisas.", opcoes, horizontal=True, key="hab41")
    st.radio("42. Gosta de jogos envolvendo lógica, como quebra-cabeças e charadas, entre outros.", opcoes, horizontal=True, key="hab42")
    st.radio("43. Organiza figuras em ordem lógica.", opcoes, horizontal=True, key="hab43")
    st.markdown("---")

    # --- INFORMÁTICA ---
    st.subheader("Informática na Escola")
    st.radio("44. Usa o computador com relativa autonomia (liga, desliga, acessa arquivos e programas).", opcoes, horizontal=True, key="hab44")
    st.radio("45. Sabe usar o computador e a internet quando disponibilizados na escola.", opcoes, horizontal=True, key="hab45")
    st.markdown("---")

    # --- ACADÊMICO E OBJETIVOS ---
    st.subheader("ACADÊMICO")
    st.text_area("Português:")
    st.text_area("Matemática:")
    st.text_area("Ciências:")
    st.text_area("História:")
    st.text_area("Geografia:")
    st.text_area("Artes:")
    st.text_area("Inglês:")
    st.text_area("Educação Física:")
    st.markdown("---")

    st.subheader("OBJETIVOS GERAIS")
    st.text_area("1)")
    st.text_area("2)")
    st.text_area("3)")
    st.markdown("---")

    st.subheader("ADAPTAÇÕES GERAIS ACADÊMICAS")
    col1, col2 = st.columns(2)
    with col1:
        st.text_area("Adaptações de conteúdo em sala")
    with col2:
        st.text_area("Adaptações em avaliações")


elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    # ... (código desta página continua o mesmo)
    
elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas (Avançado)")
    # ... (código desta página continua o mesmo)
