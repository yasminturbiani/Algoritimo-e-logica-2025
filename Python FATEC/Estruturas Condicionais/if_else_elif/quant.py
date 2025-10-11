quantidade = int(input("Qual a quantidade? "))
preco = float(input("Qual o preço? "))

if quantidade >10:
    desconto = 0.15
else:
    desconto = 0.08

valor = quantidade*preco
pagar = valor - (valor*desconto)

print(f"O valor a ser pago é {pagar}")

#No programa em questão, caso a quantidade informada seja superior a 10, ele apliacará um desconto de 0.15.
#No entanto, se essa quantidade for inferior a 10. ele aplicará um desconto de 0.08.
#Por conseguinte, o sistema calculará o valor total e subtrairá o valor de desconto, resultando no que deve ser pago.