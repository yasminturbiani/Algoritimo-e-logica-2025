print("Yasmin Turbiani, 0220482523028")

P = float(input("Digite o valor inicial do investimento (R$): "))
T = int(input("Digite o prazo do investimento em meses: "))

if T < 6:
    J = 0.005
elif 6 <= T <= 12:
    J = 0.008
else:
    J = 0.012

Rendimento_Total = P * J * T

print(f"Taxa de juros mensal aplicada: {J * 100}%")
print(f"Rendimento total após {T} meses: R$ {Rendimento_Total}")