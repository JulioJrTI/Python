"""Desafio 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

nomeCompleto=[]

print(f"{color1}Bem vindo ao analisador de nomes da Alexa 2.0!{colorEnd}")
while True:
    nome=str(input("Digite seu nome completo: (Ou digite 0 para sair) ")).lower()
    nomeSplit=nome.split()
    nomeCompleto.extend(nomeSplit) #Os items serão adicionado a lista de modo individual

    if nome=="0":
        print(f"{color1}Obrigado e tenha um bom dia!{colorEnd}")
        break
    
    if "silva" in nomeCompleto:
        print(f"{color1}Seu nome tem 'Silva'.{colorEnd}")
        nomeCompleto.clear()
    else:
        print(f"{color2}Seu nome não tem 'Silva'.{colorEnd}")
        nomeCompleto.clear()

    
