ingresso = input("Qual o tipo do seu ingresso? (Padrão ou Premium)").lower()
idade = int(input("Qual a sua idade? "))
vip = input("Está na lista de convidados VIP? (Sim ou Não)").lower()

if ingresso == "Premium":
    print("Acesso total: todas as áreas e benefícios especiais.")
elif idade >=18 and vip == "Sim":
    print("Acesso VIP: área exclusiva e entrada prioritária.")
elif idade >=18 or ingresso  == "Padrão":
    print( "Acesso padrão: entrada para a área principal do evento.")
else:
    print("Acesso negado: verifique os critérios de entrada.")