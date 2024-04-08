"""Desafio 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para o com o programa abaixo
from Modulos.matematica import ano_bissexto

#Usando de modulos para a formatação do programa
from Modulos.formatar import cor,cabecalho

#Greetings
cabecalho(cor("Bem vindo ao analizador de datas da Prof(a) Alexa!",35))

#Programa principal
while True:    
    
    #Tratamento de erros
    while True:
        try:
            ano=int(input("Digite um ano qualquer (Ex.1994): "))
            break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos para o ano (Exemplo: 2020)",31))
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa.",34))
            quit()
            
    #Usando de uma função que irá imprimir se o ano (parametro) é ou não bissexto
    ano_bissexto(ano)

    #Tratamento de erro
    while True:
        c = str(input("\nDeseja continuar verificando? [S/N]")).upper()[0]
        
        if c not in ["S","N"]:
            print(cor("Erro! Digite somente S para continuar o programa ou N para sair.",31))
        else:
            break
    #Saindo do programa
    if c == "N":
        print(cor("Obrigado e volte sempre!",35))
        break