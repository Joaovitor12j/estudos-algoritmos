

def main():

    # idade = 20
    # altura = 1.85
    # ativo = True
    # lista = []
    #
    # print(f"variavel idade contem o valor {idade} e é do tipo {type(idade)}")
    # print(f"variavel altura contem o valor {altura} e é do tipo {type(altura)}")
    # print(f"variavel ativo contem o valor {ativo} e é do tipo {type(ativo)}")
    # print(f"variavel lista contem o valor {lista} e é do tipo {type(lista)}")

    # operacao = int(input("Informe a operação desejada:  \n"
    #                      "#1: Soma \n"
    #                      "#2: Subtração \n > "))
    #
    # if operacao == 1:
    #     print("Selecionado Soma \n")
    #
    #     operador1 = int(input("Informe o operador 1: "))
    #     operador2 = int(input("Informe o operador 2: "))
    #
    #     print(f"Resultado: {operador1 + operador2}")
    # elif operacao == 2:
    #     print("Selecionado Subtração")
    #
    #     operador1 = int(input("Informe o operador 1: "))
    #     operador2 = int(input("Informe o operador 2: "))
    #
    #     print(f"Resultado: {operador1 - operador2}")
    # else:
    #     print("Operação inválida")
    #
    # print("Obrigado por utilizar nosso sistema.")

    # linguagens = ["Python", "Java", "C++", "C#", "JavaScript", "PHP", "Ruby", "Lua"]
    #
    # for linguagem in linguagens:
    #     # print(linguagem)
    #
    #     if linguagem == "PHP":
    #         print(f"{linguagem} é a melhor linguagem")
    #     elif linguagem == "JavaScript":
    #         print(f"{linguagem} é Linguagem de louco")
    #     else:
    #         print(f"{linguagem} é uma Linguagem boa")

    notas = []
    for nota in range(1, 4):
        value = float(input(f"Informa a nota da matéria {nota}: "))
        notas.append(value)

    media = sum(notas) / len(notas)
    menor_nota = min(notas)
    maior_nota = max(notas)

    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Menor nota: {menor_nota:.2f}")
    print(f"Maior nota: {maior_nota:.2f}")

if __name__ == "__main__":
    main()