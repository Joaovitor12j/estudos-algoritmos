# Problema 09
# Solicitar três números inteiros positivos e indicar se são lados de um triângulo retângulo.
# Se forem, exibir também a área correspondente.

def triangulo(lado1, lado2, lado3) -> bool:
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1


def retangulo(lado1, lado2, lado3) -> bool:
    lados = sorted([lado1, lado2, lado3])  # lado3 será a maior (hipotenusa)
    x, y, z = lados
    return x * x + y * y == z * z


def area_triangulo_retangulo(lado1, lado2, lado3) -> float:
    lados = sorted([lado1, lado2, lado3])
    x, y, z = lados
    # catetos são x e y
    return x * y / 2.0


def main():
    try:
        lado1 = int(input("Lado 1: "))
        lado2 = int(input("Lado 2: "))
        lado3 = int(input("Lado 3: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Entrada inválida: os lados devem ser positivos.")
        return

    if not triangulo(lado1, lado2, lado3):
        print("Os lados não formam um triângulo.")
        return

    if retangulo(lado1, lado2, lado3):
        print("É um triangulo retângulo.")
        area = area_triangulo_retangulo(lado1, lado2, lado3)

        # mostrar área sem casas desnecessárias
        if abs(area - round(area)) < 1e-9:
            print(f"Área: {int(round(area))}")
            return
        print(f"Área: {area:.6f}")
        return

    print("Não é um triangulo retângulo.")


if __name__ == "__main__":
    main()
