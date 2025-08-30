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
    pagina_selecionada = st.radio(
        "Navegue pelos Módulos:",
        ["Página Inicial", "Cadastro de Aprendiz", "Plano de Ensino Individualizado (PEI)", "Gerador de Atividades Adaptadas"],
        captions=["Visão geral", "Registre informações do aluno", "Crie metas e estratégias", "Adapte materiais pedagógicos"]
    )
    st.sidebar.markdown("---")
    st.info("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")


# --- LÓGICA DAS PÁGINAS ---

if pagina_selecionada == "Página Inicial":
    st.title("Bem-vinda à Versão Final da INTERVENÇÃO IA!")
    st.subheader("Plataforma estável, com código modular e busca aprimorada.")
    st.markdown("---")
    st.success("Tudo pronto! Revertemos para a estrutura organizada com arquivos separados e aprimoramos a busca de habilidades para resultados precisos.", icon="🚀")
    st.markdown("""
        **Navegue pelo menu à esquerda para acessar as ferramentas:**
        - **Cadastro de Aprendiz:** Um guia estruturado para coletar e salvar informações cruciais.
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

        # --- SEÇÃO DESENVOLVIMENTO E SAÚDE ---
        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            # ... (código dos campos desta seção)
            pass # Adicione os campos aqui

        # --- SEÇÃO ESCOLA E EQUIPE ---
        with st.expander("ESCOLA E EQUIPE"):
            # ... (código dos campos desta seção)
            pass # Adicione os campos aqui

        # --- SEÇÃO AUTONOMIA ---
        with st.expander("AUTONOMIA"):
            # ... (código dos campos desta seção)
            pass # Adicione os campos aqui
        
        # --- SEÇÃO AVALIAÇÃO ---
        with st.expander("AVALIAÇÃO E POTENCIALIDADES"):
            # ... (código dos campos desta seção)
            pass # Adicione os campos aqui
        
        # Botão para salvar
        submitted = st.form_submit_button("Salvar Cadastro do Aprendiz")
        if submitted:
            if not nome_aluno:
                st.error("O campo 'Nome do aluno' é obrigatório para salvar!")
            else:
                # Coleta todos os dados em um dicionário
                dados_para_salvar = {
                    "nome_aluno": nome_aluno,
                    "principal_responsavel": principal_responsavel,
                    "nome_escola": nome_escola,
                    "data_pei": data_pei.strftime('%Y-%m-%d'),
                    "tipo_documento": tipo_documento,
                    "data_nascimento": data_nascimento.strftime('%Y-%m-%d'),
                    "parentesco_responsavel": parentesco_responsavel,
                    "ano_escolar": ano_escolar,
                    "duracao_pei": duracao_pei,
                    "elaborado_por": elaborado_por,
                    "avaliacao_habilidades": avaliacao_habilidades,
                    "relatorio_multidisciplinar": relatorio_multidisciplinar
                    # Adicione aqui as outras variáveis dos outros campos para salvar
                }
                
                # Salva os dados no arquivo
                if salvar_dados(dados_para_salvar):
                    st.success(f"Aprendiz '{nome_aluno}' cadastrado com sucesso!")
                    st.balloons()
                else:
                    st.error("Ocorreu um erro ao salvar o cadastro.")


elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    st.info("Utilize a base de dados completa da BNCC para fundamentar seu planejamento.")
    
    tab1, tab2 = st.tabs(["🎯 **Navegador da BNCC**", "💡 **Banco de Estratégias Clínicas**"])

    with tab1:
        etapa_ensino = st.selectbox(
            "1. Selecione a Etapa de Ensino:",
            options=list(BNCC_DATABASE.keys())
        )

        lista_geral = []
        competencias = []

        if etapa_ensino == "Educação Infantil":
            grupo_etario = st.selectbox("2. Selecione o Grupo Etário:", options=list(BNCC_DATABASE["Educação Infantil"].keys()))
            campo_exp = st.selectbox("3. Selecione o Campo de Experiência:", options=list(BNCC_DATABASE["Educação Infantil"][grupo_etario].keys()))
            keywords_input = st.text_input("4. Filtrar por palavras-chave:", placeholder="Ex: corpo (use vírgula para mais de uma)")
            
            if st.button("Buscar Objetivos de Aprendizagem"):
                lista_geral = BNCC_DATABASE["Educação Infantil"][grupo_etario][campo_exp]

        elif etapa_ensino == "Ensino Fundamental":
            ano_escolar = st.selectbox("2. Selecione o Ano Escolar:", options=list(BNCC_DATABASE["Ensino Fundamental"].keys()))
            componente = st.selectbox("3. Selecione o Componente Curricular:", options=list(BNCC_DATABASE["Ensino Fundamental"][ano_escolar].keys()))
            keywords_input = st.text_input("4. Filtrar por palavras-chave:", placeholder="Ex: leitura (use vírgula para mais de uma)")

            if st.button("Buscar Habilidades"):
                lista_geral = BNCC_DATABASE["Ensino Fundamental"][ano_escolar][componente]
        
        elif etapa_ensino == "Ensino Médio":
            st.selectbox("2. Selecione o Ano (para referência):", ["1º Ano", "2º Ano", "3º Ano"])
            area_conhecimento = st.selectbox("3. Selecione a Área de Conhecimento:", options=list(BNCC_DATABASE["Ensino Médio"].keys()))
            keywords_input = st.text_input("4. Filtrar por palavras-chave:", placeholder="Ex: discursos (use vírgula para mais de uma)")

            if st.button("Buscar Competências e Habilidades"):
                lista_geral = BNCC_DATABASE["Ensino Médio"][area_conhecimento].get("Habilidades", [])
                competencias = BNCC_DATABASE["Ensino Médio"][area_conhecimento].get("Competências Específicas", [])
                
                st.subheader(f"✅ Competências Específicas de {area_conhecimento}")
                with st.container(border=True):
                    for comp in competencias:
                        st.markdown(f"**Competência {comp['codigo']}:** {comp['descricao']}")

        # --- LÓGICA DE FILTRAGEM E EXIBIÇÃO (CORRIGIDA) ---
        if lista_geral:
            st.markdown("---")
            st.subheader("✅ Resultados:")
            
            resultados_filtrados = []
            
            if keywords_input.strip():
                keywords = [key.strip().lower() for key in keywords_input.split(',')]
                for item in lista_geral:
                    descricao = item['descricao'].lower()
                    if all(key in descricao for key in keywords):
                        resultados_filtrados.append(item)
            else:
                resultados_filtrados = lista_geral

            if not resultados_filtrados:
                st.warning("Nenhum item encontrado com os critérios da sua busca.")
            else:
                st.write(f"**Exibindo {len(resultados_filtrados)} resultado(s):**")
                for item in resultados_filtrados:
                    st.success(f"**Código:** {item['codigo']}\n\n**Descrição:** {item['descricao']}")

    with tab2:
        st.subheader("Sugestão de Estratégias por Função Cognitiva")
        funcao_selecionada = st.selectbox("Selecione a função cognitiva a ser estimulada:", options=list(estrategias_por_funcao.keys()))
        st.markdown(f"#### Estratégias para **{funcao_selecionada}**:")
        with st.container(border=True):
            for estrategia in estrategias_por_funcao[funcao_selecionada]:
                st.markdown(f"- {estrategia}")

elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas (Avançado)")
    # ... (código mantido)
