"""Desafio 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

from time import sleep

retasLista=[]
retas={"Retas":retasLista}

print(f"{color1}Bem vindo ao calculador de triangulo da Alexa!{colorEnd}")

while True:        
    for n in range(3):    
        numeros=float(input(f"Digite o {n+1}º numero: (Ou digite 999 para sair)"))
        retasLista.append(numeros)
    
        if numeros==999:
            print(f"{color1}Obrigado e volte sempre!")
            quit()   
    
    if retas["Retas"][0]<retas["Retas"][1]+retas["Retas"][2] and retas["Retas"][1]<retas["Retas"][0]+retas["Retas"][2] and retas["Retas"][2]<retas["Retas"][1]+retas["Retas"][0]:
        print(f"{color1}Pode formar um triangulo.{colorEnd}")
        retasLista.clear()
        sleep(1)
    else:
        print(f"{color2}Não pode formar um triangulo.{colorEnd}")
        retasLista.clear()
        sleep(1)




