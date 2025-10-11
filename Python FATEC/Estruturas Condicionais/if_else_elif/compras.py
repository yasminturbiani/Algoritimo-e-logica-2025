total_compra = float(input("Qual o valor total da compra? "))
status_cliente = input("O cliente é 'novo' ou 'fiel'? ").lower()
tipo_produto = input("O produto é 'eletrônico' ou 'livro'? ").lower()


if total_compra >= 200 and status_cliente == "fiel":
    print("Parabéns! Você tem direito a frete grátis e um brinde especial.")
elif total_compra  >= 200 or tipo_produto =="livro":
    print("Você tem direito a frete grátis. Aproveite!")
elif status_cliente =="fiel" and tipo_produto =="eletrônico":
    print("Você tem direito a um desconto de 5% no frete.")
else:
    print("Não há promoções aplicáveis a este pedido.")