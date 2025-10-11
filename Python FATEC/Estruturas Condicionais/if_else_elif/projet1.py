s = float(input("Informe o salário: "))

if s <5000:
    imposto = 0.12*s
    print("Valor do imposto: ", imposto)
elif s>5000 and s<7500:
    imposto = 0.17*s
    print("Valor do imposto: ", imposto)
elif s>=7500 and s< 8900:
    imposto = 0.22*s
    print("Valor do imposto: ", imposto)
else:
    imposto = 0.27*s
    print("Valor do imposto: ", imposto)