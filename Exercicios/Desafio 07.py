"""Desafio 07: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""

#Efeito de carregamento
from time import sleep

#Chamando funções
from Modulos.Matematica import mediaNumeros
from Modulos.Formatar import cor,cabecalho

#Limpando o terminal a cada execução do programa
import os
os.system("cls")

#Iremos armazenar os nomes, notas e medias dos alunos em um dicionario
alunos={"Nome":[],"Nota 1":[],"Nota 2":[],"Media":[]}

#Chave de controle para adicionarmos ou não novos alunos
chave=True

#Programa principal
cabecalho(cor("Bem vindo ao calculador de notas da Professora Alexa!",35))
while True:
    
    while chave:        
        #Tratamento de erro
        while True:
            #Adicionando nome do aluno ao dicionario
            nomeAluno=str(input("Digite o nome do aluno(a): "))
            
            if nomeAluno.isalpha():
                alunos["Nome"].append(nomeAluno)
                break 
            else:
                print(cor(f"Por favor digite somente palavras!",31))
        
        #Tratamento de erro
        while True:
            try:        
                #Adicionando a primeira nota do aluno ao dicionario
                nota1=int(input(f"Digite a primeira nota do aluno(a) {nomeAluno}: "))
                alunos["Nota 1"].append(nota1)
                break
            except:
                print(cor(f"Erro! Por favor digite somente numeros!",31))
        
        #Tratamento de erro
        while True:
            try:        
                #Adicionando a segunda nota do aluno ao dicionario
                nota2=int(input(f"Digite a segunda nota do aluno(a) {nomeAluno}: "))
                alunos["Nota 2"].append(nota2)
                break
            except:
                print(cor(f"Erro! Por favor digite somente numeros!",31))
        
        print(cor("\nCalculando nota...\n"))
        sleep(2)
        
        #Calculando media e adicionando a mesma ao dicionario
        media=mediaNumeros(nota1,nota2)
        alunos["Media"].append(media)
        cabecalho(f"A media de notas do aluno(a) {nomeAluno} é {media}",quantC=45,cent=0)
        chave=False
    
    #Tratamento de erro
    while True:
        #Menu de escolha ao usuario
        c=int(input("[1] Cadastrar novo aluno\n"
                    "[2] Verificar notas de um aluno\n"
                    "[3] Mostrar todos os alunos e notas\n"
                    "[4] Sair do programa\n"
                    "Escolha uma opção: "))
        if c in [1,2,3,4]:
            break
        else:
            print(cor("Escolha somente uma opção entre 1 e 4!",31))
    
    #Caso seja escolhido a opção '1', iremos poder cadastrar um novo aluno
    if c==1:
        chave=True
        print()
    
    #Caso seja escolhido a opção '2', iremo perguntar ao usuario qual será o aluno e suas notas a ser verificado
    elif c==2:
        print("Lista de alunos cadastrados: ")
        for i, n in enumerate(alunos["Nome"]):
            print(f"{i}: {n}")        
        
        c=int(input("Escolha o aluno a verificar notas: ")) 
        alunoEscolhido = alunos["Nome"][c]
        nota1=alunos["Nota 1"][c]
        nota2=alunos["Nota 2"][c]
        media=alunos["Media"][c]
        
        print("*"*50)
        print(f"Informações do aluno(a) {alunoEscolhido}:")
        print(f"Nota 1: {nota1}")
        print(f"Nota 2: {nota2}")
        print(f"Media: {media}")
        print("*"*50)
        
    #Caso seja escolhido a opção '3', iremos mostrar uma lista com todos os alunos cadastrados, suas notas e medias
    elif c==3:
        print("*"*50)
        print("Alunos cadastrados:\n")
        for i in range(len(alunos["Nome"])):
            print(f"Aluno: {alunos['Nome'][i]}")
            print(f"Nota 1: {alunos['Nota 1'][i]}")
            print(f"Nota 2: {alunos['Nota 2'][i]}")
            print(f"Media: {alunos['Media'][i]}\n")
        print("*"*50)            
    
    #Caso seja escolhido a opção '4', iremos sair do programa
    elif c==4:
        print(cor("\nObrigado e volte sempre!",35))
        break
    
   
    

