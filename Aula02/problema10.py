# Problema 10
# Distância Manhattan entre dois pontos (X1, Y1) e (X2, Y2): |X1-X2| + |Y1-Y2|

def manhattan(origem_ponto_x1, origem_ponto_y1, destino_ponto_x2, destino_ponto_y2) -> int:
    return abs(origem_ponto_x1 - destino_ponto_x2) + abs(origem_ponto_y1 - destino_ponto_y2)


def main():
    try:
        origem_ponto_x1 = int(input("X1: "))
        origem_ponto_y1 = int(input("Y1: "))
        destino_ponto_x2 = int(input("X2: "))
        destino_ponto_y2 = int(input("Y2: "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    distancia = manhattan(origem_ponto_x1, origem_ponto_y1, destino_ponto_x2, destino_ponto_y2)
    print(f"Distância Manhattan: {distancia}")


if __name__ == "__main__":
    main()
