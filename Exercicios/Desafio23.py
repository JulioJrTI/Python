"""Desafio 23: Trabalhando com listas, faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1"""

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Iremos inserir os numeros separadas por indice na lista abaixo
numeros=[]

#Greetings!
cabecalho(cor("Bem vindo ao analizador de numeros da prof(a) Alexa!",35))

#Tratamento de erro
while True:
    num_str = input("Digite um valor numerico de quatro digitos (exemplo 1984): \n")
    
    if len(num_str)!=4:
        print(cor("Erro! Digite quatro valores numericos!",31))  
    else:
        break

#Fatiando os quatro valores numericos, convertendo os mesmos para integer e os armazenando em uma lista
for digito in num_str:
    numeros.append(int(digito))

#Imprimindo os valores numericos separados por unidade, dezena, centena e milhar
print(cor(f"\nUnidade: {numeros[3]}\nDezena: {numeros[2]}\nCentena: {numeros[1]}\nMilhar: {numeros[0]}"))