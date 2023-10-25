"""Desafio 16: Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Exemplo: Digite um numero: 6.127. O numero 6.127 tem a parte inteira 6."""

import math

color1="\033[1;32m"
color2="\033[1;34m"
colorEnd="\033[m"

numerosInt=[]
numerosFloat=[]

print(f"{color1}Bem vindo ao convertor de numeros da Alexa!{colorEnd}")
while True:
    numero=float(input(f"{color2}Digite um numero float: {colorEnd}"))    
    numerosFloat.append(numero)
    
    numeroInt=math.floor(numero)
    numerosInt.append(numeroInt)    

    print(f"{color1}Numero inteiro: {numerosInt[-1]}{colorEnd}") #Iremos exibir o ultimo numero inserido na lista
    
    c=str(input("Deseja fazer nova verificação: [S/N]"))

    if c in "Nn":
        break   
    
print(f"Numeros inteiros e convertidos durante o programa na ordem: ",end="")
for NI, NF in zip(numerosInt,numerosFloat):
    print(f"({color1}{NI}{colorEnd}={color2}{NF}{colorEnd})",end="")


