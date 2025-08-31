import streamlit as st
import datetime
from database_utils import adicionar_novo_pei

# --- FUNÇÃO PARA GERAR O PROMPT PARA A IA ---
def criar_prompt_pei(dados_aprendiz):
    dados_cadastro = dados_aprendiz.get("cadastro", {})
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    if not avaliacoes:
        return None, "Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro."
    
    ultima_avaliacao = avaliacoes[-1]
    resumo_completo = ["**Informações do Prontuário do Aprendiz:**"]
    if dados_cadastro.get("diagnostico"): resumo_completo.append(f"- Diagnóstico: {dados_cadastro['diagnostico']}")
    if dados_cadastro.get("dificuldades"): resumo_completo.append(f"- Principais Dificuldades (relatadas): {dados_cadastro['dificuldades']}")
    
    resumo_completo.append("\n**Pontos de Apoio da Avaliação de Habilidades:**")
    pontos_encontrados = False
    for i in range(1, 46):
        habilidade_cod = f"hab{i}"
        resultado = ultima_avaliacao.get(habilidade_cod)
        if resultado in ["Realiza com apoio", "Não realiza"]:
            pontos_encontrados = True
            resumo_completo.append(f"- Habilidade {habilidade_cod}: {resultado}")

    if not pontos_encontrados:
        resumo_completo.append("- Nenhum ponto de dificuldade específico marcado na avaliação.")
    
    resumo_str = "\n".join(resumo_completo)
    return f"Baseado no perfil de um aprendiz:\n{resumo_str}\nGere sugestões para: 1. Objetivos Acadêmicos Gerais. 2. Adaptações de Conteúdo. 3. Adaptações em Avaliações.", None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Adaptações Gerais")
st.header("ETAPA 1: Adaptações Gerais")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral.")
    st.stop()

st.info(f"Criando plano de adaptações para: **{st.session_state.nome_aprendiz_ativo}**")

peis_anteriores = st.session_state.get("aprendiz_ativo", {}).get("peis", [])
dados_base = peis_anteriores[-1] if peis_anteriores else {}

st.info("As sugestões da IA são geradas com base nas informações do Cadastro e na Avaliação de Habilidades mais recente.")
if st.button("🤖 Gerar Sugestões com IA"):
    prompt, erro = criar_prompt_pei(st.session_state.get("aprendiz_ativo", {}))
    if erro:
        st.error(erro)
    else:
        with st.spinner("Aguarde, a IA está analisando os dados e gerando sugestões..."):
            st.session_state.objetivos_gerados = "1. Desenvolver a autonomia na leitura de palavras simples.\n2. Aprimorar o raciocínio lógico para resolução de problemas matemáticos básicos."
            st.session_state.adapt_sala_gerados = "1. Utilizar material dourado e ábaco nas aulas de matemática.\n2. Apresentar instruções em etapas (uma de cada vez)."
            st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das provas.\n2. Ler os enunciados das questões em voz alta para o aluno."
        st.success("Sugestões geradas! Os campos abaixo foram preenchidos.")

with st.form("form_adaptacoes"):
    objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=st.session_state.get("objetivos_gerados", dados_base.get("objetivos_gerais", "")), height=150)
    st.subheader("Adaptações Gerais Acadêmicas")
    col1, col2 = st.columns(2)
    with col1:
        adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=st.session_state.get("adapt_sala_gerados", dados_base.get("adapt_sala", "")), height=200)
    with col2:
        adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=st.session_state.get("adapt_avaliacoes_gerados", dados_base.get("adapt_avaliacoes", "")), height=200)

    submitted = st.form_submit_button("Salvar Adaptações")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        novo_plano = {
            "data_criacao": data_atual,
            "objetivos_gerais": objetivos_gerais,
            "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes,
        }
        
        # A função adicionar_novo_pei ainda funciona, apenas salvará um dicionário mais simples
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_plano)
        
        if 'objetivos_gerados' in st.session_state: del st.session_state.objetivos_gerados
        if 'adapt_sala_gerados' in st.session_state: del st.session_state.adapt_sala_gerados
        if 'adapt_avaliacoes_gerados' in st.session_state: del st.session_state.adapt_avaliacoes_gerados
        
        st.success(f"Plano de Adaptações para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
