#O objetivo do programa é calcular o custo total de um produto mediante o seu peso e destino. S

peso = float(input("Digite o peso do pacote em kg: "))
destino = input("Digite o destino ('local' ou 'nacional'): ").lower()

#O custo total é definido como zero, para depois assumir um valor diferente no comando. 
custo_total = 0.0

#Caso o destino seja definido como 'local', será atribuído a ele um valor base de 5.00
if destino == 'local':
    custo_base = 5.00

    #Ainda, se o peso for superior a 10, o código executará as seguintes expressões. 
    if peso > 10:
        excesso_peso = peso - 10
        custo_extra = excesso_peso * 2.00
        custo_total = custo_base + custo_extra

    #Caso o peso seja inferior a 10, o código assumirá o valor do custo base como custo total.
    else:
        custo_total = custo_base

    #Em ambas as situações, o código exibirá uma mensagem informando o custo total para o destino nacional. 
    print(f"O custo total do envio para o destino local é: R$ {custo_total:.2f}")

    
#Se o destino for definido como nacional, o código vai assumir o custo base como 15.00. 
else:  
    if destino == 'nacional':
        custo_base = 15.00

        #Ainda, se o peso for superior a 10, o código executará as seguintes expressões. 
        if peso > 10:
            excesso_peso = peso - 10
            custo_extra = excesso_peso * 5.00
            custo_total = custo_base + custo_extra

        #Caso o peso seja inferior a 10, o código assumirá o valor do custo base como custo total.    
        else:
            custo_total = custo_base

        #Em ambas as situações, o código exibirá uma mensagem informando o custo total para o destino nacional. 
        print(f"O custo total do envio para o destino nacional é: R$ {custo_total:.2f}")
    else:

        #Caso seja informado um destino diferente de 'local' ou 'nacional', o código exibirá a seguinte mensagem. 
        print("Erro: Destino inválido. Por favor, digite 'local' ou 'nacional'.")