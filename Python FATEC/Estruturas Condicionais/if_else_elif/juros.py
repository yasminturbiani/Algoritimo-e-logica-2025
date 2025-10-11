capital = float(input("Qual o valor do captal?" ))
taxaJuros = float(input("Qual o valor da taxa de juros?" ))
tempo = int(input("Qual o tempo em anos?" )) 

porcentJuros = taxaJuros/100
 
juros = (capital*porcentJuros)*tempo 
 
print (f"O valor dos juros é de {juros}")
print (f"O valor total é de {capital + juros}") 
print (porcentJuros)
 