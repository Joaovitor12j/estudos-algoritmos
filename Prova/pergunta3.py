def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero > 0:
                break
            print("Por favor, digite um número inteiro POSITIVO.")
        except ValueError:
            print("Entrada inválida. Digite um número INTEIRO positivo.")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    main()
