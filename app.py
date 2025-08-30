# app.py
import streamlit as st

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
    page_title="INTERVENÇÃO IA 6.0",
    page_icon="🧠"
)

# --- BANCOS DE DADOS ADICIONAIS ---
estrategias_por_funcao = {
    "Atenção Sustentada": ["Dividir tarefas longas em blocos menores com pausas programadas (Técnica Pomodoro).", "Usar timers visuais (ex: ampulhetas de tempo) para marcar a duração da tarefa.", "Reduzir estímulos distratores no ambiente (visuais e sonoros).", "Utilizar o 'sussurrofone' para a criança ouvir a própria voz durante a leitura, mantendo o foco."],
    "Memória de Trabalho (Operacional)": ["Fornecer instruções em etapas, uma de cada vez (verbalmente e por escrito/desenho).", "Ensinar o uso de checklists e organizadores gráficos para sequenciar tarefas.", "Praticar jogos de memorização (ex: Jogo da Memória, 'O que mudou na sala?').", "Reduzir a carga de memorização durante cálculos, permitindo o uso de tabuadas de apoio ou calculadora para focar no raciocínio."],
    "Controle Inibitório": ["Utilizar sinais visuais ou verbais combinados para 'Pare e Pense' antes de responder.", "Praticar jogos que exigem espera e troca de turno (ex: jogos de tabuleiro, 'estátua').", "Estabelecer rotinas claras e previsíveis com quadros de rotina visuais.", "Antecipar mudanças na rotina para diminuir a impulsividade e a ansiedade."],
    "Flexibilidade Cognitiva": ["Jogos que exigem mudança de regras no meio da partida (ex: 'Uno' com regras inventadas).", "Apresentar o mesmo problema com diferentes formas de resolução.", "Criar histórias com finais alternativos.", "Incentivar o 'brainstorming' de ideias sem julgamento inicial."],
    "Processamento Fonológico": ["Atividades lúdicas com rimas, aliterações e segmentação de sílabas/fonemas.", "Utilizar o método fônico multissensorial (letras texturizadas, traçado no ar/areia).", "Jogos de 'bingo de sons' ou 'qual palavra começa com o som /f/?'.", "Uso de softwares e aplicativos focados em consciência fonológica."],
    "Processamento Visoespacial": ["Utilizar papel quadriculado para alinhar números e letras.", "Montagem de quebra-cabeças e LEGO seguindo modelos.", "Jogos de labirinto e 'encontre os 7 erros'.", "Destacar linhas ou usar réguas de leitura para evitar pular linhas durante a leitura."]
}


# --- MENU LATERAL DE NAVEGAÇÃO ---
with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA 6.0")
    st.caption("Versão com Busca Inteligente")
    pagina_selecionada = st.radio(
        "Navegue pelos Módulos:",
        ["Página Inicial", "Anamnese Aprofundada", "Plano de Ensino Individualizado (PEI)", "Gerador de Atividades Adaptadas", "Modelo RTI (Resposta à Intervenção)", "Base de Conhecimento"],
        captions=["Visão geral", "Registre informações do aluno", "Crie metas e estratégias", "Adapte materiais pedagógicos", "Planeje a intervenção em camadas", "Consulte conceitos-chave"]
    )
    st.sidebar.markdown("---")
    st.info("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")


# --- LÓGICA DAS PÁGINAS ---

if pagina_selecionada == "Página Inicial":
    st.title("Bem-vinda à Versão 6.0 da INTERVENÇÃO IA!")
    st.subheader("Plataforma aprimorada com busca inteligente de habilidades.")
    st.markdown("---")
    st.success("Nova Funcionalidade! Atendendo ao seu pedido, o Navegador da BNCC agora possui um campo de busca para filtrar habilidades e objetivos por palavras-chave.", icon="🔍")
    st.markdown("""
        **Navegue pelo menu à esquerda para acessar as ferramentas:**
        - **Anamnese Aprofundada:** Um guia estruturado para coletar informações cruciais.
        - **PEI com Inteligência Clínica:** Navegue pela BNCC completa ou use a nova busca por palavras-chave para encontrar exatamente o que precisa.
        - **Gerador de Atividades Adaptadas:** Crie materiais acessíveis com base nos princípios do DUA.
        - **Modelo RTI:** Planeje suas intervenções de forma escalonada e sistemática.
        - **Base de Conhecimento:** Revise conceitos fundamentais a qualquer momento.
    """)

elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    st.info("Utilize a base de dados completa da BNCC para fundamentar seu planejamento.")
    
    tab1, tab2 = st.tabs(["🎯 **Navegador da BNCC**", "💡 **Banco de Estratégias Clínicas**"])

    with tab1:
        etapa_ensino = st.selectbox(
            "1. Selecione a Etapa de Ensino:",
            options=list(BNCC_DATABASE.keys())
        )

        resultados = []

        if etapa_ensino == "Educação Infantil":
            grupo_etario = st.selectbox("2. Selecione o Grupo Etário:", options=list(BNCC_DATABASE["Educação Infantil"].keys()))
            campo_exp = st.selectbox("3. Selecione o Campo de Experiência:", options=list(BNCC_DATABASE["Educação Infantil"][grupo_etario].keys()))
            keywords_input = st.text_input("Filtrar por palavras-chave (separadas por vírgula):", placeholder="Ex: corpo, gestos, sons")
            
            if st.button("Buscar Objetivos de Aprendizagem"):
                resultados = BNCC_DATABASE["Educação Infantil"][grupo_etario][campo_exp]

        elif etapa_ensino == "Ensino Fundamental":
            ano_escolar = st.selectbox("2. Selecione o Ano Escolar:", options=list(BNCC_DATABASE["Ensino Fundamental"].keys()))
            componente = st.selectbox("3. Selecione o Componente Curricular:", options=list(BNCC_DATABASE["Ensino Fundamental"][ano_escolar].keys()))
            keywords_input = st.text_input("Filtrar por palavras-chave (separadas por vírgula):", placeholder="Ex: leitura, texto, análise")

            if st.button("Buscar Habilidades"):
                resultados = BNCC_DATABASE["Ensino Fundamental"][ano_escolar][componente]
        
        elif etapa_ensino == "Ensino Médio":
            st.selectbox("2. Selecione o Ano (para referência):", ["1º Ano", "2º Ano", "3º Ano"])
            area_conhecimento = st.selectbox("3. Selecione a Área de Conhecimento:", options=list(BNCC_DATABASE["Ensino Médio"].keys()))
            keywords_input = st.text_input("Filtrar por palavras-chave (separadas por vírgula):", placeholder="Ex: discursos, mídias, análise")

            if st.button("Buscar Competências e Habilidades"):
                # No Ensino Médio, a busca se aplica apenas às habilidades.
                resultados = BNCC_DATABASE["Ensino Médio"][area_conhecimento].get("Habilidades", [])
                competencias = BNCC_DATABASE["Ensino Médio"][area_conhecimento].get("Competências Específicas", [])
                
                st.subheader(f"✅ Competências Específicas de {area_conhecimento}")
                with st.container(border=True):
                    for comp in competencias:
                        st.markdown(f"**Competência {comp['codigo']}:** {comp['descricao']}")

        # --- LÓGICA DE FILTRAGEM E EXIBIÇÃO ---
        if resultados:
            resultados_filtrados = []
            if keywords_input:
                keywords = [key.strip().lower() for key in keywords_input.split(',')]
                for item in resultados:
                    descricao = item['descricao'].lower()
                    if any(key in descricao for key in keywords):
                        resultados_filtrados.append(item)
            else:
                resultados_filtrados = resultados

            st.subheader("✅ Resultados Encontrados:")
            if not resultados_filtrados:
                st.warning("Nenhum item encontrado com as palavras-chave fornecidas.")
            else:
                for item in resultados_filtrados:
                    st.success(f"**Código:** {item['codigo']}\n\n**Descrição:** {item['descricao']}")

    with tab2:
        st.subheader("Sugestão de Estratégias por Função Cognitiva")
        funcao_selecionada = st.selectbox("Selecione a função cognitiva a ser estimulada:", options=list(estrategias_por_funcao.keys()))
        st.markdown(f"#### Estratégias para **{funcao_selecionada}**:")
        with st.container(border=True):
            for estrategia in estrategias_por_funcao[funcao_selecionada]:
                st.markdown(f"- {estrategia}")

