print("Yasmin Turbiani, 0220482523028")

C_inicial = float(input("Qual o custo inicial do produto? "))
q = int(input("Qual a quantidade de itens produzidos? "))
dias = int(input("Quantos são os dias de atrasos? "))
defeito = float(input("Qual o percentual de defeitos"))

if q > 1000 and C_inicial > 5000:
    F_comp = 1.15
else:
    F_comp = 1.05

C_corrigido = C_inicial * F_comp

if defeito > 0.10 or dias > 5:
    print("Penalidade Alta: 20% de redução no lucro.")
    C_final = C_corrigido * 1.25
    print(f"O custo final é: {C_final}")

elif 0.05 <= defeito <= 0.10 and dias > 0:
    print("Penalidade Média: 10% de redução no lucro.")
    C_final = C_corrigido * 1.10
    print(f"O custo final é: {C_final}")

else: 
    print("Sem penalidade. Custo final apenas com correção.")
    C_final = C_corrigido
    print(f"O custo final é: {C_final}")