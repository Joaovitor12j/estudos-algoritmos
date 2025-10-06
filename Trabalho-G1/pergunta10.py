
def pergunta_10():
    preco_custo = float(input("Digite o preço de custo do produto: R$ "))
    percentual_acrescimo = float(input("Digite o percentual de acréscimo (apenas o número): "))

    acrescimo = preco_custo * (percentual_acrescimo / 100)
    valor_venda = preco_custo + acrescimo

    print("\n--- Cálculo do Valor de Venda ---")
    print(f"Preço de Custo: R$ {preco_custo:.2f}")
    print(f"Acréscimo de {percentual_acrescimo}%: R$ {acrescimo:.2f}")
    print(f"Valor de Venda Final: R$ {valor_venda:.2f}")

if __name__ == "__main__":
    pergunta_10()