"""Desafio 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

chave=True

print(f"{color1}Bem vindo ao analizador de pares e impares da Alexa!{colorEnd}")
for n in range(chave):
    while chave:
        numero=int(input("Digite um numero qualquer: "))
        chave=False    

        if numero%2==0:
            print(f"{color1}Numero Par{colorEnd}")
        else:
            print(f"{color2}Numero Impar{colorEnd}")

        c=str(input("Deseja efetuar nova verificação? [S/N]"))

        if c in "Ss":
            chave=True
        elif c in "Nn":
            print(f"{color1}Obrigado e tenha um bom dia!")
            break