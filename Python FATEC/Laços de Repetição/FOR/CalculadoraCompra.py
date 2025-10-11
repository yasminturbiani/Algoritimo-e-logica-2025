quant = int(input("Digite a quantidade de produtos diferentes que irá comprar: "))
total_da_compra =0.0
for i in range(quant):
    preco = float(input(f"Digite o preço do {i + 1}º produto: R$ "))
    total_da_compra += preco 

print(f"O total a pagar é: R$ {total_da_compra:.2f}")
