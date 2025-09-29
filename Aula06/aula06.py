
import random

def main():

    linhas = 3
    colunas = 3

    M = []

    letra_atual = ord('A')
    for i in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(chr(letra_atual))
            letra_atual += 1
        M.append(linha)

    for linha in M:
        print(linha)

if __name__ == "__main__":
    main()