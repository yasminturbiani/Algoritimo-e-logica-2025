
tempo = float(input("Qual foi o tempo final do atleta (em segundos)? "))
penalidade = input("O atleta recebeu alguma penalidade? (sim ou não): ").lower()
classificacao_equipe = input("Qual foi a classificação da equipe? (ouro, prata ou bronze): ").lower()

if tempo < 10.0 and penalidade == 'não':
    print("Desempenho excelente: novo recorde pessoal.")
elif tempo < 12.0 or classificacao_equipe == 'ouro':
    print("Desempenho forte: classificado para a próxima fase.")
elif tempo >= 12.0 and penalidade == 'não':
    print("Desempenho regular: precisa de mais treinamento.")
else:
    print("Desempenho insuficiente: desclassificado.")