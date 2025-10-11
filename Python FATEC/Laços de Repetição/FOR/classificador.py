print("--- Classificador de Paridade ---")
q = int(input("Digite um número para que eu possa definir todos os que são ímpares e todos os que são pares. "))

for numero in range(q+1):
    if numero % 2 == 0:
        print(f"{numero} é PAR.")
    else:
        print(f"{numero} é ÍMPAR.")

print("------------------------------------------")