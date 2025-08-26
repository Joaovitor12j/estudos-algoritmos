def main():

    # nome = input('Informe o seu nome: ')
    # nota_materia1 = float(input('Informe a nota da matéria 1: '))
    # nota_materia2 = float(input('Informe a nota da matéria 2: '))
    # nota_materia3 = float(input('Informe a nota da matéria 3: '))
    #
    # media = (nota_materia1 * 0.4) + (nota_materia2 * 0.3) + (nota_materia3 * 0.3)
    #
    # print(f"\nOlá, {nome}! Sua média é {media:.2f}")
    # return

    # celsius = float(input('Informe a temperatura em Celsius: '))
    # fahrenheit = (celsius * 9 / 5) + 32
    #
    # print(f"\nTemperatura em Fahrenheit: {fahrenheit:.1f}°F")
    # return

    """
    valor_a = int(input("Informe o valor de A: "))
    valor_b = int(input("Informe o valor de B: "))

    if valor_a > valor_b:
        print("A é maior que B")
        return

    if valor_b > valor_a:
        print("B é maior que A")
        return

    print('A e B são iguais')
    """

    nome = input('Informe o seu nome: ')

    nota1 = float(input('Informe a nota 1: '))
    nota2 = float(input('Informe a nota 2: '))
    nota3 = float(input('Informe a nota 3: '))

    media = (nota1 + nota2 + nota3) / 3

    if media <= 4.5:
        conceito = 'F'
    elif media <= 5.5:
        conceito = 'E'
    elif media <= 6.5:
        conceito = 'D'
    elif media <= 7.5:
        conceito = 'C'
    elif media <= 9.5:
        conceito = 'B'
    else:
        conceito = 'A'

    print(f" Conceito {conceito}")
    return


if __name__ == "__main__":
    main()
