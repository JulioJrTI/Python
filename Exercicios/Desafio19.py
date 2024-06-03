"""Desafio 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido."""

import random
from os import system
import json
from Modulos.Formatar import cabecalho,cor,emotes
from time import sleep

#Limpando o terminal a cada execução do programa
system("cls")

#Carregando informações se existirem
try:
    with open('informacoes_ex19.json','r') as arquivo:
        alunos = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo de dados não encontrado. Será criado um novo!")
    #Lista de alunos
    alunos=[]

#Greetings
cabecalho(cor(f"Bem vindo a sala de aula da Prof(a) Alexa! {emotes(2)}",35))

#Programa principal
while True:    
    
    #Escolha ao usuario
    while True:
        c = int(input("[1] Cadastrar um(a) novo(a) aluno(a)"
                    "\n[2] Verificar lista de alunos cadastrados"
                    "\n[3] Escolher aluno aleatorio"
                    "\n[4] Sair do programa"
                    "\nInsira sua escolha: "))
    
        #Tratamento de erro
        if c in [1,2,3,4]:
            system("cls")
            break
        else:
            print(cor("Erro! Insira um valor de escolha de 1 a 4!",31))
    
    if c == 1:    
        while True:
            aluno=str(input("Digite o nome do(a) aluno(a): "))
            
            if aluno.isalpha():
                alunos.append(aluno)
                print(cor(f"Aluno(a) {aluno} cadastrado(a)!",35))
                sleep(2)
                print()         
                break
            
            else:
                print(cor("Erro! Por favor não digite valores alem de palavras!",31))     
        
    elif c == 2:
        print(cor("Lista de Alunos cadastrados:",35))
        for i, n in enumerate(alunos):
            print(f"{i}: {n}")
        sleep(3)
        print()
        
        while True:
            c2 = str(input("Deseja excluir algum aluno da lista? [S/N]")).upper()[0]
            
            if c2 in ["S","N"]:
                break
            else:
                print(cor("Erro! Por favor digite somente S ou N!",31))
        
        if c2 == "S":
            while True:            
                excluirAluno = int(input("Digite o valor numerico referente ao aluno que deseja excluir: "))
                if excluirAluno <0 or excluirAluno >= len(alunos):
                    print(cor("Erro! Numero inserido não equivale a nenhum aluno na lista!",31))
                else:
                    print(f"Aluno '{alunos[excluirAluno]}' excluido com sucesso!\n")
                    alunos.pop(excluirAluno)                    
                    break
            
    elif c == 3:
        alunoEscolhido = random.choice(alunos)
        print("Escolhendo aluno...")
        sleep(2)        
        cabecalho(cor(f"O aluno escolhido foi: {alunoEscolhido}",35))
        sleep(5)     
            
    elif c == 4:
        #Salvando informações
        with open('informacoes_ex19.json','w') as arquivo:
            json.dump(alunos,arquivo) 
        print(cor(f"Obrigado e volte sempre! {emotes(1)}",35))
        break 