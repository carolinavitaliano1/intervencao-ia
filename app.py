# app.py
import streamlit as st
import datetime
import json
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide",
    page_title="INTERVENÇÃO IA",
    page_icon="🧠"
)

# --- FUNÇÕES DE BANCO DE DADOS (JSON) ---

# Define o caminho do arquivo do banco de dados
DB_PATH = 'pacientes.json'

# Função para carregar os pacientes do arquivo JSON
def carregar_dados():
    if not os.path.exists(DB_PATH):
        return {}  # Retorna um dicionário vazio se o arquivo não existir
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {} # Retorna dicionário vazio se o arquivo estiver vazio ou corrompido

# Função para salvar um novo paciente no arquivo JSON
def salvar_paciente(dados_paciente):
    pacientes = carregar_dados()
    nome_aluno = dados_paciente.get("nome_aluno")
    if nome_aluno:
        pacientes[nome_aluno] = dados_paciente
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(pacientes, f, ensure_ascii=False, indent=4)
        return True
    return False

# --- IMPORTAÇÃO DOS DADOS DA BNCC ---
from bncc_infantil import INFANTIL_DB
from bncc_fundamental import FUNDAMENTAL_DB
from bncc_medio import MEDIO_DB

# --- BANCO DE DADOS PRINCIPAL ---
BNCC_DATABASE = {
    "Educação Infantil": INFANTIL_DB,
    "Ensino Fundamental": FUNDAMENTAL_DB,
    "Ensino Médio": MEDIO_DB
}

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
    
    pacientes_cadastrados = carregar_dados()
    lista_nomes_pacientes = ["Novo Cadastro"] + list(pacientes_cadastrados.keys())
    
    st.session_state.paciente_selecionado = st.selectbox(
        "Selecione o Paciente:",
        options=lista_nomes_pacientes
    )
    
    st.markdown("---")

    # MODIFICAÇÃO: Renomeado "Anamnese Aprofundada" para "Cadastro de Paciente"
    pagina_selecionada = st.radio(
        "Navegue pelos Módulos:",
        ["Página Inicial", "Cadastro de Paciente", "Plano de Ensino Individualizado (PEI)", "Gerador de Atividades Adaptadas"],
        captions=["Visão geral", "Cadastre ou edite um paciente", "Crie metas e estratégias", "Adapte materiais pedagógicos"]
    )
    st.sidebar.markdown("---")
    st.info("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")


# --- LÓGICA DAS PÁGINAS ---

if pagina_selecionada == "Página Inicial":
    st.title("Bem-vinda à Versão Final da INTERVENÇÃO IA!")
    st.subheader("Plataforma estável, com banco de dados de pacientes e busca aprimorada.")
    st.markdown("---")
    st.success("Agora você pode cadastrar e salvar as informações dos seus pacientes!", icon="🚀")
    st.markdown("""
        **Navegue pelo menu à esquerda para acessar as ferramentas:**
        - **Cadastro de Paciente:** Adicione um novo paciente ou consulte as informações de um já existente.
        - **Plano de Ensino Individualizado (PEI):** Selecione um paciente e crie um PEI com base na BNCC.
        - **Gerador de Atividades Adaptadas:** Crie materiais acessíveis para o paciente selecionado.
    """)
    st.warning("Para começar, selecione 'Novo Cadastro' na caixa de seleção de pacientes e vá para a aba 'Cadastro de Paciente'.")


