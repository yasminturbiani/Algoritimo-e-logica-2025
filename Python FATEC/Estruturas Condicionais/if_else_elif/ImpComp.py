print("Vamos calcular o valor da sua compra!!")

valor_produto = float(input("Qual o valor do produto? "))
porcentagem_imposto = float(input("Qual é o percentual de imposto? "))

valor_imposto = valor_produto * (porcentagem_imposto / 100)

valor_total = valor_produto + valor_imposto

print(f"O valor final da compra é {valor_total} reais")
