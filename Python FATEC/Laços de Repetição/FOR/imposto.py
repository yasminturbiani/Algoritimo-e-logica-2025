
quantidade_dias = int(input("Digite a quantidade de dias que serão analisados: "))
vendas_totais = 0.0
for i in range(1, quantidade_dias + 1):
    valor_dia = float(input(f"Digite o valor das vendas do dia {i}: R$ "))
    vendas_totais += valor_dia

media_diaria = vendas_totais / quantidade_dias
if media_diaria > 1500:
    imposto_fixo = 200.00
else:
    imposto_fixo = 50.00

if vendas_totais > 10000:
    taxa_percentual = 0.08
else:
    taxa_percentual = 0.05

valor_taxa_servico = vendas_totais * taxa_percentual

valor_liquido = vendas_totais - valor_taxa_servico - imposto_fixo

print("\n--- RESUMO FINAL ---")
print(f"Valor total das vendas: R$ {vendas_totais:.2f}")
print(f"Imposto fixo aplicado: R$ {imposto_fixo:.2f}")
print(f"Taxa de serviço aplicada: {taxa_percentual * 100:.0f}%")
print(f"Valor líquido final da empresa: R$ {valor_liquido:.2f}")