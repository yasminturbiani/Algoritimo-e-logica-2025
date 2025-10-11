quantidade_dias = int(input("Digite a quantidade de dias que serão analisados: "))

soma_das_temperaturas = 0.0

for i in range(1, quantidade_dias + 1):
    temp = float(input(f"Digite a temperatura do dia {i} em °C: "))
    soma_das_temperaturas += temp

media_temperatura = soma_das_temperaturas / quantidade_dias

print("\n--- RESULTADO ---")
print(f"Temperatura média do período: {media_temperatura:.2f}°C")

if media_temperatura > 28:
    print("Média de temperatura: Clima Quente.")
elif 18 <= media_temperatura <= 28:
    print("Média de temperatura: Clima Agradável.")
else:
    print("Média de temperatura: Clima Frio.")