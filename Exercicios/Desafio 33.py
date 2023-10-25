"""Desafio 33: Faça um programa que leia três número e mostre qual é o maior e qual é o menor."""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
colorEnd="\033[m"

numeros={"Maior numero":[],"Menor numero":[]}

print(f"{color3}Bem vindo ao medidor de numeros max e min da Alexa!")
for n in range(3):      
    numero=int(input(f"Digite o {n+1} numero: "))
    if n==0:
        numeros["Maior numero"]=numero
        numeros["Menor numero"]=numero
    else:
        if numero > numeros["Maior numero"]:
            numeros["Maior numero"]=numero            
        if numero < numeros["Menor numero"]:
            numeros["Menor numero"]=numero            
print(f"{color1}O maior numero digitado foi o {numeros['Maior numero']}.")
print(f"{color2}O menor numero digitado foi o {numeros['Menor numero']}.{colorEnd}")
