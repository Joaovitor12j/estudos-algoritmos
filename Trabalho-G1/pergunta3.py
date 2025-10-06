
def pergunta_3():
    valor_depositado = float(input("Digite o valor do depósito: R$ "))

    juro = 0.0070

    valor_final = valor_depositado * (1 + juro)

    print("\nCalculando rendimento da poupança a 0,70% a.m...")
    print(f"O valor com rendimento após um mês será de R$ {valor_final:.2f}.")

if __name__ == "__main__":
    pergunta_3()