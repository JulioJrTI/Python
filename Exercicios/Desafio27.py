"""Desafio 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza"""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cor,cabecalho

#Greetings!
cabecalho((cor("Bem vindo ao analizador de nomes da Prof(a) Alexa!",35)))

#Tratamento de erro
while True:
    #Solicitando o nome completo de uma pessoa
    nomeCompleto = str (input ("Digite seu nome completo: "))
    
    if nomeCompleto.isalpha() or " " in nomeCompleto:
        break
    else:
        print(cor("\nErro! Por favor digite somente palavras!\n",31))

#Criando uma função que identificar o primeiro e ultimo nome de uma pessoa
def obter_primeiro_ultimo_nome(nome=""):
    if nome == "":
        print(cor("Não foi inserido nenhum valor como parametro da função!",31))
    else:
        #Separando as palavras inseridas no nome completo
        nome_separado = nome.split()

        #Imprimindo o nome completo do usuario
        print(cor(f"\nNome Completo: {nome}",35))

        #Imprimindo o primeiro nome
        print(cor(f"\nPrimeiro: {nome_separado[0]}",35))

        #Imprimindo o ultimo nome
        print(cor(f"\nUltimo: {nome_separado[-1]}",35))
    
#Chamando da função criada e imprimindo as informações solicitadas
obter_primeiro_ultimo_nome(nomeCompleto)