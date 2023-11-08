"""Desafio 99: Faça um programa que tenha uma função chamada "maior()", que receba vários parametros com valores inteiros. Seu programa tem que analisar todos os valroes e dizer qual deles é o maior."""

#Criando a função
def maior(num):
    #Criando uma logica de comparação de numeros
    maior=num[0]
    menor=num[0]

    for n in num:
        if n > maior:
            maior=n
        if n < menor:
            menor=n

    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

#Iremos armazenar os numeros digitados em uma lista
numeros=[]
for n in range(5):
    numero=int(input(f"Digite o {n+1}º numero: "))
    numeros.append(numero)

#Chamando da função para sabermos qual foi o maior e menor numero digitado
maior(numeros)
