"""Desafio 26: Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A".

Em que posição ela aparece a primeira vez.

Em que posição ela aparece a última vez."""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;31m"
colorEnd="\033[m"

chave=True
chave2=True

print(f"{color1}Bem vindo ao localizador de letras da Alexa!{colorEnd}")
while True:
    if chave==True:
        frase=str(input("Digite uma frase: ")).lower()        
        print(f"{color1}A letra 'A' aparece {frase.count('a')} vezes.")
        print(f"{color2}A letra 'A' aparece pela primeira vez na {frase.find('a')+1}º posição.")
        print(f"{color3}A letra 'A' aperece pela ultima vez na {frase.rfind('a')+1}º posição.{colorEnd}")
        chave=False
    
    chave2=True
    if chave2==True:
        c=str(input("Deseja fazer nova verificação? [S/N]"))

        if c in "Ss":
            chave2=False
            chave=True            
        elif c in "Nn":
            print(f"{color1}Obrigado e volte sempre!")
            break
        else:
            print(f"{color3}Tente novamente!{colorEnd}")



