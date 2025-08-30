import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_fundamental import FUNDAMENTAL_DB # Importando a base da BNCC

# --- FUNÇÃO PARA BUSCAR HABILIDADES NA BNCC ---
def buscar_habilidade_bncc(codigo):
    codigo = codigo.upper().strip()
    for ano, componentes in FUNDAMENTAL_DB.items():
        for componente, habilidades in componentes.items():
            for habilidade in habilidades:
                if habilidade["codigo"] == codigo:
                    return f'({habilidade["codigo"]}) {habilidade["descricao"]}'
    return None

# --- LÓGICA DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

# Carrega o PEI mais recente para preencher o formulário como base, se houver
peis_anteriores = st.session_state.get("aprendiz_ativo", {}).get("peis", [])
dados_base = peis_anteriores[-1] if peis_anteriores else {}

with st.form("form_pei"):
    
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        
        # Botão para gerar sugestões com IA
        if st.button("🤖 Gerar Sugestões com IA"):
            avaliacoes = st.session_state.get("aprendiz_ativo", {}).get("avaliacoes", [])
            if not avaliacoes:
                st.error("Nenhuma avaliação encontrada para este aprendiz. Preencha a Avaliação de Habilidades primeiro.")
            else:
                with st.spinner("Aguarde, a IA está analisando a avaliação e gerando sugestões..."):
                    # Aqui, em um cenário real, ocorreria a chamada para a IA.
                    # Para este aplicativo, simulamos a resposta da IA com sugestões padrão.
                    st.session_state.objetivos_gerados = "1. Aprimorar o reconhecimento de sílabas simples e a formação de palavras.\n2. Desenvolver a capacidade de resolver problemas matemáticos de adição e subtração com suporte visual.\n3. Ampliar a participação em atividades em grupo, respeitando as regras e a vez dos colegas."
                    st.session_state.adapt_sala_gerados = "1. Utilizar letras móveis e jogos silábicos para a construção de palavras.\n2. Oferecer material dourado ou ábaco para a resolução de operações matemáticas.\n3. Apresentar instruções de forma clara, em etapas curtas (uma de cada vez).\n4. Utilizar um cronograma visual com a rotina das atividades do dia."
                    st.session_state.adapt_avaliacoes_gerados = "1. Permitir tempo extra para a conclusão das avaliações.\n2. Ler os enunciados das questões em voz alta para o aluno.\n3. Permitir a consulta a materiais de apoio (ex: tabuada, alfabeto).\n4. Realizar avaliações orais ou com menor número de questões por página."
                st.success("Sugestões geradas pela IA!")

        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=st.session_state.get("objetivos_gerados", dados_base.get("objetivos_gerais", "")), height=150)
        
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=st.session_state.get("adapt_sala_gerados", dados_base.get("adapt_sala", "")), height=200)
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=st.session_state.get("adapt_avaliacoes_gerados", dados_base.get("adapt_avaliacoes", "")), height=200)

    with st.expander("ETAPA 2: OBJETIVOS POR DISCIPLINA", expanded=True):
        disciplina = st.selectbox("Selecione a Disciplina", options=["Português", "Matemática", "Ciências", "História", "Geografia", "Artes"], index=0)
        codigos_bncc = st.text_input("Adicionar Códigos da BNCC (separados por vírgula)", placeholder="Ex: EF01LP05, EF01LP02", value=dados_base.get("codigos_bncc", ""))
        
        if codigos_bncc:
            st.write("**Conteúdos selecionados:**")
            lista_codigos = [codigo.strip() for codigo in codigos_bncc.split(',')]
            for codigo in lista_codigos:
                if codigo:
                    descricao = buscar_habilidade_bncc(codigo)
                    if descricao:
                        st.success(descricao)
                    else:
                        st.warning(f"Código '{codigo}' não encontrado na base do Ensino Fundamental.")
        
        obj_aprendizagem = st.text_area("Objetivo de Aprendizagem (Descrição do objetivo final)", value=dados_base.get("obj_aprendizagem", ""), height=150)
        repertorio_atual = st.text_area("Repertório Atual de Habilidades (O que o aprendiz já consegue fazer)", value=dados_base.get("repertorio_atual", ""), height=150)
        repertorio_conquistar = st.text_area("Repertório que Queremos Conquistar (Próximos passos)", value=dados_base.get("repertorio_conquistar", ""), height=150)

    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        observacoes = st.text_area("Observações Gerais", value=dados_base.get("observacoes", ""), height=200)
        ajustes_proximo_pei = st.text_area("Ajustes para o Próximo PEI", value=dados_base.get("ajustes_proximo_pei", ""), height=200)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            redigido_por = st.text_input("Este documento foi redigido por", value=dados_base.get("redigido_por", ""))
        with col2:
            participacao_mae = st.text_input("Com participação da mãe/pai/responsável", value=dados_base.get("participacao_mae", ""))

    submitted = st.form_submit_button("Salvar PEI")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        novo_pei = {
            "data_criacao": data_atual, "objetivos_gerais": objetivos_gerais, "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes, "disciplina": disciplina, "codigos_bncc": codigos_bncc,
            "obj_aprendizagem": obj_aprendizagem, "repertorio_atual": repertorio_atual, "repertorio_conquistar": repertorio_conquistar,
            "observacoes": observacoes, "ajustes_proximo_pei": ajustes_proximo_pei, "redigido_por": redigido_por, "participacao_mae": participacao_mae,
        }
        
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
