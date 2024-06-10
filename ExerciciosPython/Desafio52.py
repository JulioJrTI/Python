"""Desafio 52: Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo."""

import math

from time import sleep
#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

#Função que irá identificar se um numero é ou não um numero PRIMO
def indetificar_numPrimo(num=0):
    """
    Função que irá identificar se um numero (parametro) é ou não um numero PRIMO
    
    """
    
    msg_true = cor(f"O numero {num} é um numero PRIMO!",34)
    msg_false = cor(f"O numero {num} não é um numero PRIMO!",31)
    
    if num < 2:
        return msg_false
    if num == 2:
        return msg_true
    if num%2==0:
        return msg_false

    raiz = int(math.sqrt(num))

    for i in range(3,raiz+1,2):
        if num%i==0:
            return msg_false
    
    return msg_true

#Limpando o terminal
limpar_terminal()

#Greetings
cabecalho(cor("Bem vindo ao identificador de numeros PRIMOS da prof(a) Alexa!",35))

#Programa principal
while True:

    #Solicitando um numero qualquer para a identificação
    while True:    
        try:
            num = int(input("Digite um numero: "))
            break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos!\n",31))
            sleep(1)

    #Imprimindo o resultado da função        
    print(indetificar_numPrimo(num))
    
    #Continuar ou não o programa
    c = str(input("\nDeseja continuar? [S/N]")).upper()
    print()
    
    if c in "Nn":
        print(cor("OBRIGADO E VOLTE SEMPRE!"))
        break