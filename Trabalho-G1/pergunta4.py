
def pergunta_4():
    nome = input("Digite o nome do vendedor: ")
    salario_fixo = float(input(f"Digite o salário fixo de {nome}: R$ "))
    total_vendas = float(input(f"Digite o total de vendas de {nome} no mês: R$ "))

    percentual_comissao = 0.15
    valor_comissao = total_vendas * percentual_comissao
    salario_final = salario_fixo + valor_comissao

    print("\n" + "="*30)
    print("      RESUMO DO VENDEDOR")
    print("="*30)
    print(f"Nome: {nome}")
    print(f"Salário Fixo: R$ {salario_fixo:.2f}")
    print(f"Salário Final (com comissão): R$ {salario_final:.2f}")
    print("="*30)

if __name__ == "__main__":
    pergunta_4()