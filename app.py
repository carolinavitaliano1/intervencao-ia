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

def salvar_dados_aprendiz(nome_aprendiz, novos_dados, secao):
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    
    aprendizes[nome_aprendiz][secao] = novos_dados
    
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True

# --- INICIALIZAÇÃO DO ESTADO DA SESSÃO ---
if 'aprendiz_ativo' not in st.session_state:
    st.session_state.aprendiz_ativo = None

# --- MENU LATERAL DE NAVEGAÇÃO ---
with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA")
    
    aprendizes_cadastrados = carregar_dados()
    lista_nomes = ["-- Novo Cadastro --"] + list(aprendizes_cadastrados.keys())
    
    aprendiz_selecionado = st.selectbox(
        "Selecione o Aprendiz:",
        options=lista_nomes,
        index=0
    )

    if aprendiz_selecionado != "-- Novo Cadastro --":
        st.session_state.aprendiz_ativo = aprendizes_cadastrados[aprendiz_selecionado]
        st.session_state.nome_aprendiz_ativo = aprendiz_selecionado
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

# PÁGINA DE CADASTRO
if pagina_selecionada == "Cadastro de Aprendiz":
    st.header("👤 Cadastro de Aprendiz")
    
    dados_cadastro = {}
    if st.session_state.aprendiz_ativo:
        st.info(f"Visualizando/editando dados de: **{st.session_state.nome_aprendiz_ativo}**")
        dados_cadastro = st.session_state.aprendiz_ativo.get("cadastro", {})

    with st.form("form_cadastro"):
        nome_aluno = st.text_input("Nome do Aluno (obrigatório)", value=st.session_state.nome_aprendiz_ativo or "")
        # ... (Todos os outros campos do formulário de cadastro, preenchidos com `dados_cadastro.get(...)`)
        # Exemplo:
        principal_responsavel = st.text_input("Principal responsável:", value=dados_cadastro.get("principal_responsavel", ""))
        
        submitted = st.form_submit_button("Salvar Dados Cadastrais")
        if submitted:
            if not nome_aluno:
                st.error("O nome do aluno é obrigatório!")
            else:
                novos_dados_cadastro = {
                    "principal_responsavel": principal_responsavel,
                    # ... (coletar todos os outros campos)
                }
                salvar_dados_aprendiz(nome_aluno, novos_dados_cadastro, "cadastro")
                st.success(f"Dados cadastrais de '{nome_aluno}' salvos com sucesso!")
                st.balloons()


# PÁGINA DE AVALIAÇÃO DE HABILIDADES
elif pagina_selecionada == "Avaliação de Habilidades":
    st.header("📝 Avaliação de Habilidades")
    
    if not st.session_state.aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para preencher a avaliação.")
    else:
        st.info(f"Preenchendo avaliação para: **{st.session_state.nome_aprendiz_ativo}**")
        dados_avaliacao = st.session_state.aprendiz_ativo.get("avaliacao", {})
        
        with st.form("form_avaliacao"):
            opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]
            
            st.subheader("Comunicação Oral")
            hab1 = st.radio("1. Relata acontecimentos simples...", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab1", opcoes[0])))
            # ... (Todos os outros `st.radio` da avaliação, preenchidos com `dados_avaliacao.get(...)`)

            submitted = st.form_submit_button("Salvar Avaliação de Habilidades")
            if submitted:
                novos_dados_avaliacao = {
                    "hab1": hab1,
                    # ... (coletar os resultados de todas as 45 habilidades)
                }
                salvar_dados_aprendiz(st.session_state.nome_aprendiz_ativo, novos_dados_avaliacao, "avaliacao")
                st.success(f"Avaliação de '{st.session_state.nome_aprendiz_ativo}' salva com sucesso!")

# PÁGINA DO PEI
elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")

    if not st.session_state.aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    else:
        st.info(f"Criando PEI para: **{st.session_state.nome_aprendiz_ativo}**")
        dados_pei = st.session_state.aprendiz_ativo.get("pei", {})
        
        # Exibir PEI salvo, se houver
        if dados_pei:
            with st.expander("Ver PEI Salvo"):
                st.write("Habilidades da BNCC selecionadas:", dados_pei.get("habilidades_bncc", []))
                st.write("Metas e Estratégias:", dados_pei.get("metas_estrategias", ""))
        
        st.subheader("Criar ou Editar PEI")
        # Ferramentas de busca da BNCC (seu código anterior)
        # ...
        
        habilidades_selecionadas = st.multiselect("Selecione as habilidades da BNCC para este PEI", options=["EM13LGG101", "EM13LGG102", "..."]) # Popular com os resultados da busca
        metas_estrategias = st.text_area("Descreva as Metas, Estratégias e Adaptações", height=300)

        if st.button("Salvar PEI"):
            novos_dados_pei = {
                "habilidades_bncc": habilidades_selecionadas,
                "metas_estrategias": metas_estrategias
            }
            salvar_dados_aprendiz(st.session_state.nome_aprendiz_ativo, novos_dados_pei, "pei")
            st.success(f"PEI de '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")

# PÁGINA GERADOR DE ATIVIDADES (ainda não conectada)
elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas")
    if not st.session_state.aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para gerar atividades.")
    else:
        st.info(f"Gerando atividades para: **{st.session_state.nome_aprendiz_ativo}**")
        # ... (Lógica do gerador)
