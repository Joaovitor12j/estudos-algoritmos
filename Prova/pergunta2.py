

def pergunta_2():

    valores = []
    for _ in range(3):
        numero = int(input("Insira um número: "))
        if numero < 0:
            print("O numero deve ser positivo. Tente novamente.")
            return
        valores.append(numero)

    maior = max(valores)
    menor = min(valores)
    media = sum(valores) / len(valores)

    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Média dos 3 valores: {media:.2f}")

if __name__ == "__main__":
    pergunta_2()
