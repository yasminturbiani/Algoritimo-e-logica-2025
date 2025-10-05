numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")

# Laço de repetição FOR
# O laço for é utilizado para repetir um bloco de instruções um número determinado de vezes.
# Ele percorre uma sequência (como uma faixa de números, lista ou texto),
# executando o código interno para cada elemento dessa sequência.
# No Python, a função range() é frequentemente usada para definir o intervalo de repetição.
for i in range(1, 11):  # vai de 1 até 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    