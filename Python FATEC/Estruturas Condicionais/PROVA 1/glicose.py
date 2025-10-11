print("Yasmin Turbiani, 0220482523028")

glicose = float(input("Digite o valor da glicose em jejum (mg/dL): "))


if glicose < 100:
    print("Glicemia Normal.")
elif 100 <= glicose <= 125:
    print("Pré-diabetes: Risco Moderado.")
else: 
    print("Diabetes: Nível Alto.")