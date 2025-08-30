import streamlit as st
import datetime
from database_utils import adicionar_novo_pei
from bncc_fundamental import FUNDAMENTAL_DB # Importando a base da BNCC

# --- FUNÇÃO PARA BUSCAR HABILIDADES NA BNCC ---
def buscar_habilidade_bncc(codigo):
    for ano, componentes in FUNDAMENTAL_DB.items():
        for componente, habilidades in componentes.items():
            for habilidade in habilidades:
                if habilidade["codigo"] == codigo.upper():
                    return f'({habilidade["codigo"]}) {habilidade["descricao"]}'
    return None

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Plano de Ensino Individualizado")
st.header("📝 Plano de Ensino Individualizado (PEI)")

if not st.session_state.get("nome_aprendiz_ativo"):
    st.warning("Por favor, selecione um aprendiz na barra lateral para criar um PEI.")
    st.stop()

st.info(f"Criando um novo PEI para: **{st.session_state.nome_aprendiz_ativo}**")

with st.form("form_pei", clear_on_submit=True):
    
    with st.expander("ETAPA 1: OBJETIVOS E ADAPTAÇÕES GERAIS", expanded=True):
        objetivos_gerais = st.text_area("Objetivos Acadêmicos Gerais")
        
        st.subheader("Adaptações Gerais Acadêmicas")
        col1, col2 = st.columns(2)
        with col1:
            adapt_sala = st.text_area("Adaptações de conteúdo em sala")
        with col2:
            adapt_avaliacoes = st.text_area("Adaptações em avaliações")

    with st.expander("ETAPA 2: OBJETIVOS POR DISCIPLINA", expanded=True):
        disciplina = st.selectbox("Selecione a Disciplina", options=["Português", "Matemática", "Ciências", "História", "Geografia", "Artes"])
        
        codigos_bncc = st.text_input("Adicionar Códigos da BNCC (separados por vírgula)", placeholder="Ex: EF01LP01, EF01LP04")
        
        st.write("Conteúdos selecionados:")
        if codigos_bncc:
            lista_codigos = [codigo.strip() for codigo in codigos_bncc.split(',')]
            for codigo in lista_codigos:
                descricao = buscar_habilidade_bncc(codigo)
                if descricao:
                    st.success(descricao)
                else:
                    st.warning(f"Código '{codigo}' não encontrado na base do Ensino Fundamental.")
        
        st.text_area("Objetivo de Aprendizagem (Explicação do objetivo final)", height=150)
        st.text_area("Repertório Atual de Habilidades (O que o aprendiz já consegue fazer)", height=150)
        st.text_area("Repertório que Queremos Conquistar (Próximos passos e habilidades a desenvolver)", height=150)

    with st.expander("ETAPA 3: OBSERVAÇÕES E FINALIZAÇÃO"):
        observacoes = st.text_area("Observações Gerais", height=200)
        ajustes_proximo_pei = st.text_area("Ajustes para o Próximo PEI", height=200)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            redigido_por = st.text_input("Este documento foi redigido por")
        with col2:
            participacao_mae = st.text_input("Com participação da mãe/pai/responsável")
        
        st.write("Cientes:")
        col1, col2, col3 = st.columns(3)
        with col1:
            ciente_coord = st.text_input("Nome da Coordenadora Pedagógica")
        with col2:
            ciente_prof = st.text_input("Nome da Professora Polivalente")
        with col3:
            ciente_mae = st.text_input("Nome da Mãe/Pai/Responsável")

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
            # Adicione aqui as outras variáveis do formulário para salvar...
        }
        
        adicionar_novo_pei(st.session_state.nome_aprendiz_ativo, novo_pei)
        st.success(f"Novo PEI para '{st.session_state.nome_aprendiz_ativo}' salvo com sucesso!")
        st.balloons()
