print("Yasmin Turbiani, 0220482523028")

peso = float(input("Digite o peso da encomenda (em kg): "))
distancia = float(input("Digite a distância da entrega (em km): "))


custo_base = (peso * 1.5) + (distancia * 0.25)


if custo_base > 200:
    custo_final = custo_base * 0.9  
elif 50 <= custo_base <= 200:
    custo_final = custo_base  
else:
    custo_final = custo_base + 5.00 

print(f"\nCusto base: R$ {custo_base}")
print(f"Custo final após ajustes: R$ {custo_final}")