
def pergunta_8():
    distancia_percorrida = float(input("Digite a distância total percorrida (em Km): "))
    combustivel_gasto = float(input("Digite o total de combustível gasto (em litros): "))

    if combustivel_gasto > 0:
        consumo_medio = distancia_percorrida / combustivel_gasto
        print("\n--- Resultado do Consumo ---")
        print(f"O consumo médio do automóvel foi de {consumo_medio:.2f} Km/l.")
    else:
        print("\nNão é possível calcular o consumo, pois a quantidade de combustível deve ser maior que zero.")

if __name__ == "__main__":
    pergunta_8()