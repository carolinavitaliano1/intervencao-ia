import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_fundamental import FUNDAMENTAL_DB

# --- FUNÇÃO PARA BUSCAR HABILIDADES NA BNCC ---
def buscar_habilidade_por_descricao(descricao_selecionada, ano, componente):
    if ano in FUNDAMENTAL_DB and componente in FUNDAMENTAL_DB[ano]:
        for habilidade in FUNDAMENTAL_DB[ano][componente]:
            if habilidade["descricao"] == descricao_selecionada:
                return habilidade
    return None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

# Inicializa o estado da sessão para os campos do formulário
if 'pei_objetivos_gerais' not in st.session_state: st.session_state.pei_objetivos_gerais = ""
if 'pei_adapt_sala' not in st.session_state: st.session_state.pei_adapt_sala = ""
if 'pei_adapt_avaliacoes' not in st.session_state: st.session_state.pei_adapt_avaliacoes = ""
if 'pei_habilidades_selecionadas' not in st.session_state: st.session_state.pei_habilidades_selecionadas = []

with st.form("form_pei"):
    
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", height=150)
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", height=200)
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", height=200)

    with st.expander("ETAPA 2: OBJETIVOS POR DISCIPLINA (BNCC)", expanded=True):
        st.write("Navegue e selecione as habilidades da BNCC para incluir no plano.")
        
        # Filtros de seleção
        anos_disponiveis = list(FUNDAMENTAL_DB.keys())
        ano_selecionado = st.selectbox("1. Selecione o Ano Escolar:", anos_disponiveis)
        
        componentes_disponiveis = list(FUNDAMENTAL_DB[ano_selecionado].keys())
        componente_selecionado = st.selectbox("2. Selecione o Componente Curricular (Matéria):", componentes_disponiveis)
        
        # Gera a lista de habilidades para a seleção
        habilidades_disponiveis = [h["descricao"] for h in FUNDAMENTAL_DB[ano_selecionado][componente_selecionado]]
        
        habilidades_marcadas = st.multiselect(
            "3. Marque as habilidades que deseja trabalhar:",
            options=habilidades_disponiveis
        )
        
        st.markdown("---")
        st.write("Preencha os detalhes para cada habilidade selecionada abaixo:")

        habilidades_detalhadas = []
        if habilidades_marcadas:
            for desc in habilidades_marcadas:
                habilidade_obj = buscar_habilidade_por_descricao(desc, ano_selecionado, componente_selecionado)
                if habilidade_obj:
                    with st.container(border=True):
                        st.success(f"**{habilidade_obj['codigo']}**: {habilidade_obj['descricao']}")
                        
                        estrategia = st.text_area("Estratégia", key=f"estrategia_{habilidade_obj['codigo']}", height=100)
                        col_data, col_desempenho = st.columns(2)
                        with col_data:
                            data_inicio = st.text_input("Data de Início e Duração", key=f"data_{habilidade_obj['codigo']}")
                        with col_desempenho:
                            desempenho = st.selectbox("Desempenho", options=["Não iniciado", "Em andamento", "Alcançado com apoio", "Alcançado com autonomia"], key=f"desempenho_{habilidade_obj['codigo']}")
                        
                        habilidades_detalhadas.append({
                            "codigo": habilidade_obj['codigo'],
                            "descricao": habilidade_obj['descricao'],
                            "estrategia": estrategia,
                            "data_inicio": data_inicio,
                            "desempenho": desempenho
                        })

    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        observacoes = st.text_area("Observações Gerais", height=200)
        ajustes_proximo_pei = st.text_area("Ajustes para o Próximo PEI", height=200)
        st.markdown("---")
        redigido_por = st.text_input("Este documento foi redigido por")
        data_finalizacao = st.date_input("Data de Finalização")

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
            "redigido_por": redigido_por,
            "data_finalizacao": data_finalizacao.strftime('%d/%m/%Y'),
        }
        
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
