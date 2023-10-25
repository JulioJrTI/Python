"""Desafio 58: Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer."""

from random import randint
from time import sleep

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

maquina=randint(0,10)

palpites=0

print(f"{c1}Bem vindo ao jogo de adivinhação da Alexa!{c0}")
while True:
    player=int(input("Digite um numero: "))
    print("A maquina está pensando...")
    sleep(3)

    print("-="*10)
    print(f"Voce escolheu o numero {player}.")
    sleep(1)    
    print("-="*10)

    if player==maquina:
        palpites+=1
        print(f"{c1}Vc ganhou!{c0}",end="")
        print(f" e foram necessarias {palpites} tentativas para vencer.")
        break
    else:
        palpites+=1
        print(f"{c2}Vc perdeu!{c0}")

    sleep(2)

    while True:
        c=str(input("Deseja tentar novamente? [S/N]")).upper()[0]

        if c in ["S","N"]:
            break
        else:
            print("Erro, por favor digite somente S ou N!")
    
    if c in "Nn":
        print("Obrigado por jogar!")
        break


