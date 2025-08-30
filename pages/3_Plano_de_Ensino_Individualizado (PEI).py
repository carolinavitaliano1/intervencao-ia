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

with st.form("form_pei", clear_on_submit=False):
    
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais", value=dados_base.get("objetivos_gerais", ""))
        
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala", value=dados_base.get("adapt_sala", ""))
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações", value=dados_base.get("adapt_avaliacoes", ""))

    with st.expander("ETAPA 2: OBJETIVOS POR DISCIPLINA", expanded=True):
        disciplina = st.selectbox("Selecione a Disciplina", options=["Português", "Matemática", "Ciências", "História", "Geografia", "Artes"], index=0)
        
        codigos_bncc = st.text_input("Adicionar Códigos da BNCC (separados por vírgula)", placeholder="Ex: EF01LP01, EF01LP04", value=dados_base.get("codigos_bncc", ""))
        
        st.write("Conteúdos selecionados:")
        if codigos_bncc:
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
        
        st.write("Cientes:")
        col1, col2, col3 = st.columns(3)
        with col1:
            ciente_coord = st.text_input("Nome da Coordenadora Pedagógica", value=dados_base.get("ciente_coord", ""))
        with col2:
            ciente_prof = st.text_input("Nome da Professora Polivalente", value=dados_base.get("ciente_prof", ""))
        with col3:
            ciente_mae = st.text_input("Nome da Mãe/Pai/Responsável", value=dados_base.get("ciente_mae", ""))

    submitted = st.form_submit_button("Salvar PEI")
    if submitted:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        novo_pei = {
            "data_criacao": data_atual,
            "objetivos_gerais": objetivos_gerais,
            "adapt_sala": adapt_sala,
            "adapt_avaliacoes": adapt_avaliacoes,
            "disciplina": disciplina,
            "codigos_bncc": codigos_bncc,
            "obj_aprendizagem": obj_aprendizagem,
            "repertorio_atual": repertorio_atual,
            "repertorio_conquistar": repertorio_conquistar,
            "observacoes": observacoes,
            "ajustes_proximo_pei": ajustes_proximo_pei,
            "redigido_por": redigido_por,
            "participacao_mae": participacao_mae,
            "ciente_coord": ciente_coord,
            "ciente_prof": ciente_prof,
            "ciente_mae": ciente_mae,
        }
        
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
