print("Yasmin Turbiani, 0220482523028")

pureza = float(input("Digite a pureza do lote em decimal: "))
massa_total = float(input("Digite a massa total do lote (kg): "))
taxa_contaminacao = float(input("Digite a taxa de contaminação  em decimal: "))

FD = (pureza * 100) - (taxa_contaminacao * 50)

if massa_total > 1000:
    P_base = 10.00
else:
    P_base = 12.50

if FD > 90 and pureza > 0.98:
    classificacao = "PREMIUM (Venda Imediata)"
    P_final_kg = P_base * 1.50  
elif 70 <= FD <= 90 and taxa_contaminacao < 0.05:
    classificacao = "PADRÃO (Venda Normal)"
    P_final_kg = P_base * 1.10  
elif FD < 70 or pureza < 0.90:
    classificacao = "REPROVADO (Descarte ou Re-processamento)"
    P_final_kg = P_base * 0.25 
else:
    classificacao = "ACEITÁVEL (Margem Mínima)"
    P_final_kg = P_base * 0.90  

preco_total_final = P_final_kg * massa_total

print(f"Preço Base por kg: R$ {P_base}")
print(f"Classificação: {classificacao}")
print(f"Preço Final por kg: R$ {P_final_kg}")
print(f"Preço Total Final do lote: R$ {preco_total_final}")
