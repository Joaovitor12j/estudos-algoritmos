

def pergunta_1():

    nomes = []

    for i in range(5):
        nome = input(f"Digite o {i+1}º nome: ")
        nomes.append(nome)

    print("Todos os nomes na lista:")
    for n in nomes:
        print(n)

    print(f"Primeiro nome na lista: {nomes[0]}")
    print(f"Último nome na lista: {nomes[-1]}")


if __name__ == "__main__":
    pergunta_1()
    