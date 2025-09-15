
import random

def main():

    value_n = int(input("Digite o valor de N: "))

    if value_n <= 0:
        print("N deve ser um inteiro positivo maior que zero.")
        return

    vetor_a = [random.randint(1, value_n) for _ in range(value_n)]
    vetor_b = [random.randint(1, value_n) for _ in range(value_n)]

    vetor_soma = [vetor_a[i] + vetor_b[i] for i in range(value_n)]

    print(f"A: {vetor_a}")
    print(f"B: {vetor_b}")
    print(f"C: {vetor_soma}")

if __name__ == "__main__":
    main()