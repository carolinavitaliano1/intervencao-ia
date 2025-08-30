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
    
    # Se um aprendiz estiver ativo, encontre seu índice na lista
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
                data_pei_str = dados_cadastro.get("data_pei", datetime.date.today().strftime('%Y-%m-%d'))
                data_pei = st.date_input("Data da elaboração do PEI:", value=datetime.datetime.strptime(data_pei_str, '%Y-%m-%d').date())
                tipo_documento = st.text_input("Tipo de documento:", value=dados_cadastro.get("tipo_documento", ""))
            with col2:
                data_nasc_str = dados_cadastro.get("data_nascimento", "2010-01-01")
                data_nascimento = st.date_input("Data de Nascimento:", min_value=datetime.date(1990, 1, 1), value=datetime.datetime.strptime(data_nasc_str, '%Y-%m-%d').date())
                parentesco_responsavel = st.text_input("Grau de parentesco do responsável:", value=dados_cadastro.get("parentesco_responsavel", ""))
                ano_escolar = st.text_input("Ano escolar:", value=dados_cadastro.get("ano_escolar", "5º"))
                duracao_pei = st.text_input("Duração do PEI:", value=dados_cadastro.get("duracao_pei", ""))
                elaborado_por = st.text_input("Elaborado por:", value=dados_cadastro.get("elaborado_por", ""))

            avaliacao_habilidades = st.text_area("Avaliação das habilidades:", value=dados_cadastro.get("avaliacao_habilidades", ""))
            relatorio_multidisciplinar = st.text_area("Relatório da equipe multidisciplinar:", value=dados_cadastro.get("relatorio_multidisciplinar", ""))

        with st.expander("DESENVOLVIMENTO E SAÚDE"):
            col1, col2, col3 = st.columns(3)
            with col1:
                diagnostico = st.text_input("Diagnóstico:", value=dados_cadastro.get("diagnostico", ""))
            with col2:
                comorbidades = st.text_input("Comorbidades:", value=dados_cadastro.get("comorbidades", ""))
            with col3:
                data_diag_str = dados_cadastro.get("data_diagnostico", datetime.date.today().strftime('%Y-%m-%d'))
                data_diagnostico = st.date_input("Data do diagnóstico:", value=datetime.datetime.strptime(data_diag_str, '%Y-%m-%d').date())
            terapias = st.text_area("Terapias:", value=dados_cadastro.get("terapias", ""))
            col1, col2 = st.columns(2)
            with col1:
                medico_responsavel = st.text_input("Médico responsável:", value=dados_cadastro.get("medico_responsavel", ""))
            with col2:
                contato_medico = st.text_input("Contato:", value=dados_cadastro.get("contato_medico", ""))
            col1, col2, col3 = st.columns(3)
            with col1:
                medicacao_atual = st.text_input("Medicação atual:", value=dados_cadastro.get("medicacao_atual", ""))
            with col2:
                horario_medicacao = st.text_input("Horário:", value=dados_cadastro.get("horario_medicacao", ""))
            with col3:
                objetivo_medicacao = st.text_input("Objetivo:", value=dados_cadastro.get("objetivo_medicacao", ""))
            alergia = st.text_area("Alergia:", value=dados_cadastro.get("alergia", ""))
            alteracao_sensorial = st.text_area("Alteração sensorial:", value=dados_cadastro.get("alteracao_sensorial", ""))
            gatilhos_crises = st.text_area("Gatilhos para crises:", value=dados_cadastro.get("gatilhos_crises", ""))
            outras_infos = st.text_area("Outras informações relevantes:", value=dados_cadastro.get("outras_infos", ""))

        with st.expander("AVALIAÇÃO E POTENCIALIDADES"):
            anexos = st.file_uploader("Anexar Documentos e Avaliações", accept_multiple_files=True, type=['pdf', 'docx', 'jpg', 'png'])

        submitted = st.form_submit_button("Salvar Dados Cadastrais")
        if submitted:
            if not nome_aluno:
                st.error("O nome do aluno é obrigatório!")
            else:
                novos_dados_cadastro = {
                    "principal_responsavel": principal_responsavel,
                    "nome_escola": nome_escola,
                    "data_pei": data_pei.strftime('%Y-%m-%d'),
                    "tipo_documento": tipo_documento,
                    "data_nascimento": data_nascimento.strftime('%Y-%m-%d'),
                    "parentesco_responsavel": parentesco_responsavel,
                    "diagnostico": diagnostico,
                    "comorbidades": comorbidades,
                    "data_diagnostico": data_diagnostico.strftime('%Y-%m-%d'),
                    # Adicione todas as outras variáveis aqui
                }
                salvar_dados_aprendiz(nome_aluno, novos_dados_cadastro, "cadastro")
                st.success(f"Dados cadastrais de '{nome_aluno}' salvos com sucesso!")
                st.balloons()


