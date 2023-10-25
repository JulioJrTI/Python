"""Desafio 45: Crie um programa que faça o computador jogar Pedra/Papel/Tesoura com voce."""

import random
from time import sleep

color1="\033[1;32m"
color2="\033[1;31m"
color3="\033[1;33m"
colorEnd="\033[m"
enfeite="-="*10

items=["Pedra","Papel","Tesoura"]
itemsNum={1:"Pedra",2:"Papel",3:"Tesoura"}
loops=0

print(f"{color1}Bem vindo ao game da Alexa!{colorEnd}")
while True:
    print("Faça sua escolha:")
    playerNum=int(input("[1]Pedra, [2]Papel ou [3]Tesoura: "))
    player=itemsNum.get(playerNum)

    maquina=random.choice(items)

    print(f"{color1}Player escolheu:",player)
    sleep(1)
    print(f"{color2}Maquina escolheu:",maquina)

    print(enfeite)
    if player==maquina:
        print(f"{color3}Empate{colorEnd}")
    elif (player=="Pedra" and maquina=="Tesoura") or (player=="Tesoura" and maquina=="Papel") or (player=="Papel" and maquina=="Pedra"):
        print(f"{color1}Player venceu{colorEnd}")
        sleep(1)
        loops+=1
    else:
        print(f"{color2}Maquina venceu{colorEnd}")
        sleep(1)
        loops+=1
    print(enfeite)
    
    if loops==5:
        c=str(input("Deseja continuar? [S/N]"))

        if c in "Nn":
            print(f"{color1}Obrigado e volte sempre!{colorEnd}")
            break
