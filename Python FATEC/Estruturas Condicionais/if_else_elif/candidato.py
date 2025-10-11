experiencia = int(input("Possui quantos anos de experiência com vendas? "))
habilidade= int(input("Em uma escala de 0 a 10, em quanto você classificaria sua habilidade de comunicação? "))
disponibilidade = input("Possui disponibilidade de horário? (Integral ou meio-período) ").lower

if experiencia >2 and habilidade >8:
    print("Candidato classificado como Sênior. Entra na próxima etapa para vaga integral.")
elif experiencia >2 and habilidade >6:
    print("Candidato classificado como Sênior. Entra na próxima etapa para vaga de meio período.")
elif experiencia >1 and habilidade >8 and disponibilidade == "meio-período":
    print("Candidato classificado como Pleno. Entra na próxima etapa para vaga de meio período.")
elif experiencia >1 and habilidade >8 and disponibilidade == "integral":
    print("Candidato classificado como Pleno. Entra na próxima etapa para vaga integral.")
elif habilidade >7 and disponibilidade == "meio-período":
    print("Candidato classificado como Júnior. Entra na próxima etapa para vaga de meio período.")
elif habilidade >7 and disponibilidade == "integral":
    print("Candidato classificado como Júnior. Entra na próxima etapa para vaga integral.")
else: 
    print("Candidato não classificado. Não atende aos requisitos mínimos.")