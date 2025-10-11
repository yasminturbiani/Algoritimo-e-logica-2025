sb = float(input("Qual o valor do salário bruto? "))

horaExtra = int(input("Quantas horas extras foram feitas? "))

descontos = sb * 0.08
imposto = sb *0.15

salario = sb - descontos + (horaExtra * 22.19) - imposto
print(f"Seu salário final é de: {salario}")
