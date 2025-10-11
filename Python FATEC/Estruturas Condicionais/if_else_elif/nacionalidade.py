idade =  int(input("Qual a sua idade? "))

if idade >= 60:
    nacionalidade = input("Qual a sua nacionalidade? ")
    if nacionalidade == "brasileiro":
        print("Você tem direito a um desconto especial!")
    else:
        print("Você tem direito a um desconto padrão!")
else:
    print("Você não tem direito a desconto!")
    