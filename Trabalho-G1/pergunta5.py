
def pergunta_5():
    cotacao_dolar = float(input("Digite a cotação atual do dólar: R$ "))
    quantidade_dolares = float(input("Digite a quantidade de dólares a converter: US$ "))

    valor_em_real = quantidade_dolares * cotacao_dolar

    print("\n--- Resultado da Conversão ---")
    print(f"Valor em Dólar: US$ {quantidade_dolares:.2f}")
    print(f"Cotação do Dólar: R$ {cotacao_dolar:.2f}")
    print(f"Valor em Real: R$ {valor_em_real:.2f}")

if __name__ == "__main__":
    pergunta_5()