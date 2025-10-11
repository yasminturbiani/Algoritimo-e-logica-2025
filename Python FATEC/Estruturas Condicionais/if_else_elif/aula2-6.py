valor = int(input("Qual o valor do produto? "))

porcentagem = int(input("Qual o valor do desconto? "))

desconto = valor * (porcentagem/100)

print(f"O valor do seu desconto é de {desconto}")
print (f"O valor final é de {valor- desconto}")