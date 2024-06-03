"""Desafio 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas "sorteia()" e "somaPar()". A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior."""

from random import randint
from time import sleep

#Lista de numeros sorteados
numeros=[]

#Função que irá sortear 5 numeros aleatorios
def sorteia():
    for n in range(5):
        numerosSorteados=randint(1,10)
        numeros.append(numerosSorteados)    
    
    print("Numeros sorteados: ",end="")
    for num in numeros:
        print(num,end=" > ",flush=True)
        sleep(0.8)
    print("FIM")

#Função que irá mostrar a soma entre todos os valores pares
def somaPar():
    soma=0
    print(f"Somando numeros pares: ",end="")
    for valoresPares in numeros:    
        if valoresPares%2==0:
            print(f"{valoresPares}",end=" + ")
            soma+=valoresPares
    print(f"\b\b= {soma}") #Removendo os ultimos caracteres antes de imprimir a soma, neste o caso um espaço e o sinal de "="
    

#Chamando da função que irá sortear 5 numeros aleatorios
sorteia()

#Chamando da função que irá somar os numeros pares sorteados na função anterior
somaPar()