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

def salvar_dados_cadastro(nome_aprendiz, dados_cadastro):
    """ Salva ou atualiza os dados cadastrais (seção 'cadastro') """
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    
    aprendizes[nome_aprendiz]["cadastro"] = dados_cadastro
    
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True

def adicionar_nova_avaliacao(nome_aprendiz, nova_avaliacao):
    """ Adiciona uma nova avaliação à lista de avaliações do aprendiz """
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    
    # Garante que a lista de avaliações exista
    if "avaliacoes" not in aprendizes[nome_aprendiz]:
        aprendizes[nome_aprendiz]["avaliacoes"] = []

    aprendizes[nome_aprendiz]["avaliacoes"].append(nova_avaliacao)
    
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True
