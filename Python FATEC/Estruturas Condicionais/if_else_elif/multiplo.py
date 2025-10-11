n1 = int(input("Digite um número "))
n2 = int(input("Digite outro número "))

if n1%n2 == 0 and n2%n1 ==0:
    print("Os números são divisíveis entre si")
else:
    print("Os números não são divisíveis entre si")