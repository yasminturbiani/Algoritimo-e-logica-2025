salario_fixo = float(input("Qual é o salárioi do vendedor? "))
comissao_produto = float(input("Qual é o valor da comissão por produto? "))
quantidade_produtos = float(input("Qual é a quantidade de produtos vendidos? "))

salario_total = salario_fixo + (comissao_produto * quantidade_produtos)

print(f"O salário final do vendedor é {salario_total} reais ")