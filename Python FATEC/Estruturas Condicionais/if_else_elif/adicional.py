salario = float(input("Qual é o salário? "))
horas = int(input("Quantas são as horas? "))

if salario > 5000 and horas < 40:
    adicional = 0.15
else:
    adicional = 0.18

sal_final = (salario + (salario * adicional))  + horas * 20

print (f"O salário final é {sal_final}" )

