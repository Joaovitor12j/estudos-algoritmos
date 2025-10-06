
def pergunta_9():
    nome_aluno = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    nota3 = float(input("Digite a nota da terceira prova: "))

    media = (nota1 + nota2 + nota3) / 3

    print("\n--- Resultado Final ---")
    print(f"Aluno: {nome_aluno}")
    print(f"Média Aritmética: {media:.1f}")


if __name__ == "__main__":
    pergunta_9()