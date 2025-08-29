import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide",
    page_title="INTERVENÇÃO IA",
    page_icon="🧠"
)

# --- BANCOS DE DADOS SIMULADOS ---

# Habilidades da BNCC
bncc_database = {
    "1º Ano - Ensino Fundamental": {
        "Língua Portuguesa": [
            {"codigo": "EF01LP02", "descricao": "Escrever, espontaneamente ou por ditado, palavras e frases de forma alfabética.", "tags": ["escrita", "alfabetizacao"]},
            {"codigo": "EF01LP05", "descricao": "Reconhecer o sistema de escrita alfabética como representação dos sons da fala.", "tags": ["leitura", "consciencia fonologica"]},
        ],
        "Matemática": [
            {"codigo": "EF01MA01", "descricao": "Utilizar números naturais como indicador de quantidade ou de ordem em diferentes situações cotidianas.", "tags": ["numeros", "contagem"]},
            {"codigo": "EF01MA06", "descricao": "Construir fatos básicos da adição e utilizá-los em procedimentos de cálculo para resolver problemas.", "tags": ["calculo", "soma", "problemas"]},
        ]
    },
    "2º Ano - Ensino Fundamental": {
        "Língua Portuguesa": [
            {"codigo": "EF12LP01", "descricao": "Ler palavras novas com precisão na decodificação, no caso de palavras de uso frequente, ler globalmente, por memorização.", "tags": ["leitura", "decodificacao"]},
        ],
        "Matemática": [
             {"codigo": "EF02MA06", "descricao": "Resolver e elaborar problemas de adição e de subtração, envolvendo números de até três ordens, com os significados de juntar, acrescentar, separar, retirar.", "tags": ["calculo", "soma", "subtracao", "problemas"]}
        ]
    }
}

# Estratégias de Intervenção (Inspirado nos materiais de referência)
estrategias_database = {
    "Dislexia / Dificuldades de Leitura": [
        "Utilizar textos com fontes maiores e maior espaçamento (ex: OpenDyslexic).",
        "Trabalhar a consciência fonológica com jogos de rimas e aliteração.",
        "Usar marcadores de texto ou réguas de leitura para guiar os olhos.",
        "Oferecer audiolivros ou softwares de leitura de tela como apoio.",
        "Método fônico: Focar na relação entre letras e sons de forma explícita."
    ],
    "Discalculia / Dificuldades de Matemática": [
        "Usar materiais concretos (blocos, ábaco, material dourado) para representar números e operações.",
        "Dividir problemas matemáticos complexos em etapas menores.",
        "Utilizar papel quadriculado para alinhar números em cálculos.",
        "Ensinar o uso de calculadora para tarefas complexas, focando no raciocínio do problema.",
        "Jogos de tabuleiro que envolvam contagem e cálculo."
    ],
    "TDAH / Déficit de Atenção": [
        "Dividir tarefas longas em blocos de tempo menores (Técnica Pomodoro).",
        "Oferecer instruções claras, curtas e em etapas (uma de cada vez).",
        "Permitir pausas para movimento e atividades motoras curtas.",
        "Usar checklists e organizadores visuais para guiar a execução de tarefas.",
        "Reduzir distrações no ambiente (visuais e sonoras)."
    ]
}


# --- MENU LATERAL DE NAVEGAÇÃO ---
st.sidebar.title("MENU DE FERRAMENTAS")
pagina_selecionada = st.sidebar.radio(
    "Navegue pelos Módulos:",
    ["Página Inicial", "Perfil do Aluno (Anamnese)", "Plano de Ensino Individualizado (PEI)", "Planejador de Sessão"]
)
st.sidebar.markdown("---")
st.sidebar.info("Este aplicativo foi concebido pela INTERVENÇÃO IA para apoiar profissionais da educação e saúde.")


# --- CONTEÚDO DAS PÁGINAS ---

# PÁGINA INICIAL
if pagina_selecionada == "Página Inicial":
    st.title("🧠 Bem-vinda à INTERVENÇÃO IA!")
    st.subheader("Seu assistente psicopedagógico para adaptação curricular")
    st.markdown("---")
    st.markdown(
        """
        Este é o seu painel de controle para criar, adaptar e planejar intervenções pedagógicas eficazes.
        
        **Use o menu à esquerda para navegar entre as ferramentas:**

        * **Perfil do Aluno (Anamnese):** Registre e organize as informações essenciais de seus alunos.
        * **Plano de Ensino Individualizado (PEI):** Crie metas alinhadas à BNCC e descubra estratégias de intervenção.
        * **Planejador de Sessão:** Estruture suas sessões de atendimento de forma rápida e objetiva.

        Estamos em constante desenvolvimento para trazer as melhores práticas baseadas em evidências para o seu dia a dia.
        """
    )

