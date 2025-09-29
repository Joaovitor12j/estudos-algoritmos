
import random

def main():
    value_n = int(input("Digite o valor de N: "))

    if value_n <= 0:
        print("N deve ser um inteiro positivo maior que zero.")
        return

    vetor = [random.randint(1, value_n * value_n) for _ in range(value_n)]

    maior_valor = max(vetor)
    posicao = vetor.index(maior_valor)

    print(f"Vetor: {vetor}")
    print(f"Maior valor: {maior_valor}")
    print(f"Posição do maior valor (índice): {posicao}")

if __name__ == "__main__":
    main()