"""Desafio 03: Crie um programa que leia dois numeros e mostre a soma entre eles."""

#Importando modulos, um irá somar dois numeros e outro para formatação
from Modulos.Matematica import somarNumeros
from Modulos.Formatar import cabecalho,cor

#Importando uma biblioteca do sistema operacional que irá limpar o terminal a cada execução do programa
import os
#Limpando terminal
os.system("cls") 

#Programa principal
cabecalho(cor("Bem vindo a calculadora da Alexa!"),53)
numeros=[] #Inserindo os numeros digitados no loop abaixo em uma lista
for n in range(2):    
    while True: #Tratamentos de erros
        try:
            numero=int(input(f"Digite o {n+1}º numero: "))
            numeros.append(numero)
            break            
        except (ValueError,TypeError):
            print(cor("ERRO! Por favor digite um numero sem letras ou caracteres especiais!",31))

#Inserindo os numeros da lista como parametros da função abaixo
somarNumeros(*numeros)