# PÁGINA DE ANAMNESE
elif pagina_selecionada == "Perfil do Aluno (Anamnese)":
    st.header("👤 Perfil do Aluno (Anamnese)")
    st.info("Registre aqui as informações essenciais para um planejamento individualizado.")

    with st.form("form_anamnese"):
        st.subheader("Dados de Identificação")
        nome_aluno = st.text_input("Nome Completo do Aluno")
        data_nascimento = st.date_input("Data de Nascimento")
        
        st.subheader("Informações Relevantes")
        diagnostico = st.text_input("Diagnóstico / Hipótese Diagnóstica")
        queixa_principal = st.text_area("Queixa Principal (relatada pela família/escola)")
        
        col1, col2 = st.columns(2)
        with col1:
            pontos_fortes = st.text_area("Potencialidades e Pontos Fortes")
        with col2:
            dificuldades = st.text_area("Desafios e Pontos de Atenção")
            
        submitted = st.form_submit_button("Salvar Informações")
        if submitted:
            st.success(f"Informações de {nome_aluno} salvas com sucesso! (Funcionalidade de exibição)")
            # Em uma versão futura, isso seria salvo em um banco de dados
            st.balloons()


# PÁGINA DO PEI
elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    
    tab1, tab2 = st.tabs(["🎯 Seleção de Habilidades (BNCC)", "💡 Banco de Estratégias de Intervenção"])

    with tab1:
        st.subheader("Sugestão de Habilidades para o PEI")
        col1, col2 = st.columns(2)
        with col1:
            ano_selecionado = st.selectbox("Ano Escolar:", options=list(bncc_database.keys()))
            disciplina_selecionada = st.selectbox("Disciplina:", options=list(bncc_database[ano_selecionado].keys()))
        with col2:
            palavras_chave_input = st.text_input("Dificuldades (separadas por vírgula):", placeholder="Ex: leitura, calculo")

        if st.button("Buscar Habilidades"):
            if palavras_chave_input:
                # Lógica da busca
                sugestoes = []
                palavras_chave_lista = [p.strip().lower() for p in palavras_chave_input.split(',')]
                for hab in bncc_database[ano_selecionado][disciplina_selecionada]:
                    if any(tag in palavras_chave_lista for tag in hab["tags"]):
                        sugestoes.append(hab)

                st.subheader("✅ Habilidades Recomendadas:")
                if sugestoes:
                    for s in sugestoes:
                        st.success(f"**Código:** {s['codigo']}\n\n**Descrição:** {s['descricao']}")
                else:
                    st.warning("Nenhuma habilidade encontrada.")
            else:
                st.error("Por favor, informe as dificuldades.")
    
    with tab2:
        st.subheader("Sugestão de Estratégias e Adaptações")
        st.info("Selecione a área de dificuldade para ver estratégias baseadas em evidências.")
        
        dificuldade_estrategia = st.selectbox(
            "Selecione a área de dificuldade principal:",
            options=list(estrategias_database.keys())
        )
        
        st.markdown("#### Estratégias Sugeridas:")
        for estrategia in estrategias_database[dificuldade_estrategia]:
            st.markdown(f"- {estrategia}")

# PÁGINA DO PLANEJADOR DE SESSÃO
elif pagina_selecionada == "Planejador de Sessão":
    st.header("🗓️ Planejador de Sessão")
    st.info("Estruture sua sessão de intervenção de forma rápida e prática.")

    with st.container(border=True):
        data_sessao = st.date_input("Data da Sessão")
        objetivo_sessao = st.text_input("Objetivo Principal da Sessão:", placeholder="Ex: Desenvolver a consciência silábica de palavras dissílabas.")
        materiais_necessarios = st.text_area("Materiais Necessários:", placeholder="Ex: Fichas com imagens, letras móveis, quadro branco.")
        
        st.markdown("##### Procedimento / Etapas da Sessão")
        etapa1 = st.text_input("1. Acolhimento / Atividade Inicial (Rapport):")
        etapa2 = st.text_input("2. Atividade Principal:")
        etapa3 = st.text_input("3. Atividade de Encerramento / Relaxamento:")
        
        observacoes = st.text_area("Observações e Análise do Desempenho:")

        if st.button("Gerar Plano de Sessão para Impressão"):
            st.success("Plano de sessão gerado!")
            # Em uma versão futura, isso geraria um PDF para download.
            st.balloons()
