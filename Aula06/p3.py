import random

def main():
    value_n = int(input("Digite o valor de N: "))

    if value_n <= 0:
        print("N deve ser um inteiro positivo maior que zero.")
        return

    vetor = [random.randint(1, value_n * value_n) for _ in range(value_n)]

    produto_escalar = sum(x * x for x in vetor)

    print(f"Vetor: {vetor}")
    print(f"Produto escalar (soma dos quadrados): {produto_escalar}")

if __name__ == "__main__":
    main()
