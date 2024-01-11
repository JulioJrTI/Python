"""Desafio 09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada."""

from Modulos.Formatar import cabecalho,cor
from Modulos.Matematica import tabuada

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Programa principal
cabecalho(cor("Bem vindo a tabuada da Prof(a) Alexa!",35))
while True:

    #Tratamento de erros
    while True:
        try:
            num=int(input("Digite um numero: "))
            break
        except ValueError:
            print("Erro! Por favor digite somente numeros!")
        except KeyboardInterrupt:
            print("O usuario cancelou o programa.")            

    #Chamando uma função de tabuada e imprimindo os resultados na mesma
    print(f"Tabuada do {num}:")
    tabuada(num)

    #Tratamento de erro
    while True:    
        c=str(input("Deseja continuar? [S/N]")).upper()
        
        if c in ["S","N"]:
            break
        else:
            print("Erro! Digite somente S ou N como escolhas!")
    
    if c in "Nn":
        print("Obrigado e volte sempre!")
        break


