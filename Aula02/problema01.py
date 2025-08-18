# Problema 01
# Ler dois ângulos de um triângulo, calcular o terceiro e informar se é triângulo retângulo.
# Saídas conforme exemplos da lista.

def main():
    try:
        angulo1 = int(input("Ângulo 1: "))
        angulo2 = int(input("Ângulo 2: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    angulo3 = 180 - angulo1 - angulo2

    # Mostra o ângulo calculado
    print(f"Ângulo 3: {angulo3}.", end=" ")

    # Imprime Triângulo retângulo se algum ângulo for 90
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("É triangulo retângulo.")
    else:
        print("Não é triangulo retângulo.")


if __name__ == "__main__":
    main()
