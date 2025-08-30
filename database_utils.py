import json
import os

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
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    aprendizes[nome_aprendiz]["cadastro"] = dados_cadastro
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True

def adicionar_nova_avaliacao(nome_aprendiz, nova_avaliacao):
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    if "avaliacoes" not in aprendizes[nome_aprendiz]:
        aprendizes[nome_aprendiz]["avaliacoes"] = []
    aprendizes[nome_aprendiz]["avaliacoes"].append(nova_avaliacao)
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True

def adicionar_novo_pei(nome_aprendiz, novo_pei):
    """ Adiciona um novo PEI à lista de PEIs do aprendiz """
    aprendizes = carregar_dados()
    if nome_aprendiz not in aprendizes:
        aprendizes[nome_aprendiz] = {}
    if "peis" not in aprendizes[nome_aprendiz]:
        aprendizes[nome_aprendiz]["peis"] = []
    aprendizes[nome_aprendiz]["peis"].append(novo_pei)
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(aprendizes, f, ensure_ascii=False, indent=4)
    return True

def excluir_aprendiz(nome_aprendiz):
    aprendizes = carregar_dados()
    if nome_aprendiz in aprendizes:
        del aprendizes[nome_aprendiz]
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(aprendizes, f, ensure_ascii=False, indent=4)
        return True
    return False
