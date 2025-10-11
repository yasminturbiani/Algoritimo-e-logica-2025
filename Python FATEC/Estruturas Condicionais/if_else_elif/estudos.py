media_academica = float(input("Qual a sua média acadêmica em uma escala de 0 a 10? "))
habilidade_escrita = int(input("Qul a sua habilidade em escrita em uma escala de 0 a 5? "))
necessidade_financeira = input("Possui neceiddade financeira? (Sim ou Não) ").lower()

if media_academica >= 9.0 and habilidade_escrita>= 4:
    print( "Parabéns! Você é elegível para a bolsa de mérito acadêmico.")
elif media_academica >= 8.0 and necessidade_financeira =="sim":
    print( "Parabéns! Você é elegível para a bolsa de necessidade financeira.")
elif media_academica >= 7.0 and habilidade_escrita >= 3 and necessidade_financeira =="sim":
    print("Parabéns! Você é elegível para a bolsa combinada de mérito e necessidade.")
elif media_academica >= 7.0 and habilidade_escrita >= 3:
    print("Você é elegível para a bolsa de necessidade, mas sua média e habilidade em escrita são requisitos.")
else:
    print("Infelizmente, você não atende aos critérios de elegibilidade para bolsa.")
