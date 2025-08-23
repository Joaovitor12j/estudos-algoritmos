# Problema 05
# Calcular o fatorial de um número inteiro positivo.

def fatorial(numero: int) -> int:
    if numero == 0 or numero == 1:
        return 1
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado


def main():
    try:
        numero = int(input("Informe um número inteiro positivo: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    if numero < 0:
        print("Entrada inválida: o número deve ser positivo.")
        return

    print(f"O fatorial de {numero} é igual a {fatorial(numero)}.")


if __name__ == "__main__":
    main()
