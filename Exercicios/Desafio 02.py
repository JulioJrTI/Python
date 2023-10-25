"""Desafio 02: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vidas."""

color1 = "\033[1;32m"
color2 = "\033[1;33m"
color3 = "\033[1;31m"
color4 = "\033[1;34m"
colorEnd = "\033[m"

pessoas = []  # Iremos colocar o nomes das pessoas nesta lista

print ( "=+" * 10, f"{color1}Bem vindo a festinha da Alexa!{colorEnd}", "=+" * 10 )
while True :
    pessoas.append ( input ( f"{color2}Digite o nome da garota:{colorEnd} " ) )
    c = input ( f"{color3}Deseja continuar? [S/N]{colorEnd}" )

    if c in "Nn" :
        break

for p in pessoas :  # Iremos falar o nomes das pessoas inseridas na lista e iremos dar boas vindas a elas
    print ( f"{color4}Bem vinda {p}!{colorEnd}" )