# --- O RESTANTE DO CÓDIGO PARA AS OUTRAS PÁGINAS CONTINUA O MESMO ---
elif pagina_selecionada == "Anamnese Aprofundada":
    st.header("👤 Anamnese Aprofundada")
    st.info("Colete e organize dados essenciais para uma intervenção precisa.")
    with st.form("form_anamnese_avancado"):
        st.text_input("Nome Completo do Aluno")
        with st.expander("Dados de Identificação e Histórico"):
            st.date_input("Data de Nascimento"); st.text_input("Escola"); st.text_input("Ano Escolar"); st.text_area("Queixa Principal (relatada pela família/escola)")
        with st.expander("Avaliação de Funções e Habilidades (Observação Clínica)"):
            st.multiselect("Atenção", ["Sustentada", "Dividida", "Seletiva"]); st.multiselect("Memória de Trabalho", ["Baixa capacidade", "Dificuldade em manipular informações"]); st.multiselect("Flexibilidade Cognitiva", ["Rigidez", "Dificuldade em mudar de estratégia"])
            st.multiselect("Habilidades Linguísticas", ["Atraso na fala", "Dificuldade de compreensão", "Vocabulário restrito", "Dificuldades na narrativa"])
            st.multiselect("Coordenação Motora", ["Fina (dificuldade em escrever/desenhar)", "Ampla (desajeitado, dificuldade em esportes)"])
        with st.expander("Potencialidades e Interesses"):
            st.text_area("Descreva os pontos fortes, talentos e áreas de grande interesse do aluno.", height=100)
        if st.form_submit_button("Salvar Anamnese"): st.success("Anamnese salva com sucesso!")

elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas (Avançado)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Atividade Original"); enunciado_original = st.text_area("Enunciado Original:", "Resolva os problemas de matemática com atenção."); atividade_original = st.text_area("Conteúdo da Atividade:", "1. Maria tinha 5 maçãs e comprou mais 3. Com quantas ela ficou?\n2. João tinha 10 laranjas e deu 4 para seu amigo. Com quantas ele ficou?")
    with col2:
        st.subheader("Aplicar Adaptações"); adapt_fonte = st.checkbox("Sugerir fonte ampliada e maior espaçamento."); adapt_vocabulario = st.checkbox("Simplificar vocabulário do enunciado."); adapt_quantidade = st.checkbox("Reduzir a quantidade de questões pela metade."); adapt_passos = st.checkbox("Sugerir a quebra de problemas em etapas."); adapt_resposta = st.checkbox("Sugerir formas de resposta alternativas (oral, desenho, múltipla escolha).")
    if st.button("Gerar Pré-visualização Adaptada"):
        st.subheader("✅ Pré-visualização da Atividade Adaptada")
        with st.container(border=True):
            enunciado_adaptado = "Vamos calcular! Resolva as continhas abaixo." if adapt_vocabulario else enunciado_original
            st.markdown(f"**Enunciado:** {enunciado_adaptado}")
            questoes = atividade_original.split('\n')
            if adapt_quantidade: questoes = questoes[:len(questoes)//2] if len(questoes) > 1 else questoes
            for q in questoes: st.write(q)
            st.markdown("---"); st.markdown("**Recomendações para Aplicação:**")
            if adapt_fonte: st.write("- Imprimir com fonte 20pt e espaçamento 1.5 entre linhas.")
            if adapt_passos: st.write("- Para cada problema, oriente o aluno a seguir as etapas: ler, desenhar, montar a conta, responder.")
            if adapt_resposta: st.write("- Permita que o aluno responda oralmente ou desenhando, caso tenha dificuldades na escrita.")

elif pagina_selecionada == "Modelo RTI (Resposta à Intervenção)":
    st.header("📊 Modelo RTI (Resposta à Intervenção)"); st.text_area("Nível 1: Intervenção Universal (Toda a Turma)", key="rti1"); st.text_area("Nível 2: Intervenção em Pequeno Grupo (Alunos em Risco)", key="rti2"); st.text_area("Nível 3: Intervenção Individualizada e Intensiva", key="rti3"); st.button("Salvar Plano RTI")

elif pagina_selecionada == "Base de Conhecimento":
    st.header("📚 Base de Conhecimento")
    with st.expander("🧠 O que são Funções Executivas?"): st.markdown("São um conjunto de habilidades mentais que nos permitem controlar e autorregular nossos pensamentos, emoções e ações. Componentes: Memória de Trabalho, Controle Inibitório e Flexibilidade Cognitiva.")
    with st.expander("🗣️ O que é Consciência Fonológica?"): st.markdown("É a habilidade de perceber e manipular os sons da fala, sem envolver letras. Inclui rimas, sílabas e fonemas. Dificuldades nesta área são um forte preditor de dislexia.")
    with st.expander("🔢 O que é Senso Numérico?"): st.markdown("É uma compreensão intuitiva dos números, sua magnitude e suas relações. É a base para o aprendizado matemático. Crianças com baixo senso numérico precisam de atividades com materiais concretos.")
