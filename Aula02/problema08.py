# Problema 08
# Ler um número inteiro positivo e indicar se é um número perfeito.

def soma_divisores_proprios(numero: int) -> int:
    if numero <= 1:
        return 0
    soma = 1
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            soma += divisor
            outro_divisor = numero // divisor
            if outro_divisor != divisor and outro_divisor != numero:
                soma += outro_divisor
        divisor += 1
    return soma


def main():
    try:
        numero = int(input("Informe um número inteiro positivo: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    if numero <= 0:
        print("Entrada inválida: número deve ser positivo.")
        return

    perfeito = (soma_divisores_proprios(numero) == numero)
    if perfeito:
        print("É um número perfeito.")
        return

    print("Não é número perfeito.")


if __name__ == "__main__":
    main()
