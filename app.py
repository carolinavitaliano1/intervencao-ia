import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide",
    page_title="INTERVENÇÃO IA 2.0",
    page_icon="🧠"
)

# --- BANCOS DE DADOS SIMULADOS (EXPANDIDOS COM BASE NOS MATERIAIS) ---

# Habilidades da BNCC (Mantido)
bncc_database = {
    "1º Ano - Ensino Fundamental": {
        "Língua Portuguesa": [{"codigo": "EF01LP02", "descricao": "Escrever, espontaneamente ou por ditado, palavras e frases de forma alfabética.", "tags": ["escrita", "alfabetizacao"]}, {"codigo": "EF01LP05", "descricao": "Reconhecer o sistema de escrita alfabética como representação dos sons da fala.", "tags": ["leitura", "consciencia fonologica"]}],
        "Matemática": [{"codigo": "EF01MA01", "descricao": "Utilizar números naturais como indicador de quantidade ou de ordem em diferentes situações cotidianas.", "tags": ["numeros", "contagem"]}, {"codigo": "EF01MA06", "descricao": "Construir fatos básicos da adição e utilizá-los em procedimentos de cálculo para resolver problemas.", "tags": ["calculo", "soma", "problemas"]}]
    },
    "2º Ano - Ensino Fundamental": {
        "Língua Portuguesa": [{"codigo": "EF12LP01", "descricao": "Ler palavras novas com precisão na decodificação, no caso de palavras de uso frequente, ler globalmente, por memorização.", "tags": ["leitura", "decodificacao"]}],
        "Matemática": [{"codigo": "EF02MA06", "descricao": "Resolver e elaborar problemas de adição e de subtração, envolvendo números de até três ordens, com os significados de juntar, acrescentar, separar, retirar.", "tags": ["calculo", "soma", "subtracao", "problemas"]}]
    }
}

# Estratégias de Intervenção por FUNÇÃO COGNITIVA AFETADA
estrategias_por_funcao = {
    "Atenção Sustentada": [
        "Dividir tarefas longas em blocos menores com pausas programadas (Técnica Pomodoro).",
        "Usar timers visuais (ex: ampulhetas de tempo) para marcar a duração da tarefa.",
        "Reduzir estímulos distratores no ambiente (visuais e sonoros).",
        "Utilizar o 'sussurrofone' para a criança ouvir a própria voz durante a leitura, mantendo o foco."
    ],
    "Memória de Trabalho (Operacional)": [
        "Fornecer instruções em etapas, uma de cada vez (verbalmente e por escrito/desenho).",
        "Ensinar o uso de checklists e organizadores gráficos para sequenciar tarefas.",
        "Praticar jogos de memorização (ex: Jogo da Memória, 'O que mudou na sala?').",
        "Reduzir a carga de memorização durante cálculos, permitindo o uso de tabuadas de apoio ou calculadora para focar no raciocínio."
    ],
    "Controle Inibitório": [
        "Utilizar sinais visuais ou verbais combinados para 'Pare e Pense' antes de responder.",
        "Praticar jogos que exigem espera e troca de turno (ex: jogos de tabuleiro, 'estátua').",
        "Estabelecer rotinas claras e previsíveis com quadros de rotina visuais.",
        "Antecipar mudanças na rotina para diminuir a impulsividade e a ansiedade."
    ],
    "Flexibilidade Cognitiva": [
        "Jogos que exigem mudança de regras no meio da partida (ex: 'Uno' com regras inventadas).",
        "Apresentar o mesmo problema com diferentes formas de resolução.",
        "Criar histórias com finais alternativos.",
        "Incentivar o 'brainstorming' de ideias sem julgamento inicial."
    ],
    "Processamento Fonológico": [
        "Atividades lúdicas com rimas, aliterações e segmentação de sílabas/fonemas.",
        "Utilizar o método fônico multissensorial (letras texturizadas, traçado no ar/areia).",
        "Jogos de 'bingo de sons' ou 'qual palavra começa com o som /f/?'.",
        "Uso de softwares e aplicativos focados em consciência fonológica."
    ],
    "Processamento Visoespacial": [
        "Utilizar papel quadriculado para alinhar números e letras.",
        "Montagem de quebra-cabeças e LEGO seguindo modelos.",
        "Jogos de labirinto e 'encontre os 7 erros'.",
        "Destacar linhas ou usar réguas de leitura para evitar pular linhas durante a leitura."
    ]
}


# --- MENU LATERAL DE NAVEGAÇÃO ---
with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA 2.0")
    pagina_selecionada = st.radio(
        "Navegue pelos Módulos:",
        ["Página Inicial", "Anamnese Aprofundada", "Plano de Ensino Individualizado (PEI)", "Gerador de Atividades Adaptadas", "Modelo RTI (Resposta à Intervenção)", "Base de Conhecimento"],
        captions=["Visão geral", "Registre informações do aluno", "Crie metas e estratégias", "Adapte materiais pedagógicos", "Planeje a intervenção em camadas", "Consulte conceitos-chave"]
    )
    st.markdown("---")
    st.info("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")


# --- LÓGICA DAS PÁGINAS ---

