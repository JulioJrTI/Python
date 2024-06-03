"""Desafio 78: Faça um programa que leia 5 valores númericos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

numeros=[]

maiorNumero=0
menorNumero=0

print(f"{c1}Bem vindo ao analisador listal de numeros da Alexa!{c0}")
for n in range(5):
    while True:
        try:
            num=int(input(f"Digite o {n+1}º primeiro: "))
            break
        except:
            print(f"{c2}Por favor, digite somente numeros!{c0}")
    
    if n==0:
        maiorNumero=num
        menorNumero=num
    else:
        if num>maiorNumero:
            maiorNumero=num
        if num<menorNumero:
            menorNumero=num
    numeros.append(num)
print(numeros)

print(f"O maior numero da lista é o numero {maiorNumero}, na posição {numeros.index(maiorNumero)}.")
print(f"O menor numero da lista é o numero {menorNumero}, na posição {numeros.index(menorNumero)}.")