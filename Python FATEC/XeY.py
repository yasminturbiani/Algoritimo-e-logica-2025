a = float (input ("Qual o valor de a? "))
b = float (input ("Qual o valor de b? "))
c = float (input ("Qual o valor de c? "))
d = float (input ("Qual o valor de d? "))
e = float (input ("Qual o valor de e? ")) 
f = float (input ("Qual o valor de f? "))

x = (((c*e) - (b*f)) / ((a*e)-(b*d)))
y = (((a*f) - (c*d)) / ((a*e) - (b*d)))

print(f"O valor de x é {x}")
print(f"O valor de y é {y}")