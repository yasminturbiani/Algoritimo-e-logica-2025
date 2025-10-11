salario_fixo = float(input("Qual é o valor do salário? "))
comissao_produto = float(input("Qual é a comissão em cima de cada produto? "))
quantidade_produtos = float(input("Qual a quantidade de produtos? "))

salario_total = salario_fixo + (comissao_produto * quantidade_produtos)

if salario_total < 5000:
    imposto = salario_total*0.16
else:
    imposto = salario_total*0.27

print(f"O valor do imposto refernte ao salário é de {imposto}")

print("FIM")