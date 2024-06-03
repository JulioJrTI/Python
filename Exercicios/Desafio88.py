"""Desafio 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

loteria=[]

print(f"{c1}Bem vindo a loteria da Alexa!{c0}")

while True:
    try:
        jogos=int(input("Quantos jogos deseja jogar: ")) #Pedindo a quantidade de jogos (quant de listas de numeros aleatorios a serem geradas)
        break
    except:
        print(f"{c2}Erro! Digite somente numeros!{c0}")

for p in range(jogos): #Quantidade de jogos gerada de acordo com o input
    novo_jogo=[] #Cada loop de listas será armazenada nesta lista vazia
    print(f"{p+1}º Jogo: ")
    print("Gerando numeros...")
    sleep(2)    
    for j in range(6): #Quantidade de numeros aleatorios a serem geradas
        num=randint(1,60) #Gerando numeros de 1 a 60
        novo_jogo.append(num) #Armazendo os numeros gerados na lista vazia acima
    loteria.append(novo_jogo) #Armazendo todos as listas de numeros geradas para a lista principal
    print(f"{c1}Numeros gerados para o {p+1}º jogo:{c0} {novo_jogo}") #Mostrando os numeros geradas a cada loop
    sleep(1) 
print("<<< FIM >>>")

print(f"{c1}Lista geral de numeros:{c0}")
for i, n in enumerate(loteria,start=1): #Mostrando as listas de numeros de acordo com a ordem de jogos
    print(f"{i}º jogo: {n}")
