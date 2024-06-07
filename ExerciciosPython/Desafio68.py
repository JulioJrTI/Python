"""Desafio 68: Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas(f): #Função de linhas que irá acompanhar a quantidade de letras em uma frase ou variavel
    l=len(f)
    print("~"*l)
    print(f)
    print("~"*l)    

import random
from time import sleep

vitorias=0 #Contador de vitorias

Linhas(f"{c1}Bem vindo ao jogo de par e impar da Alexa!{c0}")
while True:
    playerEscolha1=str(input("Par ou Impar: ")).strip().upper() #Deixando a escolha do player em maiu e removendo os espaços
    playerEscolha2=int(input("Digite um numero: "))

    maquina=random.randint(1,11)
    print("Maquina está pensando...")
    sleep(2)
    print(f"Maquina escolheu {maquina}")
    sleep(2)
    somaNumeros=playerEscolha2+maquina #Iremos somar os numeros escolhidos pelo player e CPU
    print(f"Soma dos numeros escolhidos: {somaNumeros}")
    sleep(2)

    if somaNumeros%2==0:#Se a soma dos numeros for igual a PAR
        if playerEscolha1=="PAR": #E SE o player escolheu PAR
            print(f"{c1}Player venceu!{c0}") #Player wins
            vitorias+=1 #+1 vitoria ao contador
        else: #Se player escolher impar e a soma dos numeros for PAR
            print(f"{c2}Maquina venceu!{c0}") #CPU wins
            break #E o programa irá fechar
    else: #Se a soma dos numeros for igual a IMPAR
        if playerEscolha1=="IMPAR": #E SE o player escolheu IMPAR
            print(f"{c1}Player venceu!{c0}") #Player wins
            vitorias+=1 #+1 vitoria ao contador
        else: #Se player escolher PAR e a soma dos numeros for IMPAR
            print(f"{c2}Maquina venceu!{c0}") #CPU wins
            break #E o programa irá fechar  

Linhas(f"Vitorias do jogador: {vitorias}") #Resumo de vitorias do player