if pagina_selecionada == "Página Inicial":
    st.title("Bem-vinda à Versão Especialista da INTERVENÇÃO IA!")
    st.subheader("Uma plataforma aprimorada com base em neurociência e práticas psicopedagógicas.")
    st.markdown("---")
    st.info("Esta versão foi enriquecida com base nos materiais de referência sobre Neuropsicopedagogia, Resposta à Intervenção (RTI) e Adaptações Curriculares.", icon="📚")
    st.markdown("""
        **Navegue pelo menu à esquerda para acessar as novas e aprimoradas ferramentas:**
        - **Anamnese Aprofundada:** Um guia estruturado para coletar informações cruciais.
        - **PEI com Inteligência Clínica:** Receba sugestões de estratégias baseadas nas funções cognitivas.
        - **Gerador de Atividades Adaptadas:** Crie materiais acessíveis com base nos princípios do DUA.
        - **Modelo RTI:** Planeje suas intervenções de forma escalonada e sistemática.
        - **Base de Conhecimento:** Revise conceitos fundamentais a qualquer momento.
    """)

elif pagina_selecionada == "Anamnese Aprofundada":
    st.header("👤 Anamnese Aprofundada")
    st.info("Colete e organize dados essenciais para uma intervenção precisa.")

    with st.form("form_anamnese_avancado"):
        st.text_input("Nome Completo do Aluno")
        
        with st.expander("Dados de Identificação e Histórico"):
            col1, col2 = st.columns(2)
            with col1:
                st.date_input("Data de Nascimento")
                st.text_input("Escola")
            with col2:
                st.text_input("Ano Escolar")
                st.text_area("Queixa Principal (relatada pela família/escola)")
        
        with st.expander("Avaliação de Funções e Habilidades (Observação Clínica)"):
            st.write("**Funções Executivas:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.multiselect("Atenção", ["Sustentada", "Dividida", "Seletiva"])
            with col2:
                st.multiselect("Memória de Trabalho", ["Baixa capacidade", "Dificuldade em manipular informações"])
            with col3:
                st.multiselect("Flexibilidade Cognitiva", ["Rigidez", "Dificuldade em mudar de estratégia"])

            st.write("**Linguagem:**")
            st.multiselect("Habilidades Linguísticas", ["Atraso na fala", "Dificuldade de compreensão", "Vocabulário restrito", "Dificuldades na narrativa"])

            st.write("**Habilidades Motoras:**")
            st.multiselect("Coordenação Motora", ["Fina (dificuldade em escrever/desenhar)", "Ampla (desajeitado, dificuldade em esportes)"])
        
        with st.expander("Potencialidades e Interesses"):
            st.text_area("Descreva os pontos fortes, talentos e áreas de grande interesse do aluno.", height=100)

        if st.form_submit_button("Salvar Anamnese"):
            st.success("Anamnese salva com sucesso! (Funcionalidade de armazenamento em desenvolvimento)")
            st.balloons()


elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    
    tab1, tab2 = st.tabs(["🎯 **Seleção de Habilidades (BNCC)**", "💡 **Banco de Estratégias Clínicas**"])

    with tab1:
        st.subheader("Sugestão de Habilidades para o PEI")
        col1, col2 = st.columns(2)
        with col1:
            ano_selecionado = st.selectbox("Ano Escolar:", options=list(bncc_database.keys()), key="pei_ano")
            disciplina_selecionada = st.selectbox("Disciplina:", options=list(bncc_database[ano_selecionado].keys()), key="pei_disc")
        with col2:
            palavras_chave_input = st.text_input("Dificuldades (separadas por vírgula):", placeholder="Ex: leitura, calculo", key="pei_tags")

        if st.button("Buscar Habilidades", key="pei_buscar"):
            # Lógica de busca...
            st.success("Busca realizada!")

    with tab2:
        st.subheader("Sugestão de Estratégias por Função Cognitiva")
        st.warning("Selecione a principal função cognitiva que precisa ser trabalhada para ver estratégias de intervenção direcionadas.", icon="🎯")
        
        funcao_selecionada = st.selectbox(
            "Selecione a função cognitiva a ser estimulada:",
            options=list(estrategias_por_funcao.keys())
        )
        
        st.markdown(f"#### Estratégias para **{funcao_selecionada}**:")
        with st.container(border=True):
            for estrategia in estrategias_por_funcao[funcao_selecionada]:
                st.markdown(f"- {estrategia}")


elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas (Avançado)")
    st.info("Insira uma atividade e aplique diferentes níveis de adaptação curricular.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Atividade Original")
        enunciado_original = st.text_area("Enunciado Original:", "Resolva os problemas de matemática com atenção.")
        atividade_original = st.text_area("Conteúdo da Atividade:", "1. Maria tinha 5 maçãs e comprou mais 3. Com quantas ela ficou?\n2. João tinha 10 laranjas e deu 4 para seu amigo. Com quantas ele ficou?")
    
    with col2:
        st.subheader("Aplicar Adaptações")
        st.write("**1. Adaptação de Apresentação (Como se vê):**")
        adapt_fonte = st.checkbox("Sugerir fonte ampliada e maior espaçamento.")
        
        st.write("**2. Adaptação de Conteúdo (O que se faz):**")
        adapt_vocabulario = st.checkbox("Simplificar vocabulário do enunciado.")
        adapt_quantidade = st.checkbox("Reduzir a quantidade de questões pela metade.")

        st.write("**3. Adaptação Estrutural (Como se organiza):**")
        adapt_passos = st.checkbox("Sugerir a quebra de problemas em etapas (Ex: 1º Desenhe, 2º Calcule).")
        
        st.write("**4. Adaptação Avaliativa (Como se responde):**")
        adapt_resposta = st.checkbox("Sugerir formas de resposta alternativas (oral, desenho, múltipla escolha).")
    
    if st.button("Gerar Pré-visualização Adaptada"):
        st.subheader("✅ Pré-visualização da Atividade Adaptada")
        with st.container(border=True):
            enunciado_adaptado = enunciado_original
            if adapt_vocabulario:
                enunciado_adaptado = "Vamos calcular! Resolva as continhas abaixo."
            
            st.markdown(f"**Enunciado:** {enunciado_adaptado}")
            
            questoes = atividade_original.split('\n')
            if adapt_quantidade:
                questoes = questoes[:len(questoes)//2]
            
            for q in questoes:
                st.write(q)

            st.markdown("---")
            st.markdown("**Recomendações para Aplicação:**")
            if adapt_fonte: st.write("- Imprimir com fonte 20pt e espaçamento 1.5 entre linhas.")
            if adapt_passos: st.write("- Para cada problema, oriente o aluno a seguir as etapas: ler, desenhar, montar a conta, responder.")
            if adapt_resposta: st.write("- Permita que o aluno responda oralmente ou desenhando, caso tenha dificuldades na escrita.")


elif pagina_selecionada == "Modelo RTI (Resposta à Intervenção)":
    st.header("📊 Modelo RTI (Resposta à Intervenção)")
    st.info("Planeje e documente as ações de intervenção em 3 níveis (camadas), com base no modelo RTI.")

    st.subheader("Nível 1: Intervenção Universal (Toda a Turma)")
    st.text_area("Descreva as estratégias de ensino de alta qualidade e o monitoramento aplicados a todos os alunos da turma.", key="rti1", height=100)

    st.subheader("Nível 2: Intervenção em Pequeno Grupo (Alunos em Risco)")
    st.text_area("Descreva a intervenção direcionada, a frequência, a duração e os critérios de monitoramento para os alunos que não responderam adequadamente ao Nível 1.", key="rti2", height=150)

    st.subheader("Nível 3: Intervenção Individualizada e Intensiva")
    st.text_area("Descreva o plano de intervenção intensivo e individualizado para alunos que continuam com dificuldades significativas, muitas vezes envolvendo a equipe multidisciplinar.", key="rti3", height=150)
    
    if st.button("Salvar Plano RTI"):
        st.success("Plano de intervenção RTI salvo com sucesso! (Funcionalidade em desenvolvimento)")


elif pagina_selecionada == "Base de Conhecimento":
    st.header("📚 Base de Conhecimento")
    st.info("Consulte definições e implicações práticas de conceitos-chave da neuropsicopedagogia.")

    with st.expander("🧠 O que são Funções Executivas?"):
        st.markdown("""
            Conforme explorado em **'Neurociência e Transtornos de Aprendizagem'**, as Funções Executivas são um conjunto de habilidades mentais que nos permitem controlar e autorregular nossos pensamentos, emoções e ações. Elas são como o "CEO" do nosso cérebro.
            - **Principais componentes:** Memória de Trabalho, Controle Inibitório e Flexibilidade Cognitiva.
            - **Implicação Prática:** Alunos com déficits nas F.E. podem ter dificuldade em iniciar tarefas, se organizar, controlar impulsos e adaptar-se a novas regras, mesmo que saibam o conteúdo.
        """)
    
    with st.expander("🗣️ O que é Consciência Fonológica?"):
        st.markdown("""
            A consciência fonológica é a habilidade de perceber e manipular os sons da fala. É um pilar fundamental para a alfabetização, como destacado em diversos materiais sobre transtornos de aprendizagem.
            - **Não envolve letras, apenas sons.** Inclui a capacidade de identificar rimas, sílabas e fonemas (os menores sons da fala).
            - **Implicação Prática:** Dificuldades nesta área são um forte preditor de dislexia. A intervenção deve focar em jogos e atividades sonoras antes de focar intensamente na letra-som.
        """)

    with st.expander("🔢 O que é Senso Numérico?"):
        st.markdown("""
            Mencionado em estudos sobre discalculia, o senso numérico é uma compreensão intuitiva dos números, sua magnitude e suas relações. É a base para todo o aprendizado matemático.
            - **Envolve:** Estimar quantidades, comparar números (qual é maior?), entender que '5' é uma quantidade fixa de objetos.
            - **Implicação Prática:** Crianças com baixo senso numérico precisam de muitas atividades com materiais concretos (blocos, fichas) para construir essa noção antes de avançar para cálculos abstratos.
        """)
