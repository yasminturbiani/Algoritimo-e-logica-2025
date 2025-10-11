idade = int(input("Qual a sua idade? "))
experiencia = float(input("Você tem quantos anos de experiência em programação? "))
turno = input("Tem disponibilidade de horário? (manhã ou tarde)? ")

if idade > 18 and experiencia > 1:
    if turno == 'manhã' or turno == 'tarde':
        print("Parabéns! Você é elegível para a vaga!")
    else:
        print("Não elegível: Disponibilidade não corresponde aos requisitos.")
else:
    print("Não elegível: Idade ou experiência insuficientes.")