elif pagina_selecionada == "Avaliação de Habilidades":
    st.header("📝 Avaliação de Habilidades")
    
    if not st.session_state.nome_aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para preencher a avaliação.")
    else:
        st.info(f"Preenchendo avaliação para: **{st.session_state.nome_aprendiz_ativo}**")
        dados_avaliacao = st.session_state.aprendiz_ativo.get("avaliacao", {})
        
        with st.form("form_avaliacao"):
            opcoes = ["Realiza sem suporte", "Realiza com apoio", "Não realiza", "Não foi observado"]
            
            st.subheader("Comunicação Oral")
            hab1 = st.radio("1. Relata acontecimentos...", opcoes, horizontal=True, index=opcoes.index(dados_avaliacao.get("hab1", "Não foi observado")))
            # ... Adicione todos os 45 `st.radio` aqui, como no exemplo acima ...
            
            st.subheader("ACADÊMICO")
            portugues_acad = st.text_area("Português:", value=dados_avaliacao.get("portugues_acad", ""))
            # ... Adicione as outras áreas acadêmicas ...

            submitted = st.form_submit_button("Salvar Avaliação de Habilidades")
            if submitted:
                novos_dados_avaliacao = {
                    "hab1": hab1,
                    # ... coletar todos os 45 `habX` ...
                    "portugues_acad": portugues_acad,
                    # ... coletar todas as áreas ...
                }
                salvar_dados_aprendiz(st.session_state.nome_aprendiz_ativo, novos_dados_avaliacao, "avaliacao")
                st.success(f"Avaliação de '{st.session_state.nome_aprendiz_ativo}' salva com sucesso!")

elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")

    if not st.session_state.nome_aprendiz_ativo:
        st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    else:
        st.info(f"Criando PEI para: **{st.session_state.nome_aprendiz_ativo}**")
        dados_pei = st.session_state.aprendiz_ativo.get("pei", {})

        if dados_pei:
            with st.expander("Ver PEI Salvo Anteriormente"):
                st.write("**Habilidades da BNCC selecionadas:**", dados_pei.get("habilidades_bncc", []))
                st.write("**Metas e Estratégias:**", dados_pei.get("metas_estrategias", ""))

        tab_busca, tab_estrategias = st.tabs(["Navegador da BNCC", "Banco de Estratégias Clínicas"])

        with tab_busca:
            # ... Coloque aqui toda a lógica de busca da BNCC que já tínhamos ...
            st.write("Aqui entra a busca da BNCC...")
        
        with st.form("form_pei"):
            st.subheader("Montar e Salvar o PEI")
            habilidades_selecionadas = st.multiselect(
                "Selecione as habilidades da BNCC para este PEI (busque na aba acima e digite os códigos aqui):",
                options=["EF15LP01", "EF01MA01", "EM13LGG101", "EM13MAT301"], # Exemplo
                default=dados_pei.get("habilidades_bncc", [])
            )
            metas_estrategias = st.text_area(
                "Descreva as Metas, Estratégias e Adaptações",
                height=300,
                value=dados_pei.get("metas_estrategias", "")
            )
            
            submitted = st.form_submit_button("Salvar PEI")
            if submitted:
                novos_dados_pei = {
                    "habilidades_bncc": habilidades_selecionadas,
                    "metas_estrategias": metas_estrategias,
                }
                salvar_dados_aprendiz(st.session_state.nome_aprendiz_ativo, novos_dados_pei, "pei")
                st.success(f"PEI de '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")

# ... O restante do código para as outras páginas ...
