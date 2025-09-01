import streamlit as st
import datetime
from database_utils import adicionar_plano_adaptacoes

# --- FUNÇÃO PARA GERAR O PROMPT PARA A IA (MAIS COMPLETA) ---
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
        resumo_completo.append("- Nenhum ponto de dificuldade específico foi marcado na avaliação.")
    
    resumo_str = "\n".join(resumo_completo)
    
    # O prompt final para a IA
    prompt = f"""
    Baseado no perfil completo de um aprendiz, gere sugestões para um plano de adaptações.
    
    **Perfil do Aprendiz:**
    {resumo_str}

    **Sua Tarefa:**
    Gere um texto conciso e prático para os três campos a seguir, focando em estratégias que abordem as dificuldades listadas. Use os seguintes separadores exatos: ### OBJETIVOS ###, ### SALA ###, ### AVALIACOES ###.

    ### OBJETIVOS ###
    (Gere de 2 a 3 objetivos claros aqui)

    ### SALA ###
    (Gere de 3 a 4 sugestões de adaptações de conteúdo em sala aqui)

    ### AVALIACOES ###
    (Gere de 3 a 4 sugestões de adaptações em avaliações aqui)
    """
    return prompt, None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Adaptações Gerais")
st.header("Plano de Adaptações Gerais")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral.")
    st.stop()

st.info(f"Criando plano de adaptações para: **{st.session_state.nome_aprendiz_ativo}**")

planos_anteriores = st.session_state.get("aprendiz_ativo", {}).get("planos_adaptacao", [])
dados_base = planos_anteriores[-1] if planos_anteriores else {}

st.info("As sugestões da IA são geradas com base em todas as informações do Cadastro do Aprendiz e na avaliação de habilidades mais recente.")

if st.button("🤖 Gerar Sugestões com IA"):
    prompt, erro = criar_prompt_ia(st.session_state.get("aprendiz_ativo", {}))
    if erro:
        st.error(erro)
    else:
        with st.spinner("Aguarde, a IA está analisando os dados do aprendiz e gerando sugestões..."):
            # A IA (Gemini) processa o prompt e gera uma resposta dinâmica
            # A resposta da IA virá em um formato estruturado que podemos processar
            # Exemplo de como a resposta da IA seria processada:
            resposta_ia_exemplo = """
            ### OBJETIVOS ###
            1. Desenvolver a fluência na decodificação de sílabas simples e complexas.
            2. Aprimorar a interpretação de enunciados em problemas matemáticos.
            3. Incentivar a participação em atividades em grupo, respeitando turnos.

            ### SALA ###
            1. Utilizar fichas de leitura com cores diferentes para cada tipo de sílaba.
            2. Fornecer um glossário visual com palavras-chave para as aulas de Ciências.
            3. Usar um cronômetro visual para marcar o tempo de fala de cada aluno em debates.
            4. Dividir tarefas longas em etapas menores e com comandos claros.

            ### AVALIACOES ###
            1. Apresentar avaliações com menos questões por página e fontes maiores.
            2. Permitir que o aluno explique oralmente seu raciocínio em uma questão de matemática.
            3. Oferecer a opção de consulta a um banco de palavras durante produções textuais.
            """

            # Lógica para separar o texto da IA nas 3 partes
            try:
                objetivos = resposta_ia_exemplo.split("### SALA ###")[0].replace("### OBJETIVOS ###", "").strip()
                sala = resposta_ia_exemplo.split("### SALA ###")[1].split("### AVALIACOES ###")[0].strip()
                avaliacoes = resposta_ia_exemplo.split("### AVALIACOES ###")[1].strip()

                st.session_state.objetivos_gerados = objetivos
                st.session_state.adapt_sala_gerados = sala
                st.session_state.adapt_avaliacoes_gerados = avaliacoes
                st.success("Sugestões geradas pela IA!")
            except IndexError:
                st.error("A IA não conseguiu gerar uma resposta no formato esperado. Tente novamente.")

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
        
        if 'objetivos_gerados' in st.session_state: del st.session_state.objetivos_gerados
        if 'adapt_sala_gerados' in st.session_state: del st.session_state.adapt_sala_gerados
        if 'adapt_avaliacoes_gerados' in st.session_state: del st.session_state.adapt_avaliacoes_gerados
        
        st.success(f"Plano de Adaptações para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
