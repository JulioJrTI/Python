"""Desafio 38: Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

"O primeiro valor é maior"
"O segundo valor é maior"
"Não existe valor maior, os dois são iguais"""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

numeros={"Primeiro numero":[],"Segundo numero":[]}

print(f"{color1}Bem vindo ao analizador de maior e menor numero da Alexa!{colorEnd}")
while True:
    n1=int(input("Digite o primeiro numero: "))
    numeros["Primeiro numero"].append(n1)
    
    n2=int(input("Digite o segundo numero: "))
    numeros["Segundo numero"].append(n2)

    if numeros["Primeiro numero"]>numeros["Segundo numero"]:
        print(f"{color1}O primeiro valor é maior{colorEnd}")        
    elif numeros["Segundo numero"]>numeros["Primeiro numero"]:
        print(f"{color1}O segundo valor é maior{colorEnd}")        
    elif n1==n2:
        print(f"{color2}Não existe valor maior, os dois são iguais{colorEnd}")    
    print()
    
    while True:
        c=str(input("Deseja efetuar nova verificação? [S/N]")).lower()

        if c in ["s","n"]:
            break
        print(f"{color2}Input invalido!{colorEnd}")

    if c in "s":
        numeros["Primeiro numero"]=[]
        numeros["Segundo numero"]=[]      
    elif c in "n":
        print(f"{color1}Obrigado e tenha um bom dia!{colorEnd}")
        break