
def pergunta_5():

    idade = int(input("Informe a idade: "))

    if idade < 12:
        print("Criança")
    elif idade < 18:
        print("Adolescente")
    elif idade < 60:
        print("Adulto")
    else:
        print("Idoso")

if __name__ == "__main__":
    pergunta_5()
