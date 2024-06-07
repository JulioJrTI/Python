"""Desafio 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais."""

c1="\033[1;32m"
c2="\033[1;34m"
c0="\033[m"

palavras=("Alexa","Dakota", "Candice","Tegan","Sereh")
vogais="aeiou"

print(f"{c1}Bem vindo ao identificador de vogais da Alexa!{c0}")
for p in palavras:
    print(f"Palavra: {c2}{p}{c0} - Vogais: ",end="")    
    for letras in p:
        if letras.lower() in vogais:
            print(f"{c1}{letras}{c0}",end=", ")
    print()
print("<<< FIM >>>")         