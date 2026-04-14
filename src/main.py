from processamento import carregar_parametros, avaliar_saude_solo

def main():

    # 1. Carregar Regras (JSON)
    regras_tecnicas = carregar_parametros("data/parametros.json")

    # 2. Simular uma entrada de dados (Posteriormente virá do Oracle ou Input)
    amostra_teste = {
        "cultura": "soja",
        "ph": 5.2,
        "fosforo": 10.5,
        "potassio": 55.0,
        "nitrogenio": 15.0
    }

    # 3. Processar
    status, acao = avaliar_saude_solo(amostra_teste, regras_tecnicas)

    print("-" * 40)
    print(f"RELATÓRIO DE ANÁLISE: {amostra_teste['cultura'].upper()}")
    print(f"Status: {status}")
    print(f"Recomendação: {acao}")
    print("-" * 40)

if __name__ == "__main__":
    main()