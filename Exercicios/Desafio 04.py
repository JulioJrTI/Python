"""Desafio 04: Faça um programa que leia algo pelo teclado e mostre na tela o seu primitivo e todas as informações possiveis sobre ele."""

from Modulos.Formatar import tipoPrimitivo,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Iremos perguntar ao input um valor, este valor será armazenado em uma variavel e iremos chamar o metodo criado usando desta variavel como parametro    
while True:
    v=input("Digite algo: (Int ou Str)")
    if v.isalpha() or v.isnumeric() or v.isspace(): #Se o valor inserido for um string, numero ou somente espaços, iremos continuar com o programa       
        tipoPrimitivo(v)
        break
    else: #Caso contrario, iremos acionar um erro
        print(cor("ERRO! Digite um valor valido!",31))
        
        