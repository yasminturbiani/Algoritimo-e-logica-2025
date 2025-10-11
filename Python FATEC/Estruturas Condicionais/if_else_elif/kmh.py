print("Vamos calcular quanto tempo da sua viagem!!")

distancia = float(input("Qual a distancia a ser percorrida em Km? "))
velocidade = float(input("Qual a velocidade média ultilizada no trajeto em Km/h? "))

tempo = distancia/velocidade

print(f"O tempo da sua viagem será de {tempo} horas")

horas = tempo*60

print(f"Ou seja {horas} minutos")