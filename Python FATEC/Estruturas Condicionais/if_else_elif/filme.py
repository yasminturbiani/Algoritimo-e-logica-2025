idade = int(input("Qual a sua idade? "))
genero = input("Qual o gênero? (Terror ou Ação) ").lower()

if idade < 18 and genero == "Terror":
    print("Este filme não é recomendado para sua idade devido ao gênero.")
elif idade < 16 and genero == "Ação":
    print("Este filme de ação não é adequado para sua faixa etária.")
elif idade >= 18 or genero == "Ação":
    print("Recomendado para você: assistir o filme.")
else:
    print("Não há recomendações para este filme ou idade.")