renda = float(input("Qual a sua renda mensal? "))
score = int(input("Qual o seu score de crédito? "))
tempo = int(input("Quanto tempo você trabalha nessa empresa? "))

if renda >3000 and tempo>=2:
    if 700 <= score <= 1000:
        print("Empréstimo aprovado com taxa de juros baixa!")
    else:
        print("Empréstimo aprovado com taxa de juros alta. Score de crédito insuficiente.")
else:
    print("Não elegível: Renda ou tempo de trabalho insuficientes.")