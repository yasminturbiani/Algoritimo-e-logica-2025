plano = input("Digite seu plano de assinatura ('básico', 'padrão' ou 'premium'): ")
tempo_uso = int(input("Digite o tempo de uso do serviço (em meses): "))
 
if plano == 'padrão' or plano == 'premium':
    if 12 <= tempo_uso <= 24:
        print("Parabéns! Você tem direito a um desconto de 15%.")
    else:
        print("Seu plano é elegível, mas você não atende ao tempo de uso necessário para o desconto.")
else:
    print("Seu plano não é elegível para este desconto.")