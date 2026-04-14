import json
import os

def carregar_parametros(caminho_json: str) -> dict:
    """
    Subalgoritmo para ler o arquivo JSON de referência técnica.
    Retorna um dicionário com as regras de cada cultura.
    """
    try:
        base_path = os.path.dirname(__file__)
        full_path = os.path.join(base_path, 'data', 'parametros.json')

        with open(full_path, 'r', encoding='utf-8') as file:
            dados = json.load(file)
        
        return dados['culturas']

    except FileNotFoundError:
        print(f"Erro: Arquivo {caminho_json} não encontrado.")
        return {}

    except Exception as e:
        print(f"Erro inesperado ao carregar JSON: {e}")
        return {}

def avaliar_saude_solo(amostra, parametros: dict ) -> tuple:
    """
    Compara uma amostra (dict) com os parâmetros da cultura.
    Retorna uma tupla (Status, Recomendação).
    """
    cultura = amostra['cultura'].lower()

    if cultura not in parametros:
        return ("Erro", "Cultura não catalogada nos parâmetros técnicos.")

    regras = parametros[cultura]
    alertas = []

    # 1. Nitrogênio (N)
    if amostra['nitrogenio'] < regras['nitrogenio_min_mg_dm3']:
        alertas.append("Suplementar Nitrogênio (N)")

    # 2. Fósforo (P)
    if amostra['fosforo'] < regras['fosforo_min_mg_dm3']:
        alertas.append("Suplementar Fósforo (P)")

    # 3. Potássio (K)
    if amostra['potassio'] < regras['potassio_min_cmolc_dm3']:
        alertas.append("Suplementar Potássio (K)")

    # 4. pH
    ph = amostra['ph']

    if ph < regras['ph_faixa'][0]:
        alertas.append("Aplicar Calcário (pH baixo)")
        
    elif ph > regras['ph_faixa'][1]:
        alertas.append("Solo muito alcalino")

    status = "Saudável" if not alertas else "Necessita Atenção"
    recomendacao = "Solo em conformidade técnica." if not alertas else " | ".join(alertas)

    return (status, recomendacao)

