distancia = float(input("Qual é a distância? "))
velocidade = float(input("Qual a velocidade? "))

tempo = distancia / velocidade

if tempo >4:
    print("Viagem demorada, utilizar veículo sedan")
else:
    print("Viagem rápida, utilizar veículo hatch")

print("FIM")