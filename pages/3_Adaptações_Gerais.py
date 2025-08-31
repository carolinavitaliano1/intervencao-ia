import streamlit as st
import datetime
from database_utils import adicionar_plano_adaptacoes

# --- FUNÇÃO PARA GERAR O PROMPT PARA A IA ---
def criar_prompt_ia(dados_aprendiz):
    """Cria um prompt detalhado para a IA com base no cadastro e na última avaliação."""
    dados_cadastro = dados_aprendiz.get("cadastro", {})
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    
    if not avaliacoes:
        return None, "Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro."
    
    ultima_avaliacao = avaliacoes[-1]
    
    # Monta um resumo completo
    resumo_completo = ["**Informações do Prontuário do Aprendiz:**"]
    if dados_cadastro.get("diagnostico"): resumo_completo.append(f"- Diagnóstico: {dados_cadastro['diagnostico']}")
    if dados_cadastro.get("dificuldades"): resumo_completo.append(f"- Principais Dificuldades (relatadas): {dados_cadastro['dificuldades']}")
    if dados_cadastro.get("potencialidades"): resumo_completo.append(f"- Principais Potencialidades (relatadas): {dados_cadastro['potencialidades']}")
    if dados_cadastro.get("comunicacao_alt"): resumo_completo.append(f"- Usa comunicação alternativa? {dados_cadastro['comunicacao_alt']}")
    
    resumo_completo.append("\n**Pontos de Apoio da Avaliação de Habilidades Recente:**")
    pontos_encontrados = False
    for i in range(1, 46):
        habilidade_cod = f"hab{i}"
        resultado = ultima_avaliacao.get(habilidade_cod)
        if resultado in ["Realiza com apoio", "Não realiza"]:
            pontos_encontrados = True
            resumo_completo.append(f"- Habilidade {habilidade_cod} (precisa de apoio): {resultado}")

    if not pontos_encontrados:
        resumo_completo.append("- Nenhum ponto de dificuldade específico foi marcado na avaliação de habilidades.")
    
    resumo_str = "\n".join(resumo_completo)
    
    # O prompt final para a IA
    prompt = f"""
    Baseado no perfil completo de um aprendiz, gere sugestões para um plano de adaptações.
    
    **Perfil do Aprendiz:**
    {resumo_str}

    **Sua Tarefa:**
    Gere um texto conciso e prático para os três campos a seguir, focando em estratégias que abordem as dificuldades listadas.
    1.  **Objetivos Acadêmicos Gerais:** (2 a 3 objetivos claros)
    2.  **Adaptações de Conteúdo em Sala:** (3 a 4 sugestões práticas)
    3.  **Adaptações em Avaliações:** (3 a 4 sugestões específicas)
    """
    return prompt, None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Adaptações Gerais")
st.header("Plano de Adaptações Gerais")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral.")
    st.stop()

st.info(f"Criando plano de adaptações para: **{st.session_state.nome_aprendiz_ativo}**")

# Carrega o plano mais recente para preencher o formulário como base, se houver
planos_anteriores = st.session_state.get("aprendiz_ativo", {}).get("planos_adaptacao", [])
dados_base = planos_anteriores[-1] if planos_anteriores else {}

# Aviso sobre a IA
st.info("As sugestões da IA são geradas com base em **todas as informações do Cadastro do Aprendiz** e na **avaliação de habilidades mais recente**.")

if st.button("🤖 Gerar Sugestões com IA"):
    prompt, erro = criar_prompt_ia(st.session_state.get("aprendiz_ativo", {}))
    if erro:
        st.error(erro)
    else:
        with st.spinner("Aguarde, a IA está analisando os dados do aprendiz e gerando sugestões..."):
            # Simulação da resposta da IA
            st.session_state.objetivos_gerados = "1. Desenvolver a autonomia na leitura de palavras simples e na escrita do próprio nome.\n2. Aprimorar o raciocínio lógico para resolução de problemas matemáticos de adição e subtração com suporte visual."
            st.session_state.adapt_sala_gerados = "1. Utilizar letras móveis e jogos silábicos para a construção de palavras.\n2. Oferecer material dourado ou ábaco para a resolução de operações matemáticas.\n3. Apresentar instruções de forma clara, em etapas curtas (uma de cada vez), com apoio visual."
            st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das provas.\n2. Ler os enunciados das questões em voz alta para o aluno.\n3. Permitir o uso de uma tabuada de apoio ou calculadora durante as avaliações de matemática."
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
        adicionar_plano_adaptacoes(st.session_state.nome_aprendiz_ativo, novo_plano)
        
        # Limpa os campos gerados pela IA da sessão para não persistirem
        if 'objetivos_gerados' in st.session_state: del st.session_state.objetivos_gerados
        if 'adapt_sala_gerados' in st.session_state: del st.session_state.adapt_sala_gerados
        if 'adapt_avaliacoes_gerados' in st.session_state: del st.session_state.adapt_avaliacoes_gerados
        
        st.success(f"Plano de Adaptações para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
