quantidade_dias = int(input("Digite a quantidade de dias em que houve viagem: "))

total_km_percorridos = 0.0

for i in range(1, quantidade_dias + 1):
    km_dia = float(input(f"Digite os KM percorridos no dia {i}: "))
    total_km_percorridos += km_dia

km_por_litro = 12

preco_litro = 4.80

total_litros = total_km_percorridos / km_por_litro

custo_total = total_litros * preco_litro

print("\n--- RESUMO DA VIAGEM ---")
print(f"Total de KM percorridos: {total_km_percorridos:.2f} km")
print(f"Total de litros consumidos: {total_litros:.2f} L")
print(f"Custo total com combustível: R$ {custo_total:.2f}")

if custo_total > 500:
    print("Alerta de Gastos: O custo total com combustível foi alto (Acima de R$ 500,00).")
else:
    print("Gastos sob controle: O custo total com combustível foi baixo ou moderado.")