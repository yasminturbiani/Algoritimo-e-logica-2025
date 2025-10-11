print("Yasmin Turbiani, 0220482523028")

R_investimento = float(input("Digite o retorno do investimento em decimal : "))
R_livre = float(input("Digite a taxa livre de risco em decimal : "))
Sigma = float(input("Digite o desvio-padrão da volatilidade em decimal : "))

if Sigma == 0:
    print("O desvio-padrão (Sigma) não pode ser zero para calcular o Sharp Ratio.")
else:
    Sharp = (R_investimento - R_livre) / Sigma
    Spread = R_investimento - R_livre

    if Sharp > 1.5 and Spread > 0.05:
        classificacao = "Investimento Excelente: Alta performance ajustada ao risco."
    elif 0.5 <= Sharp <= 1.5 or Spread > 0.02:
        classificacao = "Investimento Bom: Risco e retorno moderados."
    elif Sharp < 0.5 and R_investimento > 0:
        classificacao = "Investimento Aceitável: Retorno positivo, mas risco alto para o ganho."
    else:
        classificacao = "Investimento Ruim: Não recomendado."

    print(f"Sharp Ratio: {Sharp}")
    print(f"Classificação: {classificacao}")