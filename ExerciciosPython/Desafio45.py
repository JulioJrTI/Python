"""Desafio 45: Crie um programa que faça o computador jogar Pedra/Papel/Tesoura com voce."""

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Efeito cosmetico de delay
from time import sleep

#A maquina irá sortear um numero aleatorio
from random import randint

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Programa principal
while True:

    #Greetings!
    cabecalho(cor("Bem vindo ao game de Rock/Paper/Scissors da Alexa!",35))

    #Opções para o jogador
    opcoes=["[0] Pedra",
            "[1] Papel",
            "[2] Tesoura"]

    #Imprimindo as opções a serem escolhidas
    for o in opcoes:
        print(o)

    #Escolha do Player
    while True:
        player=int(input("Insira sua escolha: "))
        
        if player <=2:
            break
        else:
            print(cor("\nEscolha incorreta! Escolha um valor numerico de 0 a 2!\n",35))        

    #A maquina irá escolher um valor numerico de 0 a 2
    cpu=randint(0,2)

    #Imprimindo escolhas da maquina e player    
    print(cor(f"\nJogador escolheu: {opcoes[player]}",34))
    sleep(2)
    print(cor(f"\nMaquina escolheu: {opcoes[cpu]}",31))
    sleep(2)

    #Condições de vitoria e derrota
    if (player==0 and cpu==2) or (player==1 and cpu==0) or (player==2 and cpu==1):
        print(cor("\nPlayer ganhou!",34))
    elif player == cpu:
        print(cor("\nEmpate!",33))
    else:
        print(cor("\nMaquina ganhou!",31))
        
    #Continuar ou não o game
    sleep(3)
    c=str(input("\nDeseja continuar? [S/N]")).upper()[0]
    
    if c in "S":
        system("cls")
    else:
        print(cor("\nOBRIGADA E VOLTE SEMPRE!",35))
        break