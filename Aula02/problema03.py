# Problema 03
# Três pontos na mesma reta (colinearidade) via determinante (Sarrus)

def sao_colineares(ponto_a, ponto_b, ponto_c) -> bool:
    x1, y1 = ponto_a
    x2, y2 = ponto_b
    x3, y3 = ponto_c
    det = x1 * y2 * 1 + y1 * 1 * x3 + 1 * x2 * y3 - (y1 * x2 * 1 + x1 * 1 * y3 + 1 * y2 * x3)
    return det == 0

def main():
    try:
        print("Digite as coordenadas do ponto A (x1, y1)")
        ponto_a_x1 = int(input("x1: "))
        ponto_a_y1 = int(input("y1: "))
        print("Digite as coordenadas do ponto B (x2, y2)")
        ponto_b_x2 = int(input("x2: "))
        ponto_b_y2 = int(input("y2: "))
        print("Digite as coordenadas do ponto C (x3, y3)")
        ponto_c_x3 = int(input("x3: "))
        ponto_c_y3 = int(input("y3: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    if sao_colineares((ponto_a_x1, ponto_a_y1), (ponto_b_x2, ponto_b_y2), (ponto_c_x3, ponto_c_y3)):
        print("São colineares. Parabéns, você acertou o alvo!")
    else:
        print("Não são colineares. Que mira ruim!")


if __name__ == "__main__":
    main()
