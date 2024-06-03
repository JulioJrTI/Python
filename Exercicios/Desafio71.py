"""Desafio 71: Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues.

OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

print(f"{c1}Bem vindo ao internet banking da Alexa!{c0}")

while True:
    try:
        dinheiro = int ( input ("Quanto deseja sacar: R$" ) )        
        if dinheiro<=0:
            print("Por favor digite somente valores positivos.")
        else:
            break    
    except:
        print(f"Erro! Digite somente valores em R$")  

while True:
    totalBanco = dinheiro  
    cedula = 50  
    cedulaTotal = 0  

    while True :
        if totalBanco >= cedula : 
            totalBanco -= cedula 
            cedulaTotal += 1 
        else :
            if cedulaTotal > 0 : 
                print ( f"Foi retirado {cedulaTotal} notas de R${cedula}" ) 
            if cedula == 50 : 
                cedula = 20 
            elif cedula == 20 : 
                cedula = 10 
            elif cedula == 10 : 
                cedula = 1 
            cedulaTotal = 0 
            if totalBanco == 0 : 
                break
    
    c=str(input("Deseja efetuar nova retirada? [S/N]")).upper()[0]

    if c in "Nn":
        print("Obrigado e volte sempre!")
        break