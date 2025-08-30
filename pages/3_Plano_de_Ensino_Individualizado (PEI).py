import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_fundamental import FUNDAMENTAL_DB

# --- FUNÇÃO PARA BUSCAR HABILIDADES NA BNCC ---
def buscar_habilidade_bncc(codigo):
    codigo = codigo.upper().strip()
    for ano, componentes in FUNDAMENTAL_DB.items():
        for componente, habilidades in componentes.items():
            for habilidade in habilidades:
                if habilidade["codigo"] == codigo:
                    return f'({habilidade["codigo"]}) {habilidade["descricao"]}'
    return None

# --- FUNÇÃO PARA GERAR O PROMPT PARA A IA (VERSÃO MAIS COMPLETA) ---
def criar_prompt_pei(dados_aprendiz):
    # Pega os dados do cadastro
    dados_cadastro = dados_aprendiz.get("cadastro", {})
    
    # Pega a avaliação mais recente
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    if not avaliacoes:
        return None, "Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro."
    
    ultima_avaliacao = avaliacoes[-1]
    
    # Monta um resumo dos dados do cadastro, incluindo Autonomia e Avaliação Geral
    resumo_cadastro = ["**Informações do Prontuário do Aprendiz:**"]
    if dados_cadastro.get("diagnostico"): resumo_cadastro.append(f"- Diagnóstico Principal: {dados_cadastro['diagnostico']}")
    if dados_cadastro.get("comorbidades"): resumo_cadastro.append(f"- Comorbidades: {dados_cadastro['comorbidades']}")
    # Seção Autonomia
    if dados_cadastro.get("comunicacao_alt"): resumo_cadastro.append(f"- Utiliza comunicação alternativa? {dados_cadastro['comunicacao_alt']}")
    if dados_cadastro.get("costuma_crises"): resumo_cadastro.append(f"- Costuma ter crises? {dados_cadastro['costuma_crises']}")
    # Seção Avaliação Geral
    if dados_cadastro.get("dificuldades"): resumo_cadastro.append(f"- Principais Dificuldades (relatadas): {dados_cadastro['dificuldades']}")
    if dados_cadastro.get("potencialidades"): resumo_cadastro.append(f"- Principais Potencialidades (relatadas): {dados_cadastro['potencialidades']}")
    if dados_cadastro.get("adapt_materiais"): resumo_cadastro.append(f"- Necessita de adaptação de materiais? {dados_cadastro['adapt_materiais']}")
    if dados_cadastro.get("adapt_curriculo"): resumo_cadastro.append(f"- Necessita de adaptação de currículo? {dados_cadastro['adapt_curriculo']}")
    
    # Monta um resumo dos pontos fracos da avaliação de habilidades
    resumo_pontos_apoio = ["\n**Resumo da Avaliação de Habilidades Recente (pontos que necessitam de apoio):**"]
    pontos_encontrados = False
    for i in range(1, 46):
        habilidade_cod = f"hab{i}"
        resultado = ultima_avaliacao.get(habilidade_cod)
        if resultado in ["Realiza com apoio", "Não realiza"]:
            pontos_encontrados = True
            resumo_pontos_apoio.append(f"- Habilidade '{habilidade_cod}': {resultado}")

    if not pontos_encontrados:
        resumo_pontos_apoio.append("- Nenhum ponto de dificuldade marcado na avaliação de habilidades.")

    # Junta os dois resumos
    resumo_cadastro_str = "\n".join(resumo_cadastro)
    resumo_avaliacao_str = "\n".join(resumo_pontos_apoio)

    prompt = f"""
    Você é um especialista em psicopedagogia. Com base nas seguintes informações de um aprendiz, gere sugestões para um Plano de Ensino Individualizado (PEI).

    {resumo_cadastro_str}

    {resumo_avaliacao_str}

    **Sua Tarefa:**
    Considerando TODAS as informações acima (diagnóstico, autonomia, dificuldades, potencialidades e avaliação de habilidades), gere um texto conciso e prático para os três campos a seguir.

    1.  **Objetivos Acadêmicos Gerais:**
    2.  **Adaptações de Conteúdo em Sala:**
    3.  **Adaptações em Avaliações:**
    """
    return prompt, None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

peis_anteriores = st.session_state.get("aprendiz_ativo", {}).get("peis", [])
dados_base = peis_anteriores[-1] if peis_anteriores else {}

st.info("As sugestões da IA são geradas com base nas informações do **Cadastro do Aprendiz** (incluindo Autonomia e Avaliação Geral) e na **avaliação de habilidades mais recente**.")

if st.button("🤖 Gerar Sugestões com IA"):
    prompt, erro = criar_prompt_pei(st.session_state.get("aprendiz_ativo", {}))
    if erro:
        st.error(erro)
    else:
        with st.spinner("Aguarde, a IA está analisando os dados e gerando sugestões..."):
            # Simulação da resposta da IA
            st.session_state.objetivos_gerados = "1. Desenvolver a autonomia na leitura de palavras simples e na escrita do próprio nome.\n2. Aprimorar o raciocínio lógico para resolução de problemas matemáticos de adição e subtração com suporte visual.\n3. Ampliar a participação e interação em atividades de grupo."
            st.session_state.adapt_sala_gerados = "1. Utilizar letras móveis e jogos silábicos para a construção de palavras.\n2. Oferecer material dourado ou ábaco para a resolução de operações matemáticas.\n3. Apresentar instruções de forma clara, em etapas curtas (uma de cada vez), com apoio visual.\n4. Criar um 'cantinho da calma' na sala para momentos de desregulação sensorial."
            st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das provas.\n2. Ler os enunciados das questões em voz alta para o aluno.\n3. Permitir o uso de uma tabuada de apoio ou calculadora durante as avaliações de matemática.\n4. Adaptar questões de múltipla escolha para respostas diretas ou com menor número de alternativas."
        st.success("Sugestões geradas pela IA! Os campos abaixo foram preenchidos.")

with st.form("form_pei"):
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=st.session_state.get("objetivos_gerados", dados_base.get("objetivos_gerais", "")), height=150)
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=st.session_state.get("adapt_sala_gerados", dados_base.get("adapt_sala", "")), height=200)
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=st.session_state.get("adapt_avaliacoes_gerados", dados_base.get("adapt_avaliacoes", "")), height=200)

    # ... (Restante do formulário como antes)
    
    submitted = st.form_submit_button("Salvar PEI")
    if submitted:
        # ... (Lógica de salvamento como antes)
        st.success("PEI salvo com sucesso!")
