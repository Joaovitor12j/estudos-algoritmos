def pergunta_2():
    celsius = float(input("Digite a temperatura em graus Celsius (C°): "))

    fahrenheit = (9 * celsius + 160) / 5

    print("\n--- Resultado ---")
    print(f"A temperatura de {celsius}°C equivale a {fahrenheit:.1f}°F.")

if __name__ == "__main__":
    pergunta_2()