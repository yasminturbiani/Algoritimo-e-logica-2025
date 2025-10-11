import math as m

x1 =int(input("Escolha um valor para x1: "))
y1 =int(input("Escolha um valor para y1: "))
x2 =int(input("Escolha um valor para x2: "))
y2 =int(input("Escolha um valor para y2: "))

distancia = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"A distância entre os dois pontos é {distancia}")

