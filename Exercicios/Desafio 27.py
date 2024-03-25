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

#Solicitando o nome completo de uma pessoa
nomeCompleto = str (input ("Digite seu nome completo: "))

#Separando as palavras inseridas no nome completo
nome_separado = nomeCompleto.split()

#Imprimindo o nome completo do usuario
print(f"Nome Completo: {nomeCompleto}.")

#Imprimindo o primeiro nome
print(f"Primeiro: {nome_separado[0]}")

#Imprimindo o ultimo nome
print(f"Ultimo: {nome_separado[-1]}")