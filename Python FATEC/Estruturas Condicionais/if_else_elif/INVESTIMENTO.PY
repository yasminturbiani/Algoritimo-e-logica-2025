valor_futuro = float(input("Qual o valor de rendimentos somados aos invetimentos? "))
taxa_juros = float(input("Qual taxa foi aplicada? "))
anos = int(input("Por quantos anos esse dinheiro está rendendo? "))

valor_presente = valor_futuro / ((1 + (taxa_juros/100))*anos)

print(f"O valor de investimento foi de {round(valor_presente ,2)}")

if valor_presente <30000:
    print("valor deve ser investido em bens não duráveis")
else: 
    print("valor deve ser investido em renda fixa superior a 24")

print("FIM")