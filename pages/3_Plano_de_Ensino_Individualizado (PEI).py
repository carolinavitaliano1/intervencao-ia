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

# --- FUNÇÃO PARA GERAR O PROMPT PARA A IA ---
def criar_prompt_pei(dados_aprendiz):
    # Pega a avaliação mais recente
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    if not avaliacoes:
        return None
    
    ultima_avaliacao = avaliacoes[-1]
    
    # Monta um resumo dos pontos fracos para a IA focar
    resumo_pontos_apoio = []
    for i in range(1, 46):
        habilidade = f"hab{i}"
        resultado = ultima_avaliacao.get(habilidade)
        if resultado in ["Realiza com apoio", "Não realiza"]:
            # (Aqui poderíamos ter um dicionário para mapear hab1 -> "Descrição da habilidade 1")
            resumo_pontos_apoio.append(f"- Habilidade {habilidade}: {resultado}")

    # Adiciona observações acadêmicas se houver
    for materia, obs in ultima_avaliacao.items():
        if "_acad" in materia and obs:
            resumo_pontos_apoio.append(f"- Observação em {materia.replace('_acad', '').capitalize()}: {obs}")

    if not resumo_pontos_apoio:
        return "O aprendiz não apresentou pontos de dificuldade na última avaliação."

    prompt = f"""
    Você é um especialista em psicopedagogia. Com base no seguinte resumo da avaliação de um aprendiz, gere sugestões para um Plano de Ensino Individualizado (PEI).

    **Principais pontos que necessitam de apoio:**
    {'
'.join(resumo_pontos_apoio)}

    **Sua Tarefa:**
    Gere um texto conciso e prático para os seguintes três campos. Use uma linguagem clara e direta.

    1.  **Objetivos Acadêmicos Gerais:** Descreva 2 a 3 objetivos gerais e abrangentes que focam nas principais áreas de dificuldade do aluno para o próximo semestre.
    2.  **Adaptações de Conteúdo em Sala:** Sugira 3 a 4 adaptações práticas e acionáveis que o professor pode usar em sala de aula (ex: uso de material concreto, instruções passo a passo, tempo para processamento, etc.).
    3.  **Adaptações em Avaliações:** Sugira 3 a 4 adaptações específicas para provas e avaliações (ex: enunciados lidos em voz alta, tempo extra, consulta a materiais de apoio, avaliações orais, etc.).
    """
    return prompt

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

with st.form("form_pei"):
    
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        
        # O novo botão para gerar sugestões com IA
        if st.button("🤖 Gerar Sugestões com IA"):
            prompt = criar_prompt_pei(st.session_state.get("aprendiz_ativo", {}))
            if prompt:
                # Simulação da chamada da IA (neste caso, o próprio Gemini gera a resposta)
                # Em um sistema real, aqui seria a chamada para a API da IA
                with st.spinner("Aguarde, a IA está analisando a avaliação e gerando sugestões..."):
                    # Aqui você pode colocar a lógica para chamar a API da IA.
                    # Por enquanto, vamos usar um texto de exemplo:
                    st.session_state.objetivos_gerados = "1. Desenvolver a autonomia na leitura de palavras simples.\n2. Aprimorar o raciocínio lógico para resolução de problemas matemáticos básicos."
                    st.session_state.adapt_sala_gerados = "1. Utilizar material dourado e ábaco nas aulas de matemática.\n2. Apresentar instruções em etapas (uma de cada vez).\n3. Oferecer textos com letras maiores e espaçamento duplo."
                    st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das provas.\n2. Ler os enunciados das questões em voz alta para o aluno.\n3. Permitir o uso de uma tabuada de apoio durante as avaliações de matemática."
                st.success("Sugestões geradas pela IA!")
            else:
                st.error("Não foi encontrada uma avaliação com pontos de apoio para este aprendiz. Por favor, preencha a 'Avaliação de Habilidades' primeiro.")

        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=st.session_state.get("objetivos_gerados", ""), height=150)
        
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=st.session_state.get("adapt_sala_gerados", ""), height=200)
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=st.session_state.get("adapt_avaliacoes_gerados", ""), height=200)

    # ... (Restante do formulário do PEI)

    submitted = st.form_submit_button("Salvar PEI")
    if submitted:
        # Lógica para salvar os dados...
        st.success("PEI Salvo com sucesso!")
