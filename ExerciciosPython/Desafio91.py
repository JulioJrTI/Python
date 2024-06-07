"""Desafio 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep

color_1="\033[1;32m"
color_2="\033[1;31m"
color_Reset="\033[m"

jogo={"Nome do jogador":[],"Dados":[],"Ganhador":[],"Perdedor":[]} #Dicionario com os nomes dos jogadores, pontos e resultados

maior=0 #Iremos armazenas o jogada com o maior ponto
menor=0 #Iremos armazenas o jogada com o menor ponto

print(f"{color_1}Bem vindo ao cassino da Alexa!{color_Reset}")
for j in range(4): #4 Jogadores   
    nome=str(input("Nome do jogador: "))
    jogo["Nome do jogador"].append(nome) #Adicionando o nome do jogador ao dicionario

    print(f"Player {nome} jogou os dados...")
    sleep(2)
    
    dados=randint(1,6) #Pensando em numeros aleatorios de 1 a 6
    print(f"Player {nome} tirou: {dados}")
    jogo["Dados"].append(dados) #Adicionando os pontos de cada jogador ao dicionario   

    #Iremos descobrir quem tirou o maior e menor ponto    
    if j==0: 
        maior=dados
        menor=dados
    else:
        if dados > maior:
            maior=dados
            ganhador=[nome,dados] #O jogador com maior ponto irá ter seu nome e ponto adicionario ao dicionario ganhador
            jogo["Ganhador"]=ganhador          
            
        if dados<menor:
            menor=dados
            perdedor=[nome,dados] #O jogador com menor ponto irá ter seu nome e ponto adicionario ao dicionario perdedor
            jogo["Perdedor"]=perdedor    

    print("-="*10)
print("<<< FIM >>>")

#Resumo do jogo
print(f"{color_2}Resumo da partida:{color_Reset}")
for i in range(len(jogo["Nome do jogador"])):
    print(f"Jogador: {jogo['Nome do jogador'][i]}")
    print(f"Resultado: {jogo['Dados'][i]}")
    print("-="*10)

#Resultado final
print(f"{color_1}Ganhador: {jogo['Ganhador']}{color_Reset}")
