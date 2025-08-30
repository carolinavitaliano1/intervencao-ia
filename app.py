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
UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def carregar_dados():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def salvar_dados_aprendiz(nome_aprendiz, dados_para_salvar, secao):
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    
    if secao not in aprendizes[nome_aprendiz]:
        aprendizes[nome_aprendiz][secao] = {}

    aprendizes[nome_aprendiz][secao].update(dados_para_salvar)
    
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True

# --- INICIALIZAÇÃO DO ESTADO DA SESSÃO ---
if 'aprendiz_ativo' not in st.session_state:
    st.session_state.aprendiz_ativo = None
    st.session_state.nome_aprendiz_ativo = None

# --- MENU LATERAL DE NAVEGAÇÃO ---
with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA")
    
    aprendizes_cadastrados = carregar_dados()
    lista_nomes = ["-- Novo Cadastro --"] + list(aprendizes_cadastrados.keys())
    
    index = 0
    if st.session_state.nome_aprendiz_ativo in lista_nomes:
        index = lista_nomes.index(st.session_state.nome_aprendiz_ativo)

    aprendiz_selecionado = st.selectbox(
        "Selecione o Aprendiz:",
        options=lista_nomes,
        index=index
    )

    if aprendiz_selecionado != "-- Novo Cadastro --":
        if st.session_state.nome_aprendiz_ativo != aprendiz_selecionado:
            st.session_state.aprendiz_ativo = aprendizes_cadastrados[aprendiz_selecionado]
            st.session_state.nome_aprendiz_ativo = aprendiz_selecionado
            st.rerun()
    else:
        st.session_state.aprendiz_ativo = None
        st.session_state.nome_aprendiz_ativo = None

    st.markdown("---")
    
    pagina_selecionada = st.radio(
        "Navegue pelos Módulos:",
        ["Cadastro de Aprendiz", "Avaliação de Habilidades", "Plano de Ensino Individualizado (PEI)", "Gerador de Atividades Adaptadas"],
        captions=["Dados do aluno", "Avaliação pedagógica", "Metas e estratégias", "Materiais pedagógicos"]
    )
    st.sidebar.markdown("---")
    st.info("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")

# --- LÓGICA DAS PÁGINAS ---

if pagina_selecionada == "Cadastro de Aprendiz":
    st.header("👤 Cadastro de Aprendiz")

    dados_cadastro = {}
    nome_preenchido = ""
    if st.session_state.aprendiz_ativo:
        st.info(f"Visualizando/editando dados de: **{st.session_state.nome_aprendiz_ativo}**")
        dados_cadastro = st.session_state.aprendiz_ativo.get("cadastro", {})
        nome_preenchido = st.session_state.nome_aprendiz_ativo
    else:
        st.info("Preencha os campos abaixo para um novo cadastro.")

    with st.form("form_cadastro"):
        nome_aluno = st.text_input("Nome do Aluno (obrigatório)", value=nome_preenchido)
        
        with st.expander("DADOS DO ESTUDANTE", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                principal_responsavel = st.text_input("Principal responsável:", value=dados_cadastro.get("principal_responsavel", ""))
                nome_escola = st.text_input("Nome da escola:", value=dados_cadastro.get("nome_escola", ""))
            with col2:
                parentesco_responsavel = st.text_input("Grau de parentesco do responsável:", value=dados_cadastro.get("parentesco_responsavel", ""))
                ano_escolar = st.text_input("Ano escolar:", value=dados_cadastro.get("ano_escolar", ""))

        # ... (outros expanders como DESENVOLVIMENTO, ESCOLA, AUTONOMIA)
        
        # --- SEÇÃO AVALIAÇÃO E POTENCIALIDADES ---
        with st.expander("AVALIAÇÃO E POTENCIALIDADES"):
            col1, col2 = st.columns(2)
            with col1:
                dificuldades = st.text_area("Principais Dificuldades (restrições):", value=dados_cadastro.get("dificuldades", ""))
            with col2:
                potencialidades = st.text_area("Principais Potencialidades (o que gosta):", value=dados_cadastro.get("potencialidades", ""))

            radio_opts = ["Sim", "Não"]
            aval_multi = st.radio("Possui avaliação da equipe multi?", radio_opts, horizontal=True, index=radio_opts.index(dados_cadastro.get("aval_multi", "Não")))
            desenv_habil = st.radio("Precisa desenvolver habilidades básicas?", radio_opts, horizontal=True, index=radio_opts.index(dados_cadastro.get("desenv_habil", "Não")))
            adapt_materiais = st.radio("Possui necessidade de adaptação de materiais?", radio_opts, horizontal=True, index=radio_opts.index(dados_cadastro.get("adapt_materiais", "Não")))
            adapt_curriculo = st.radio("Possui necessidade de adaptação de currículo?", radio_opts, horizontal=True, index=radio_opts.index(dados_cadastro.get("adapt_curriculo", "Não")))
            
            disciplinas_apoio = st.text_area("Disciplinas que necessita de maior apoio:", value=dados_cadastro.get("disciplinas_apoio", ""))

            anexos = st.file_uploader("Anexar Documentos e Avaliações", accept_multiple_files=True, type=['pdf', 'docx', 'jpg', 'png'])

        submitted = st.form_submit_button("Salvar Dados Cadastrais")
        if submitted:
            if not nome_aluno:
                st.error("O nome do aluno é obrigatório!")
            else:
                novos_dados_cadastro = {
                    "principal_responsavel": principal_responsavel,
                    "nome_escola": nome_escola,
                    "parentesco_responsavel": parentesco_responsavel,
                    "ano_escolar": ano_escolar,
                    "dificuldades": dificuldades,
                    "potencialidades": potencialidades,
                    "aval_multi": aval_multi,
                    "desenv_habil": desenv_habil,
                    "adapt_materiais": adapt_materiais,
                    "adapt_curriculo": adapt_curriculo,
                    "disciplinas_apoio": disciplinas_apoio,
                }
                salvar_dados_aprendiz(nome_aluno, novos_dados_cadastro, "cadastro")
                st.success(f"Dados cadastrais de '{nome_aluno}' salvos com sucesso!")
                st.balloons()

# O restante do código para as outras páginas permanece o mesmo
elif pagina_selecionada == "Avaliação de Habilidades":
    st.header("📝 Avaliação de Habilidades")
    
    if not st.session_state.nome_aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para preencher a avaliação.")
    else:
        # ... (código da página de avaliação)
        pass

elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    if not st.session_state.nome_aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    else:
        # ... (código da página de PEI)
        pass

elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas")
    if not st.session_state.nome_aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para gerar atividades.")
    else:
        # ... (código do gerador de atividades)
        pass
