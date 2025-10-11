import math
 
lado_a = float(input("Digite o lado a: "))
lado_b = float(input("Digite o lado b: "))
lado_c = float(input("Digite o lado c: "))
 
# Determina qual é o maior lado e reatribui a, b e c
if lado_a >= lado_b and lado_a >= lado_c:
    c = lado_a
    a = lado_b
    b = lado_c
elif lado_b >= lado_a and lado_b >= lado_c:
    c = lado_b
    a = lado_a
    b = lado_c
else:
    c = lado_c
    a = lado_a
    b = lado_b
 
if a + b <= c:
    print("Não é um triângulo.")
else:
    cosseno_gama = (a**2 + b**2 - c**2) / (2 * a * b)
 
    # Garante que o valor do cosseno esteja entre -1 e 1
    cosseno_gama = min(1, max(-1, cosseno_gama))
 
    angulo_gama = math.degrees(math.acos(cosseno_gama))
 
# A função math.isclose() serve para comparar dois números decimais (float)e verificar se eles são "praticamente iguais", permitindo uma pequena margem de erro.
 
# abs_tol define a "tolerância absoluta"
 
# 1e-5 é a notação científica para o número 0.00001, ou seja, 1e-5 = 1 × 10⁻⁵ = 0.00001
    if math.isclose(angulo_gama, 90, abs_tol=1e-5):
        print("Triângulo Retângulo")
    elif angulo_gama < 90:
        print("Triângulo Acutângulo")
    else:
        print("Triângulo Obtusângulo")