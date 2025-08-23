# Problema 06
# Números triangulares: Tn = n(n+1)/2. Ler n e mostrar Tn.

def triangular(valor_n: int) -> int:
    return valor_n * (valor_n + 1) // 2

def main():
    try:
        valor_n = int(input("Informe o valor de N: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    if valor_n < 0:
        print("Entrada inválida: N deve ser positivo.")
        return

    print(f"T{valor_n} = {triangular(valor_n)}")


if __name__ == "__main__":
    main()
