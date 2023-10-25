"""Desafio 28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;31m"
colorEnd="\033[m"

maquinaLista=[]

print(f"{color1}Bem vindo ao game de adivinhação da Alexa!{colorEnd}")
while True:    
    maquina=randint(0,5)
    maquinaLista.append(maquina)

    player=int(input("Digite um numero entre 0 e 5: "))

    if player>5:
        print(f"{color3}Numero invalido, por favor digite um numero entre 0 e 5!{colorEnd}")
        maquinaLista.clear()
    else:
        print("A maquina está pensando em um numero...")
        sleep(2)

        print(f"O player escolheu o numero [{player}].")
        sleep(2)
        print(f"A maquina escolheu o numero {maquinaLista}.")

        if player==maquinaLista[0]:
            print(f"{color1}Vc venceu!{colorEnd}")
        else:
            print(f"{color3}Vc perdeu!{colorEnd}")

        c=str(input("Deseja jogar novamente? [S/N]"))

        if c in "Ss":
            maquinaLista.clear()
        elif c in "Nn":
            print(f"{color2}Obrigado e volte sempre!{colorEnd}")
            break


