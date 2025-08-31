import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_fundamental import FUNDAMENTAL_DB

# --- FUNÇÕES AUXILIARES ---
def buscar_habilidade_bncc(codigo):
    codigo = codigo.upper().strip()
    for ano, componentes in FUNDAMENTAL_DB.items():
        for componente, habilidades in componentes.items():
            for habilidade in habilidades:
                if habilidade["codigo"] == codigo:
                    return habilidade
    return None

# --- INICIALIZAÇÃO E LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

# Inicializa a lista de habilidades para o PEI atual na sessão
if 'pei_habilidades_atuais' not in st.session_state:
    st.session_state.pei_habilidades_atuais = []

# --- ÁREA DE BUSCA E ADIÇÃO DE HABILIDADES (FORA DO FORMULÁRIO PRINCIPAL) ---
st.subheader("ETAPA 1: Selecionar Habilidades (BNCC)")
col1, col2 = st.columns([3, 1])
with col1:
    codigo_input = st.text_input("Digite o código da habilidade (Ex: EF01LP05)", key="codigo_input")
with col2:
    st.write("‎") # Espaçamento
    if st.button("Adicionar Habilidade"):
        if codigo_input:
            habilidade_encontrada = buscar_habilidade_bncc(codigo_input)
            if habilidade_encontrada:
                # Verifica se a habilidade já foi adicionada
                if any(h['codigo'] == habilidade_encontrada['codigo'] for h in st.session_state.pei_habilidades_atuais):
                    st.warning(f"A habilidade {habilidade_encontrada['codigo']} já foi adicionada.")
                else:
                    st.session_state.pei_habilidades_atuais.append({
                        "codigo": habilidade_encontrada['codigo'],
                        "descricao": habilidade_encontrada['descricao'],
                        "estrategia": "",
                        "data_inicio": "",
                        "desempenho": ""
                    })
                    st.success(f"Habilidade {habilidade_encontrada['codigo']} adicionada ao plano!")
            else:
                st.error(f"Código '{codigo_input}' não encontrado.")
            # Limpa o campo de input
            st.session_state.codigo_input = ""


# --- FORMULÁRIO PRINCIPAL PARA SALVAR O PEI ---
with st.form("form_pei"):
    st.subheader("ETAPA 2: Detalhar o Plano")
    
    # Renderiza as habilidades que foram adicionadas à sessão
    if not st.session_state.pei_habilidades_atuais:
        st.info("Nenhuma habilidade adicionada ao plano ainda. Use o campo acima para começar.")
    else:
        st.write("Preencha os detalhes para cada habilidade selecionada:")
        for i, habilidade in enumerate(st.session_state.pei_habilidades_atuais):
            with st.container(border=True):
                st.success(f"**{habilidade['codigo']}**: {habilidade['descricao']}")
                
                # Cria campos de input para cada detalhe da habilidade
                habilidade['estrategia'] = st.text_area("Estratégia", key=f"estrategia_{i}", height=100)
                col_data, col_desempenho = st.columns(2)
                with col_data:
                    habilidade['data_inicio'] = st.text_input("Data de Início e Duração", key=f"data_{i}")
                with col_desempenho:
                    habilidade['desempenho'] = st.selectbox("Desempenho", options=["Não iniciado", "Em andamento", "Alcançado com apoio", "Alcançado com autonomia"], key=f"desempenho_{i}")

    st.markdown("---")
    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        observacoes = st.text_area("Observações Gerais", height=200)
        redigido_por = st.text_input("Este documento foi redigido por")

    submitted = st.form_submit_button("Salvar PEI Completo")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        novo_pei = {
            "data_criacao": data_atual,
            "habilidades_plano": st.session_state.pei_habilidades_atuais,
            "observacoes": observacoes,
            "redigido_por": redigido_por,
        }
        
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        
        # Limpa a lista de habilidades da sessão para o próximo PEI
        st.session_state.pei_habilidades_atuais = []
        
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
