def pan_digital(sequencia: str) -> bool:
    # print("Entrou no pan_digital 002 >>>")
    # print(f"Sequencia: {sequencia}")
    # print(f"len Sequencia: {len(sequencia)}")
    return len(sequencia) == 9 and set(sequencia) == set("123456789")

def desafio01():
    identidades_pandigitais = []
    produtos_unicos_set = set()

    # Pegar 1 digito de 1 a 9
    for multiplicando in range(4, 10):
        print(f"Multiplicando: {multiplicando}")
        # Pegar 4 digito de 1234 a 9876
        for multiplicador in range(1234, 9877):
            # print(f"Multiplicador: {multiplicador}")
            produto = multiplicando * multiplicador
            # print(f"Produto >>: {produto}")
            concatenacao = f"{multiplicando}{multiplicador}{produto}"
            # print(f"Concatenação: {concatenacao}")
            if "0" in concatenacao:
                # print(f"if concatenacao {concatenacao}")
                # return
                continue
            if pan_digital(concatenacao):
                print("Chegou aqui")
                # return
                identidades_pandigitais.append((multiplicando, multiplicador, produto))
                produtos_unicos_set.add(produto)
                print("Saiu do if pan_digital")
                # return
        # print(produtos_unicos_set)
        # return

    for multiplicando in range(12, 99):
        for multiplicador in range(123, 988):
            produto = multiplicando * multiplicador
            concatenacao = f"{multiplicando}{multiplicador}{produto}"
            if "0" in concatenacao:
                continue
            if pan_digital(concatenacao):
                identidades_pandigitais.append((multiplicando, multiplicador, produto))
                produtos_unicos_set.add(produto)


    # print(produtos_unicos_set)
    # print(identidades_pandigitais)
    # print("Saiu do for 1")
    # return

    print("Identidades pandigitais:")
    for multiplicando, multiplicador, produto in sorted(identidades_pandigitais, key=lambda x: (x[2], x[0], x[1])):
        print(f"{multiplicando} × {multiplicador} = {produto}")

    print("\nProdutos únicos:")
    for produto in sorted(produtos_unicos_set):
        print(produto)
    print("\nSoma dos produtos únicos:", sum(produtos_unicos_set))

if __name__ == "__main__":
    desafio01()
