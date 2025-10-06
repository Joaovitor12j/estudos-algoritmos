
def pergunta_1():

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2

    print("\n--- Resultados ---")
    print(f"Soma: {numero1} + {numero2} = {soma}")
    print(f"Subtração: {numero1} - {numero2} = {subtracao}")
    print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")

    if numero2 != 0:
        divisao = numero1 / numero2
        print(f"Divisão: {numero1} / {numero2} = {divisao:.2f}")
    else:
        print("Divisão: Não é possível dividir por zero")

if __name__ == "__main__":
    pergunta_1()