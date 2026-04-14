from processamento import carregar_parametros, avaliar_saude_solo, coletar_dados

def main():

    # Carregar Regras (JSON)
    regras = carregar_parametros("data/parametros.json")
    if not regras: return

    # Input do usuário
    dados_usuario = coletar_dados(regras)
    
    # Processar
    status, acao = avaliar_saude_solo(dados_usuario, regras)

    print("-" * 40)
    print(f"RELATÓRIO DE ANÁLISE: {dados_usuario['cultura'].upper()}")
    print(f"Status: {status}")
    print(f"Recomendação: {acao}")
    print("-" * 40)

if __name__ == "__main__":
    main()