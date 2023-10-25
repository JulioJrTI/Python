"""Desafio 74: Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla."""

from random import randint

def Linhas():
    print("~"*20)

c1="\033[1;32m"
c0="\033[m"

numeros=tuple(randint(1,10) for _ in range(5))

print(f"{c1}Lista de numeros aleatorios gerados:{c0}")
for i,v in enumerate(numeros,start=1):
    print(f"{i}º: {v}")

Linhas()
maiorNum=max(numeros)
print(f"Maior numero na tupla: {maiorNum}")

Linhas()
menorNum=min(numeros)
print(f"Menor numero na tupla: {menorNum}")
Linhas()


