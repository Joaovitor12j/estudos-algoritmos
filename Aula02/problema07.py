# Problema 07
# Mostrar os números primos entre 1 e 500 (inclusive).

def verificar_primo(numero: int) -> bool:
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    impares = 3
    while impares * impares <= numero:
        if numero % impares == 0:
            return False
        impares += 2
    return True


def main():
    primos = [str(numero) for numero in range(1, 501) if verificar_primo(numero)]
    # Mostra um número por linha
    print("\n".join(primos))


if __name__ == "__main__":
    main()
