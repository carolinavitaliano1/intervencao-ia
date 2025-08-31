import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_infantil import INFANTIL_DB
from bncc_fundamental import FUNDAMENTAL_DB
from bncc_medio import MEDIO_DB

# --- Dicionário unificado da BNCC ---
BNCC_DATABASE = {
    "Educação Infantil": INFANTIL_DB,
    "Ensino Fundamental": FUNDAMENTAL_DB,
    "Ensino Médio": MEDIO_DB
}

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

# Inicializa a lista de habilidades para o PEI atual na sessão
if 'pei_habilidades_atuais' not in st.session_state:
    st.session_state.pei_habilidades_atuais = []

with st.form("form_pei"):
    
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        # ... (código da Etapa 1 como antes) ...
        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", height=150)
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", height=200)
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", height=200)

    with st.expander("ETAPA 2: OBJETIVOS POR DISCIPLINA (BNCC)", expanded=True):
        st.write("Navegue e selecione as habilidades da BNCC para incluir no plano.")
        
        etapa_ensino = st.selectbox("1. Selecione a Etapa de Ensino:", list(BNCC_DATABASE.keys()))
        
        lista_de_habilidades = []
        
        # Lógica para Educação Infantil
        if etapa_ensino == "Educação Infantil":
            grupos_etarios = list(BNCC_DATABASE[etapa_ensino].keys())
            grupo_selecionado = st.selectbox("2. Selecione o Grupo Etário:", grupos_etarios)
            campos_exp = list(BNCC_DATABASE[etapa_ensino][grupo_selecionado].keys())
            campo_selecionado = st.selectbox("3. Selecione o Campo de Experiência:", campos_exp)
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][grupo_selecionado][campo_selecionado]

        # Lógica para Ensino Fundamental
        elif etapa_ensino == "Ensino Fundamental":
            anos_disponiveis = list(BNCC_DATABASE[etapa_ensino].keys())
            ano_selecionado = st.selectbox("2. Selecione o Ano Escolar:", anos_disponiveis)
            componentes_disponiveis = list(BNCC_DATABASE[etapa_ensino][ano_selecionado].keys())
            componente_selecionado = st.selectbox("3. Selecione o Componente Curricular (Matéria):", componentes_disponiveis)
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][ano_selecionado][componente_selecionado]

        # Lógica para Ensino Médio
        elif etapa_ensino == "Ensino Médio":
            areas_conhecimento = list(BNCC_DATABASE[etapa_ensino].keys())
            area_selecionada = st.selectbox("2. Selecione a Área de Conhecimento:", areas_conhecimento)
            lista_de_habilidades = BNCC_DATABASE[etapa_ensino][area_selecionada].get("Habilidades", [])

        # Prepara as opções para o multiselect e um dicionário de busca
        opcoes_formatadas = [f"({h['codigo']}) {h['descricao']}" for h in lista_de_habilidades]
        habilidades_lookup = {f"({h['codigo']}) {h['descricao']}": h for h in lista_de_habilidades}
        
        habilidades_marcadas_formatadas = st.multiselect(
            "4. Marque as habilidades que deseja trabalhar:",
            options=opcoes_formatadas
        )
        
        st.markdown("---")
        st.write("Preencha os detalhes para cada habilidade selecionada abaixo:")

        habilidades_detalhadas = []
        if habilidades_marcadas_formatadas:
            for selecao in habilidades_marcadas_formatadas:
                habilidade_obj = habilidades_lookup[selecao]
                with st.container(border=True):
                    st.success(f"**{habilidade_obj['codigo']}**: {habilidade_obj['descricao']}")
                    estrategia = st.text_area("Estratégia", key=f"estrategia_{habilidade_obj['codigo']}", height=100)
                    col_data, col_desempenho = st.columns(2)
                    with col_data:
                        data_inicio = st.text_input("Data de Início e Duração", key=f"data_{habilidade_obj['codigo']}")
                    with col_desempenho:
                        desempenho = st.selectbox("Desempenho", options=["Não iniciado", "Em andamento", "Alcançado com apoio", "Alcançado com autonomia"], key=f"desempenho_{habilidade_obj['codigo']}")
                    habilidades_detalhadas.append({
                        "codigo": habilidade_obj['codigo'], "descricao": habilidade_obj['descricao'],
                        "estrategia": estrategia, "data_inicio": data_inicio, "desempenho": desempenho
                    })

    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        # ... (código da Etapa 3 como antes) ...
        observacoes = st.text_area("Observações Gerais", height=200)
        ajustes_proximo_pei = st.text_area("Ajustes para o Próximo PEI", height=200)

    submitted = st.form_submit_button("Salvar PEI Completo")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        novo_pei = {
            "data_criacao": data_atual,
            "objetivos_gerais": objetivos_gerais,
            "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes,
            "habilidades_plano": habilidades_detalhadas,
            "observacoes": observacoes,
            "ajustes_proximo_pei": ajustes_proximo_pei,
        }
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
