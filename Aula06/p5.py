import random

def main():
    value_n = int(input("Digite o valor de N: "))

    if value_n <= 0:
        print("N deve ser um inteiro positivo maior que zero.")
        return

    vetor = [random.randint(1, value_n * value_n) for _ in range(value_n)]

    pares = sum(1 for x in vetor if x % 2 == 0)
    impares = value_n - pares

    print(f"Vetor: {vetor}")
    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de ímpares: {impares}")

if __name__ == "__main__":
    main()
