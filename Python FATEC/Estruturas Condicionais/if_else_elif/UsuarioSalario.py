

salario = float(input("Qual é o seu salário? "))

if salario < 5000:
    imposto = round(salario*0.27 ,2)
else:
    imposto = round(salario*0.27 ,2)

print(f"O valor do imposto é {imposto} reais ")