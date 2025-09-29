
def pergunta_4():

    valor_a = int(input("Informe o valor de A (Precisa ser maior do que 0): "))
    if valor_a <= 0:
        print("O valor de A deve ser maior do que 0. Tente novamente.")
        return

    valor_b = int(input("Informe o valor de B (Precisa ser maior do que A e maior que 0): "))
    if valor_b <= valor_a or valor_b <= 0:
        print("O valor de B deve ser maior do que A e maior que 0. Tente novamente.")
        return

    primeiro_par = valor_a + 1
    if valor_a % 2 == 0:
        primeiro_par = valor_a

    pares = list(range(primeiro_par, valor_b + 1, 2))
    if primeiro_par > valor_b:
        pares = []

    saida = "."
    if pares:
        saida = ", ".join(map(str, pares)) + "."

    print(saida)

if __name__ == "__main__":
    pergunta_4()
