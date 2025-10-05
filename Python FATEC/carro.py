custo = float(input ("Qual o valor de fábrica do carro? "))
distribuidor = float(input("Qual a porcentagem do distribuidor?"))
impostos = float (input ("Qual a porcentagem dos impostos? "))

Cdistribuidor = (custo*(distribuidor/100))
Cimposto = ((custo + Cdistribuidor)*(impostos/100))

final = (custo + Cdistribuidor + Cimposto)

print(f"O custo final do carro é {final}")