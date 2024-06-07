"""Desafio 28: Escreva um programa que faça o computador "pensar" 
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Criando uma função que irá escolher aleatoriamente um valor entre o valores em parametro inseridos como inicio e fim
def numeros_aleatorios(inicio=0,fim=0):
    #Iremos usar da função 'randint' do modulo Random para gerarmos numeros aleatorios
    from random import randint
    num = randint(inicio,fim)    
    return num    

#Greetings!
cabecalho(cor("Bem vindo(a) ao game de adivinhação da Prof(a) Alexa Luzia!",35))

#Programa principal
while True:    
    
    #Tratamento de erros
    while True:    
        try:
            #Jogador
            jogador=int(input("Digite um numero qualquer entre 0 e 5: "))            
            
            if 0 <= jogador <= 5:
                break
            else:
                print(cor("Erro! Digite somente numeros entre 0 e 5!",31))   
        
        except ValueError:
            print(cor("Erro! Digite valores somente valores numericos!",31))
    
    #Maquina
    maquina = numeros_aleatorios(0,5)

    #Se o jogador adivinhar o numero escolhido pela maquina, o mesmo ganha
    if jogador==maquina:
        print(cor(f"Voce ganhou!\nA maquina escolheu o numero {maquina}",34))
    else:
        print(cor(f"Voce perdeu!\nA maquina escolheu o numero {maquina}",31))
        
    #Tratamento de erro
    while True:    
        c = str(input("Deseja tentar novamente? [S/N]")).upper()[0]
        
        if c in ["S","N"]:
            break
        else:
            print(cor("Erro! Digite somente S para continuar ou N para sair do game!",31)) 
    
    if c in "Nn":
        print(cor("Obrigada por jogar!",35))
        break