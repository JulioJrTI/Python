"""Desafio 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

c1="\033[1;32m"
c2="\033[1;34m"
c3="\033[1;31m"
c0="\033[m"

numeros=[]

print(f"{c1}Bem vindo ao listador de numeros da Alexa!{c0}")
while True:
    while True:
        try:
            num=int(input("Digite um numero: (Ou digite 0 para sair)"))
            break
        except:
            print(f"{c3}Erro! Digite somente numeros!{c0}")

    if num==5:
        print(f"{c1}Numero 5 digitado!{c0}")
    
    if num==0:
        break
    else:
        numeros.append(num)

#Quantidade de valores na lista
print(f"{c2}Foram digitados {len(numeros)} numeros.{c0}")

#Lista em ordem decrescente
numeros.sort(reverse=True)
print(f"{c2}Segue lista ordenada em ordem decrescente: {numeros}{c0}")

#Verificando se o valor 5 está ou não na lista
if 5 not in numeros:
    print(f"{c3}O numero 5 não está na lista.{c0}")
else:
    print(f"{c1}O numero 5 está na lista.{c0}")