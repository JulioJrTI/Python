"""Desafio 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundos entre eles."""

from time import sleep
from datetime import date

anoAtual=date.today().year

color="\033[1;32m"
colorEnd="\033[m"

print(f"{color}Contagem regressiva para o ano novo!{colorEnd}")
for n in range(10,0,-1):
    color=f"\033[1;3{n}m"
    print(color,n)
    sleep(1)    
print(colorEnd)
print(f"{color}Feliz {anoAtual+1}!!!{colorEnd}")
