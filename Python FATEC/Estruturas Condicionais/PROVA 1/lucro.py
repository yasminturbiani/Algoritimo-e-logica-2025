print("Yasmin Turbiani, 0220482523028")
custo = float(input("Qual o preço de custo do produto? "))
venda = float(input("Qual o preço de venda do produto? "))

lucro = venda - custo
print(f"Lucro: {lucro:.2f}")
margem = (lucro / custo) * 100
print(f"Margem: {margem:.2f}")

if margem > 30:
    print("Margem Excelente!")
elif 10 <= margem <= 30:
    print("Margem Satisfatória") 
else:
    print("Margem baixa: Avaliar preço de venda.")