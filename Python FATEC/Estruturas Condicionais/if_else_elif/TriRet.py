cateto1 = float(input("Qual a medida do cateto 1? "))
cateto2 = float(input("Qual a medida do cateto 2? "))

hipotenusa = (cateto1*2 + cateto2*2)*0.5

if hipotenusa > 180:
    print("O triângulo deve ser refeito para ser compatível com a proposta")
else:
    print("Triângulo aceito deve ser incluído na proposta")

print("FIM")