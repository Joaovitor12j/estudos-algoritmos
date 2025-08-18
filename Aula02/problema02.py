# Problema 02
# Ler dois números inteiros e positivos: A e B. Considerar que A < B.
# Mostrar a média dos pares menores que B, excluindo A.

def media_pares_excluindo_a(a: int, b: int):
    soma = 0
    cont = 0
    # começa em 2 (primeiro par positivo) e vai até < b, de 2 em 2
    for x in range(2, b, 2):
        if x != a:
            soma += x
            cont += 1
    if cont == 0:
        return None
    return soma / cont


def main():
    try:
        a = int(input("A: "))
        b = int(input("B: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    if a >= b or a <= 0 or b <= 0:
        print("Entrada inválida: garanta que A < B e ambos sejam positivos (> 0).")
        return

    m = media_pares_excluindo_a(a, b)
    if m is None:
        print("Média: indefinida (nenhum número par encontrado)")
    else:
        # imprimir como inteiro se for inteiro exato
        if abs(m - round(m)) < 1e-9:
            print(f"Média: {int(round(m))}")
        else:
            # limitar casas para clareza
            print(f"Média: {m:.6f}")


if __name__ == "__main__":
    main()
