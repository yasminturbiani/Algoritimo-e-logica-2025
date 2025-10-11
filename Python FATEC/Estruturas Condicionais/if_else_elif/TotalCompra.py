total_compra = float(input("Qual o valor total da compra? "))

if total_compra > 100.00:
    total_compra = total_compra - (total_compra *0.05)
    if total_compra > 150.00:
        total_compra = total_compra - (total_compra *0.02)
        print(f"O valor do produto com o desconto é de {total_compra}")

    else:
        print(f"O valor do produto com o desconto é de {total_compra}")
else:
    print("Nenhum desconto foi aplicado. ")
