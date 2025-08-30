import json
import os
import streamlit as st

DB_FILE = "aprendizes.json"

def carregar_dados():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def salvar_dados_aprendiz(nome_aprendiz, dados_para_salvar, secao):
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    
    if secao not in aprendizes[nome_aprendiz]:
        aprendizes[nome_aprendiz][secao] = {}

    aprendizes[nome_aprendiz][secao].update(dados_para_salvar)
    
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True
