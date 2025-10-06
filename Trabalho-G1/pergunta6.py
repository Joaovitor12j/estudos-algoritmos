
def pergunta_6():
    valor_compra = float(input("Digite o valor total da compra: R$ "))

    numero_prestacoes = 5
    valor_prestacao = valor_compra / numero_prestacoes

    print("\n--- Detalhes do Parcelamento SBRUBLES ---")
    print(f"Compra no valor de R$ {valor_compra:.2f}")
    print(f"Será dividida em {numero_prestacoes} prestações sem juros.")
    print(f"O valor de cada prestação será de R$ {valor_prestacao:.2f}.")


if __name__ == "__main__":
    pergunta_6()