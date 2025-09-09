
def main():

    numeroExercicio = int(input("Insira o exercício: "))

    match numeroExercicio:
        case 1:
            print("Exibir um número de 1 a 10 usando um laço for")
            for i in range(1, 11):
                print(i)
            return
        case 2:
            print("Exibir números pares de 2 a 20")
            for i in range(2, 21, 2):
                print(i)
            return
        case 3:
            print("Exibir números de 1 a 5 usando while")
            i = 1
            while i <= 5:
                print(i)
                i += 1
            return
        case 4:
            print("Exibir a soma de números de 1 a 100 usando for")
            soma = 0
            for i in range(1, 101):
                soma += i
            print(soma)
        case 5:
            print("Receber um número e exibir a tabuada usando o for")
            numero = int(input("Insira um número: "))
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
            return
        case 6:
            print("Receber um número e exibir todos os números até ele usando while")
            numero = int(input("Insira um número: "))
            i = 1
            while i <= numero:
                print(i)
                i += 1
            return
        case 7:
            print("Exibir a soma dos números pares de 1 a 50")
            soma = 0
            for i in range(2, 51, 2):
                soma += i
            print(soma)
        case 8:
            print("Contar quantos números de 1 a 100 são múltiplos de 7")
            contador = 0
            for i in range(1, 101):
                if i % 7 == 0:
                    contador += 1
            print(contador)
        case 9:
            print("Exibir uma lista de 1 a 10 usando for")
            lista = [i for i in range(1, 11)]
            print(lista)
        case 10:
            print("Somar todos os elementos de uma lista de números inteiros fornecidos")
            lista = input("Insira uma lista de números inteiros separados por espaço: ").split()
            soma = sum(int(num) for num in lista)
            print(soma)
        case 11:
            print("Exibir 5 nomes de uma lista um por um")
            nomes = ["João", "Vitor", "Thaiane", "Elisa", "Cacau"]
            for nome in nomes:
                print(nome)
        case 12:
            print("Receber 10 numeros, armazenar e exibir os números pares")
            numeros = []
            for _ in range(10):
                numero = int(input("Insira um número: "))
                numeros.append(numero)
            numeros_pares = [num for num in numeros if num % 2 == 0]
            print(numeros_pares)
        case 13:
            print("Receber 10 números e exibir o maior e o menor")
            numeros = []
            for _ in range(10):
                numero = int(input("Insira um número: "))
                numeros.append(numero)
            maior = max(numeros)
            menor = min(numeros)
            print(f"Maior: {maior}, Menor: {menor}")
        case 14:
            print("Exibir a média de 10 números de uma lista")
            numeros = []
            sequencia = 1
            for _ in range(10):
                numero = int(input(f"Insira o número {sequencia}: "))
                numeros.append(numero)
                sequencia += 1
            media = sum(numeros) / len(numeros)
            print(f"Média: {media}")
        case 15:
            print("Crie um programa que leia uma lista de números e mostre apenas os números ímpares.")
            numeros = []
            for _ in range(5):
                numero = int(input("Insira um número: "))
                numeros.append(numero)
            numeros_impares = [num for num in numeros if num % 2 != 0]
            print(numeros_impares)
        case 16:
            print("Multiplicar todos os números de uma lista por 2")
            numeros = []
            for _ in range(5):
                numero = int(input("Insira um número: "))
                numeros.append(numero)
            numeros_multiplicados = [num * 2 for num in numeros]
            print(numeros_multiplicados)
        case 17:
            print("Crie uma lista de 10 números e exiba apenas aqueles maiores que a média da lista.")
            numeros = []
            for _ in range(10):
                numero = int(input("Insira um número: "))
                numeros.append(numero)
            media = sum(numeros) / len(numeros)
            numeros_maiores = [num for num in numeros if num > media]
            print(numeros_maiores)
        case 18:
            print("Criar um vetor com 5 números e exibir o quadrado de cada um dos elementos.")
            numeros = []
            for _ in range(5):
                numero = int(input("Insira um número: "))
                numeros.append(numero)
            numeros_quadrados = [num ** 2 for num in numeros]
            print(numeros_quadrados)
        case 19:
            print(" Leia 5 notas de um aluno e calcule a média, exibindo se ele foi aprovado (média >= 6) ou reprovado.")
            notas = []
            for _ in range(5):
                nota = float(input("Insira uma nota: "))
                notas.append(nota)
            media = sum(notas) / len(notas)
            if media >= 6:
                print("Aprovado")
            else:
                print("Reprovado")
        case 20:
            print("Criar uma matriz 3x3 e exibir os elementos de cada linha.")
            matriz = []
            for _ in range(3):
                linha = []
                for _ in range(3):
                    elemento = int(input("Insira um elemento: "))
                    linha.append(elemento)
                matriz.append(linha)
            for linha in matriz:
                print(linha)
        case 21:
            print("Some os elementos da diagonal principal de uma matriz 3x3.")
            matriz = []
            for _ in range(3):
                linha = []
                for _ in range(3):
                    elemento = int(input("Insira um elemento: "))
                    linha.append(elemento)
                matriz.append(linha)
            soma_diagonal = sum(matriz[i][i] for i in range(3))
            print(f"Soma da diagonal principal: {soma_diagonal}")
        case 22:
            print("Criar uma matriz 2x2 e exiba sua transposta.")
            matriz = []
            for _ in range(2):
                linha = []
                for _ in range(2):
                    elemento = int(input("Insira um elemento: "))
                    linha.append(elemento)
                matriz.append(linha)
            transposta = [[matriz[j][i] for j in range(2)] for i in range(2)]
            for linha in transposta:
                print(linha)
        case 23:
            print("Ler 4 números de uma lista, exibir o maior e a posição")
            numeros = []
            for _ in range(4):
                numero = int(input("Insira um número: "))
                numeros.append(numero)
            maior = max(numeros)
            posicao = numeros.index(maior)
            print(f"Maior número: {maior}, Posição: {posicao}")
        case 24:
            print("Receber números até que seja digitado 0, armazenar em uma lista e mostrar a soma")
            numeros = []
            while True:
                numero = int(input("Insira um número (0 para sair): "))
                if numero == 0:
                    break
                numeros.append(numero)
            soma = sum(numeros)
            print(f"Soma dos números: {soma}")
        case 25:
            print("Receber 2 listas de 5 números e exiba a lista resultante da soma dos elementos de mesma posição.")
            lista1 = []
            lista2 = []
            for _ in range(5):
                numero1 = int(input("Insira um número para a lista 1: "))
                numero2 = int(input("Insira um número para a lista 2: "))
                lista1.append(numero1)
                lista2.append(numero2)
            lista_soma = [lista1[i] + lista2[i] for i in range(5)]
            print(f"Lista resultante: {lista_soma}")
        case 26:
            print("Receber uma frase e contar quantas vogais ela possui")
            frase = input("Insira uma frase: ")
            vogais = "aeiouAEIOU"
            contador = sum(1 for letra in frase if letra in vogais)
            print(f"Quantidade de vogais: {contador}")
        case 27:
            print("Ler uma matriz 3x3 e exiba a soma de cada linha.")
            matriz = []
            for _ in range(3):
                linha = []
                for _ in range(3):
                    elemento = int(input("Insira um elemento: "))
                    linha.append(elemento)
                matriz.append(linha)
            for i in range(3):
                soma_linha = sum(matriz[i])
                print(f"Soma da linha {i+1}: {soma_linha}")
        case 28:
            print("Receber uma lista de números e exibir True se a lista estiver ordenada em ordem crescente e False caso "
                  "contrário.")
            lista = []
            for _ in range(5):
                numero = int(input("Insira um número: "))
                lista.append(numero)
            ordenada = all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
            print(f"Lista ordenada: {ordenada}")
        case 29:
            print("Gerar a sequencia de Fibonacci até o decimo termo.")
            sequencia = [0, 1]
            for _ in range(8):
                sequencia.append(sequencia[-1] + sequencia[-2])
            print(f"Sequencia: {sequencia}")
        case 30:
            print("Ler uma matriz 3x3 e exibir o maior elemento.")
            matriz = []
            for _ in range(3):
                linha = []
                for _ in range(3):
                    elemento = int(input("Insira um elemento: "))
                    linha.append(elemento)
                matriz.append(linha)
            maior = max(max(linha) for linha in matriz)
            print(f"Maior elemento: {maior}")
        case _:
            print("Exercício inválido")

if __name__ == "__main__":
    main()