elif pagina_selecionada == "Cadastro de Paciente":
    # MODIFICAÇÃO: Renomeado o cabeçalho
    st.header("👤 Cadastro de Paciente")

    # Carrega os dados do paciente selecionado, se houver um
    dados_atuais = {}
    if st.session_state.paciente_selecionado != "Novo Cadastro":
        dados_atuais = pacientes_cadastrados.get(st.session_state.paciente_selecionado, {})
        st.info(f"Visualizando dados de: **{st.session_state.paciente_selecionado}**")
    else:
        st.info("Preencha os campos abaixo para realizar um novo cadastro.")

    with st.form("form_paciente", clear_on_submit=False):
        # --- SEÇÃO DADOS DO ESTUDANTE ---
        with st.expander("DADOS DO ESTUDANTE", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                nome_aluno = st.text_input("Nome do aluno:", value=dados_atuais.get("nome_aluno", ""))
                principal_responsavel = st.text_input("Principal responsável:", value=dados_atuais.get("principal_responsavel", ""))
                nome_escola = st.text_input("Nome da escola:", value=dados_atuais.get("nome_escola", ""))
                data_pei = st.date_input("Data da elaboração do PEI:", value=datetime.datetime.strptime(dados_atuais.get("data_pei", "2024-01-01"), "%Y-%m-%d").date())
                tipo_documento = st.text_input("Tipo de documento:", value=dados_atuais.get("tipo_documento", ""))
            with col2:
                data_nascimento_str = dados_atuais.get("data_nascimento", "2010-01-01")
                data_nascimento = st.date_input("Data de Nascimento:", value=datetime.datetime.strptime(data_nascimento_str, "%Y-%m-%d").date())
                parentesco = st.text_input("Grau de parentesco do responsável:", value=dados_atuais.get("parentesco", ""))
                ano_escolar = st.text_input("Ano escolar:", value=dados_atuais.get("ano_escolar", "5º"))
                duracao_pei = st.text_input("Duração do PEI:", value=dados_atuais.get("duracao_pei", ""))
                elaborado_por = st.text_input("Elaborado por:", value=dados_atuais.get("elaborado_por", ""))

            avali_habilidades = st.text_area("Avaliação das habilidades:", value=dados_atuais.get("avali_habilidades", ""))
            relatorio_multi = st.text_area("Relatório da equipe multidisciplinar:", value=dados_atuais.get("relatorio_multi", ""))

        # Adicione aqui as outras seções (DESENVOLVIMENTO E SAÚDE, ESCOLA E EQUIPE, etc.) da mesma forma
        # ...

        # Botão para salvar
        submitted = st.form_submit_button("Salvar Cadastro")
        if submitted:
            if not nome_aluno:
                st.error("O nome do aluno é obrigatório para salvar!")
            else:
                dados_paciente = {
                    "nome_aluno": nome_aluno,
                    "principal_responsavel": principal_responsavel,
                    "nome_escola": nome_escola,
                    "data_pei": data_pei.strftime("%Y-%m-%d"),
                    "tipo_documento": tipo_documento,
                    "data_nascimento": data_nascimento.strftime("%Y-%m-%d"),
                    "parentesco": parentesco,
                    "ano_escolar": ano_escolar,
                    "duracao_pei": duracao_pei,
                    "elaborado_por": elaborado_por,
                    "avali_habilidades": avali_habilidades,
                    "relatorio_multi": relatorio_multi,
                    # Adicione aqui os outros campos para salvar
                }
                if salvar_paciente(dados_paciente):
                    st.success(f"Paciente '{nome_aluno}' salvo com sucesso! Atualize a página ou selecione-o na lista para ver os dados.")
                    st.balloons()
                else:
                    st.error("Ocorreu um erro ao salvar o paciente.")


elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    
    # Verifica se um paciente foi selecionado
    if st.session_state.paciente_selecionado == "Novo Cadastro":
        st.warning("Por favor, selecione um paciente na barra lateral para criar um PEI.")
    else:
        st.success(f"Criando PEI para o paciente: **{st.session_state.paciente_selecionado}**")
        st.info("Utilize a base de dados completa da BNCC para fundamentar seu planejamento.")

        tab1, tab2 = st.tabs(["🎯 **Navegador da BNCC**", "💡 **Banco de Estratégias Clínicas**"])

        with tab1:
            etapa_ensino = st.selectbox("1. Selecione a Etapa de Ensino:", options=list(BNCC_DATABASE.keys()))
            # (O restante do seu código para a aba BNCC continua aqui...)
            # ...
        with tab2:
            st.subheader("Sugestão de Estratégias por Função Cognitiva")
            # (O restante do seu código para a aba de Estratégias continua aqui...)
            # ...


elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas (Avançado)")

    # Verifica se um paciente foi selecionado
    if st.session_state.paciente_selecionado == "Novo Cadastro":
        st.warning("Por favor, selecione um paciente na barra lateral para gerar atividades.")
    else:
        st.success(f"Gerando atividades para o paciente: **{st.session_state.paciente_selecionado}**")
        # (O restante do seu código para o Gerador de Atividades continua aqui...)
        # ...
