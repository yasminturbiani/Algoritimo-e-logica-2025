vendas = float(input("Qual foi o volume de vendas total no mês? (em R$) "))
satisfacao = float(input("Qual foi a taxa de satisfação do cliente? (de 0.0 a 1.0) "))
meta_clientes = input("A meta de novos clientes foi atingida? (sim ou não) ").lower()

if vendas >= 50000 and satisfacao > 0.9:
    print("Vendedor de alta performance: classificado como Sênior.")
elif vendas >= 30000 and meta_clientes == "sim":
    print("Vendedor de bom desempenho: classificado como Pleno.")
elif satisfacao > 0.8 or meta_clientes == "sim":
    print("Vendedor em desenvolvimento: classificado como Júnior.")
else:
    print("Vendedor em revisão de desempenho: não atende aos critérios mínimos.")