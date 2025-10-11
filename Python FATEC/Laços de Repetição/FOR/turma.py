quant = int(input("Qual a quantidade de alunos na turma? "))
soma_das_notas =0
for i in range (quant):
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    soma_das_notas = soma_das_notas + nota

media = soma_das_notas / quant

print(f"A média da turma é: {media:}")