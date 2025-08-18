# Problema 03
# Três pontos na mesma reta (colinearidade) via determinante (Sarrus)

def sao_colineares(p1, p2, p3) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    det = x1 * y2 * 1 + y1 * 1 * x3 + 1 * x2 * y3 - (y1 * x2 * 1 + x1 * 1 * y3 + 1 * y2 * x3)
    return det == 0

def main():
    try:
        print("Digite as coordenadas de A (x1, y1)")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        print("Digite as coordenadas de B (x2, y2)")
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        print("Digite as coordenadas de C (x3, y3)")
        x3 = int(input("x3: "))
        y3 = int(input("y3: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    if sao_colineares((x1, y1), (x2, y2), (x3, y3)):
        print("São colineares. Parabéns, você acertou o alvo!")
    else:
        print("Não são colineares. Que mira ruim!")


if __name__ == "__main__":
    main()
