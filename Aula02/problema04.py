# Problema 04
# Trocar o valor de duas variáveis sem variável auxiliar.

def main():
    try:
        a = int(input("A = "))
        b = int(input("B = "))
    except (ValueError, EOFError):
        print("O valor informado não é válido.")
        return

    print("\nANTES")
    print(f"A = [{a}] e B = [{b}]")

    a = a + b
    b = a - b
    a = a - b

    print("DEPOIS")
    print(f"A = [{a}] e B = [{b}]")

if __name__ == "__main__":
    main()
