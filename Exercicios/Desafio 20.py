"""Desafio 20: O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

#Usando de funções para a formatação do codigo
from Modulos.Formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Greetings!
cabecalho(cor("Bem vindo a classe da professora Alexa!",35))

#Lista de alunos
alunos = list()

#Solicitando ao usuario os nomes dos alunos e adicionando os mesmos a lista acima
while True: 
    aluno=str(input(f"Digite o nome do {len(alunos)+1}º aluno: (Ou digite 0 para sair)"))
    
    if aluno.isalpha():
        alunos.append(aluno)
    elif aluno == "0":
        break
    else:
        print(cor("Erro! Digite somente nomes! (Exemplo: Alexa)",31))

#Usando da biblioteca random para embaralhar a lista acima
import random
random.shuffle(alunos)

#Efeito cosmetico de loading
from time import sleep
print("\nSorteando alunos...")
sleep(3)

#Imprimindo a lista em ordem aleatoria
print(cor("\nSegue lista de alunos sorteados:",35))
for i, a in enumerate(alunos):
    print(f"{i+1}: {a}")