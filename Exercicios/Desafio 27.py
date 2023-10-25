"""Desafio 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza"""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;31m"
colorEnd="\033[m"

nomeLista=[]

chave=True
chave2=True

print(f"{color1}Bem vindo ao separador de nomes da Alexa!{colorEnd}")
while True:
    if chave==True:
        nome=str(input("Digite seu nome completo: "))
        nomeLista.extend(nome.split())

        print(f"{color1}Nome completo = {nome}")
        print(f"{color2}Primeiro = {nomeLista[0]} ")
        print(f"{color3}Ultimo = {nomeLista[-1]}{colorEnd}")
        chave=False
        chave2=True

    if chave2==True:
        c=str(input("Deseja fazer nova verificação? [S/N]"))

        if c in "Ss":
            nomeLista.clear()
            chave=True
            chave2=False
        elif c in "Nn":
            print(f"{color1}Obrigado e volte sempre!")
            break
        else:
            print(f"{color3}Input invalido, tente novamente!{colorEnd}")