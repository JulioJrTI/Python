"""
Desafio 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.

"""

#Usando de funções para a formatação
from Modulos.Formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Greetings!
cabecalho(cor("Bem vindo ao analisador de nomes da Prof(a) Alexa!",35))

#Tratamento de erros
while True:
    #Solicitando o nome completo de uma pessoa ao usuario
    nome=str(input("Digite seu nome completo: "))
    
    if nome.replace(" ","").isalpha():
        break
    else:
        print(cor("Erro! Digite somente palavras!",31))

#Imprimindo o nome inserido acima em MAIUSCULO
cabecalho(cor(f"Seu nome em maiusculo é '{nome.upper()}'",34),cent=0,quantC=50)

#Imprimindo o nome inserido acima em minusculo
cabecalho(cor(f"Seu nome em minusculo é '{nome.lower()}'",35),cent=0,quantC=50)

#Imprimindo a quantidade de caracteres no nome completo (sem espaços)
cabecalho(cor(f"Seu nome possui {len(nome.replace(" ",""))} caracteres.",36),cent=0,quantC=50)

#Dividindo o nome completo
nome = nome.split()

#Imprimindo a quantidade de caracteres no primeiro nome
cabecalho(cor(f"Seu primeiro nome possui {len(nome[0])} caracteres.",37),cent=0,quantC=50)