"""Desafio 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuario vai digitar o comando e o manual vai aparecer. Quanto o usuario digitar a palavra "FIM", o programa se encerrará.

OBS: use cores."""

#Efeito de loading
from time import sleep

#Cores
c1="\033[1;32m"
c0="\033[m"

#Função principal
def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'")    
    help(com)
    sleep(2)

#Função para personalizarmos os titulos
def titulo(msg):
    tam=len(msg)+4    
    print(c1)
    print("~"*tam)
    print(f"  {msg}")
    print("~"*tam)
    print(c0)
    sleep(1)

#Programa principal
comando=""
while True:
    titulo(f"Sistema de ajuda PyHelp")
    comando=str(input("Função ou biblioteca -> "))
    if comando.upper()=="FIM":
        break
    else:
        ajuda(comando)
titulo(f"Ate Logo")