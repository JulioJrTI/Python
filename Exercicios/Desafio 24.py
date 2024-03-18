"""Desafio 24: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santa"."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cor,cabecalho

#Greetings!
cabecalho(cor("Bem vindo ao analizador de endereços da prof(a) Alexa!",35))

#Tratamento de erro
while True:        
    endereco = str(input("\nDigite seu endereço completo: ")).upper().strip()
    
    #Se o endereço inserido conter palavras ou se existirem espaços em branco, iremos aceitar e proseguir com o programa
    if endereco.isalpha() or " " in endereco:
        break
    else:
        print(cor("\nErro! Digite somente palavras em seu endereço!",31))

#Definindo uma função que irá ter uma palavra a ser identificada e o endereço completo como parametros
def identificarPalavra_endereco(palavra="",endereco=""):
    
    #Fatiando o endereço inserido
    endereco_separado = endereco.split()

    #Se a primeira palavra do endereço for 'Santa'
    if endereco_separado[0] in palavra:
        print(cor(f"\nO endereço começa com a palavra 'Santa'.",35))
    else:
        print(cor(f"\nO endereço não começa com a palavra 'Santa'.",31))

#Chamando da função acima
identificarPalavra_endereco("SANTA",endereco)