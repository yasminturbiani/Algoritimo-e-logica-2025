largura = float(input("Qual é a medida da lagura do terreno? "))
comprimento = float(input("Qual é a medida do comprimento do terreno? "))

perimetro = 2 * (largura + comprimento)

if perimetro >16:
    print("Aprovar alteração do cadastro!")
else:
    print("Reprovar alteração do cadastro!")

