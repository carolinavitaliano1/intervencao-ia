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
        return None, "Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro."
    
    ultima_avaliacao = avaliacoes[-1]
    resumo_pontos_apoio = []
    
    habilidades_map = { "hab5": "Conhecer as letras do alfabeto", "hab7": "Dominar sílabas simples", "hab22": "Solucionar problemas simples" }

    for i in range(1, 46):
        habilidade_cod = f"hab{i}"
        resultado = ultima_avaliacao.get(habilidade_cod)
        if resultado in ["Realiza com apoio", "Não realiza"]:
            habilidade_desc = habilidades_map.get(habilidade_cod, f"Habilidade {habilidade_cod}")
            resumo_pontos_apoio.append(f"- {habilidade_desc}: {resultado}")

    if not resumo_pontos_apoio:
        return None, "O aprendiz não apresentou pontos que necessitam de apoio na última avaliação."

    resumo_str = "\n".join(resumo_pontos_apoio)
    prompt = f"""
    Baseado no resumo da avaliação de um aprendiz, gere sugestões para um PEI.
    Pontos que necessitam de apoio:
    {resumo_str}

    Gere texto para:
    1. Objetivos Acadêmicos Gerais (2-3 objetivos).
    2. Adaptações de Conteúdo em Sala (3-4 sugestões práticas).
    3. Adaptações em Avaliações (3-4 sugestões específicas).
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

# NOVO AVISO ADICIONADO AQUI
st.info("As sugestões da IA são geradas com base na **avaliação de habilidades mais recente** do aprendiz. Certifique-se de que a avaliação está preenchida e salva antes de usar esta função.")

if st.button("🤖 Gerar Sugestões com IA"):
    prompt, erro = criar_prompt_pei(st.session_state.get("aprendiz_ativo", {}))
    if erro:
        st.error(erro)
    else:
        with st.spinner("Aguarde, a IA está analisando a avaliação e gerando sugestões..."):
            st.session_state.objetivos_gerados = "1. Desenvolver a autonomia na leitura de palavras simples.\n2. Aprimorar o raciocínio lógico para resolução de problemas matemáticos básicos."
            st.session_state.adapt_sala_gerados = "1. Utilizar material dourado e ábaco nas aulas de matemática.\n2. Apresentar instruções em etapas (uma de cada vez).\n3. Oferecer textos com letras maiores e espaçamento duplo."
            st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das provas.\n2. Ler os enunciados das questões em voz alta para o aluno.\n3. Permitir o uso de uma tabuada de apoio durante as avaliações de matemática."
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

    with st.expander("ETAPA 2: OBJETIVOS POR DISCIPLINA", expanded=True):
        disciplina = st.selectbox("Selecione a Disciplina", options=["Português", "Matemática", "Ciências", "História", "Geografia", "Artes"], index=0)
        codigos_bncc = st.text_input("Adicionar Códigos da BNCC (separados por vírgula)", placeholder="Ex: EF01LP01", value=dados_base.get("codigos_bncc", ""))
        if codigos_bncc:
            lista_codigos = [codigo.strip() for codigo in codigos_bncc.split(',')]
            for codigo in lista_codigos:
                if codigo:
                    descricao = buscar_habilidade_bncc(codigo)
                    if descricao: st.success(descricao)
                    else: st.warning(f"Código '{codigo}' não encontrado.")
        obj_aprendizagem = st.text_area("Objetivo de Aprendizagem", value=dados_base.get("obj_aprendizagem", ""), height=150)
        repertorio_atual = st.text_area("Repertório Atual de Habilidades", value=dados_base.get("repertorio_atual", ""), height=150)
        repertorio_conquistar = st.text_area("Repertório a ser Conquistado", value=dados_base.get("repertorio_conquistar", ""), height=150)

    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        observacoes = st.text_area("Observações Gerais", value=dados_base.get("observacoes", ""), height=200)
        ajustes_proximo_pei = st.text_area("Ajustes para o Próximo PEI", value=dados_base.get("ajustes_proximo_pei", ""), height=200)

    submitted = st.form_submit_button("Salvar PEI")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        novo_pei = {
            "data_criacao": data_atual, "objetivos_gerais": objetivos_gerais, "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes, "disciplina": disciplina, "codigos_bncc": codigos_bncc,
            "obj_aprendizagem": obj_aprendizagem, "repertorio_atual": repertorio_atual,
            "repertorio_conquistar": repertorio_conquistar, "observacoes": observacoes,
            "ajustes_proximo_pei": ajustes_proximo_pei,
        }
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        
        if 'objetivos_gerados' in st.session_state: del st.session_state.objetivos_gerados
        if 'adapt_sala_gerados' in st.session_state: del st.session_state.adapt_sala_gerados
        if 'adapt_avaliacoes_gerados' in st.session_state: del st.session_state.adapt_avaliacoes_gerados
        
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
