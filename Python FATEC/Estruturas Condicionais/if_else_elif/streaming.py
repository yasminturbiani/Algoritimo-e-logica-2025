
tipo_plano = input("Qual é o seu plano de streaming? (premium, padrão ou básico): ").lower()
tempo_assinatura = int(input("Há quantos meses você é assinante?: "))
compartilhada = input("Você compartilha a sua conta com alguém? (sim ou não): ").lower()

if tipo_plano == 'premium' and tempo_assinatura >= 24:
    print("Você é um cliente premium de longa data: 25% de desconto vitalício!")
elif tipo_plano == 'padrão' and tempo_assinatura > 12 and compartilhada == 'não':
    print("Você atende aos critérios para um desconto de 15%.")
elif tipo_plano == 'básico' and tempo_assinatura > 6:
    print("Sua lealdade merece um reconhecimento: 5% de desconto na próxima fatura.")
else:
    print("Nenhum desconto disponível no momento para o seu perfil.")