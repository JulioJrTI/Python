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
            #Solicitando um valor ao usuario
            num=int(input("Digite um numero: "))
            break
        #Caso o usuario tenha inserido um valor invalido
        except ValueError:
            print(cor("Erro! Por favor digite somente numeros!",31))
        #Caso o usuario tenha cancelado o programa
        except KeyboardInterrupt:
            print(cor("O usuario cancelou o programa.",31) )           

    #Chamando uma função de tabuada e imprimindo os resultados na mesma
    cabecalho(cor(f"Tabuada do {num}:"),"*",45,53)
    tabuada(num)

    #Tratamento de erro
    while True:    
        #Iremos permitir ao usuario continuar o programa escolhendo novo numeros para tabuada
        c=str(input("\nDeseja continuar? [S/N]")).upper()
        
        #Caso o osuario tenha escolhido S ou N
        if c in ["S","N"]:
            break
        
        #Caso o usuario tenha inserido algum valor invalido
        else:
            print(cor("Erro! Digite somente S ou N como escolhas!",31))
    
    #Saindo do programa
    if c in "Nn":
        print(cor("Obrigado e volte sempre!",35))
        break


