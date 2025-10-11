A = int(input("Digite um número "))
B = int(input("Digite outro número "))
print(f"A soma dos números escolhidos foi: {A + B}")
print(f"A subtração dos números escolhidos foi: {A - B}")
print(f"A multiplicação dos números escolhidos foi: {A * B}")
print(f"A divisão dos números escolhidos foi: {A/B}")

if(B>0):
    print(f"O resultado da divisão entre {A} e {B} é {A/B} ")
else:
    print("Para obter o valor da divisão, o número escolhido deve ser diferente de 0")
    