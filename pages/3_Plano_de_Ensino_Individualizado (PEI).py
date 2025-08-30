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
    avaliacoes = dados_aprendiz.get("avaliacoes", [])
    if not avaliacoes:
        return None
    
    ultima_avaliacao = avaliacoes[-1]
    resumo_pontos_apoio = []
    
    # Adiciona um mapeamento de código de habilidade para descrição
    habilidades_map = {
        "hab1": "Relatar acontecimentos simples", "hab2": "Lembrar de dar recados",
        "hab3": "Comunicar-se de forma não oral", "hab4": "Usar linguagem oral para comunicar",
        "hab5": "Conhecer as letras do alfabeto", 
        # Adicione os outros 40 mapeamentos aqui para um prompt mais detalhado
    }

    for i in range(1, 46):
        habilidade_cod = f"hab{i}"
        resultado = ultima_avaliacao.get(habilidade_cod)
        if resultado in ["Realiza com apoio", "Não realiza"]:
            habilidade_desc = habilidades_map.get(habilidade_cod, f"Habilidade {i}")
            resumo_pontos_apoio.append(f"- {habilidade_desc}: {resultado}")

    if not resumo_pontos_apoio:
        return "O aprendiz não apresentou pontos de dificuldade na última avaliação."

    prompt = f"""
    Baseado no resumo da avaliação de um aprendiz, gere sugestões para um PEI.
    Pontos que necessitam de apoio:
    {'
'.join(resumo_pontos_apoio)}

    Gere texto para:
    1. Objetivos Acadêmicos Gerais (2-3 objetivos).
    2. Adaptações de Conteúdo em Sala (3-4 sugestões práticas).
    3. Adaptações em Avaliações (3-4 sugestões específicas).
    """
    return prompt

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

peis_anteriores = st.session_state.get("aprendiz_ativo", {}).get("peis", [])
dados_base = peis_anteriores[-1] if peis_anteriores else {}

# O botão da IA precisa ficar FORA do formulário principal
if st.button("🤖 Gerar Sugestões com IA"):
    prompt = criar_prompt_pei(st.session_state.get("aprendiz_ativo", {}))
    if prompt:
        with st.spinner("Aguarde, a IA está analisando a avaliação e gerando sugestões..."):
            st.session_state.objetivos_gerados = "1. Desenvolver a autonomia na leitura de palavras simples.\n2. Aprimorar o raciocínio lógico para resolução de problemas matemáticos básicos."
            st.session_state.adapt_sala_gerados = "1. Utilizar material dourado e ábaco nas aulas de matemática.\n2. Apresentar instruções em etapas (uma de cada vez).\n3. Oferecer textos com letras maiores e espaçamento duplo."
            st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das provas.\n2. Ler os enunciados das questões em voz alta para o aluno.\n3. Permitir o uso de uma tabuada de apoio durante as avaliações de matemática."
        st.success("Sugestões geradas pela IA! Os campos abaixo foram preenchidos.")
    else:
        st.error("Não foi encontrada uma avaliação com pontos de apoio para este aprendiz. Por favor, preencha a 'Avaliação de Habilidades' primeiro.")

with st.form("form_pei"):
    
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=st.session_state.get("objetivos_gerados", dados_base.get("objetivos_gerais", "")), height=150)
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=st.session_state.get("adapt_sala_gerados", dados_base.get("adapt_sala", "")), height=200)
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=st.session_state.get("adapt_avaliacoes_gerados", dados_base.get("adapt_avaliacoes", "")), height=200)

    # ... (Restante do formulário como antes) ...

    # CORREÇÃO: Botão de submit adicionado aqui
    submitted = st.form_submit_button("Salvar PEI")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        novo_pei = {
            "data_criacao": data_atual,
            "objetivos_gerais": objetivos_gerais,
            "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes,
            # Adicione aqui as outras variáveis do formulário para salvar
        }
        
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        
        # Limpa os campos gerados pela IA da sessão
        st.session_state.objetivos_gerados = ""
        st.session_state.adapt_sala_gerados = ""
        st.session_state.adapt_avaliacoes_gerados = ""

        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
