"""Desafio 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome."""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
color4="\033[1;35m"
colorEnd="\033[m"
enfeite="=-"*10

chave=True

print(f"{color1}Bem vindo ao contador de letras da Alexa!")
print(enfeite)
while True:
    if chave==True:
        nome=input(f"Digite seu nome: {colorEnd}")
        chave=False
    
    maiu=nome.upper()
    print(f"Seu nome em maiu é: {color1}{maiu}{colorEnd}")
        
    minu=nome.lower()
    print(f"Seu nome em minu é: {color2}{minu}{colorEnd}")

    semEsp=nome.replace(" ","")
    quantLetras=len(semEsp)
    print(f"Seu nome completo tem {color3}{quantLetras}{colorEnd} letras (Sem espaços)")

    primeiroNome=nome.split()
    print(f"Seu primeiro nome tem {color4}{len(primeiroNome[0])}{colorEnd} letras.")
    print(enfeite)
    
    c=str(input("Deseja efetuar nova verificação? [S/N]"))

    if c in "Ss":
        chave=True
    elif c in "Nn":
        print(f"{color1}Obrigado e tenha um bom dia!{colorEnd}")
        break





