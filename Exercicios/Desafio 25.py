"""Desafio 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

from Modulos.formatar import cor,cabecalho

#Greetings!
cabecalho(cor("Bem vindo ao analizador de nomes da prof(a) Alexa Blessings!",35))

while True:
    #Solicitando o nome completo de uma pessoa
    nomePessoa = str(input("Digite o nome completo de seu aluno(a): ")).lower()
    
    if nomePessoa.isalpha() or " " in nomePessoa:
        break
    else:
        print(cor("Erro! Não digite valores alem de palavras!\n",31))
    
#Criando uma função que irá conter uma palavra a ser identificar e uma frase (como o nome completo de uma pessoa) como parametros
def identificarPalavra(palavra="",frase=""):
    #Fatiando as palavras inseridas acima
    nome_split = frase.split()

    #Se uma palavra especifica for encontrado no nome completo de uma pessoa, iremos exibir uma confirmação
    if palavra in nome_split:
        print(cor(f"\nSeu nome completo contem a palavra '{palavra}'",35))
    else:
        print(cor(f"\nSeu nome completo não contem a palavra '{palavra}'",31))    
    
#Chamando da função criada acima para identificarmos a palavra 'silva' em um nome completo    
identificarPalavra("silva",nomePessoa)