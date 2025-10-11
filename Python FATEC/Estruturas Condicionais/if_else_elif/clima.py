temperatura = float(input("qual a temperatura atual?  "))
chuva = input("está chovendo? ")
 
if temperatura > 20 and chuva == "não":
    print("o tempo está ideal para sair")
elif 15 <= temperatura <= 20 or chuva == "sim":
    print("a temperatura nao está boa para sair")
else:
    print("o tempo nao está ideal para atividade ao ar livre")