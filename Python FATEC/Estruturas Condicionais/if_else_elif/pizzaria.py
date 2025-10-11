
tamanho_pizza = input("Informe o tamanho da pizza ('pequena', 'média' ou 'grande'): ").lower()
numero_sabores = int(input("Informe o número de sabores (número inteiro): "))
status_cliente = input("Informe o status do cliente ('vip' ou 'normal'): ").lower()


if tamanho_pizza == 'grande' and numero_sabores > 2:
    print("Pedido especial: sujeito a taxa extra.")
elif tamanho_pizza == 'grande' or status_cliente == 'vip':
    print("Pedido prioritário: prepare para entrega rápida.")
elif tamanho_pizza == 'média' and numero_sabores == 1:
    print("Pedido padrão: processamento normal.")
else:
    print("Pedido de baixo volume: pode ser processado a qualquer momento.")