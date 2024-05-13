"""Desafio 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: Reprovado
-Média entre 5.0 e 6.9: Recuperação
-Média entre 7.0 ou superior: Aprovado"""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Efeito cosmetico de loading
from time import sleep

#Usando JSON para o armazenamento de informações
import json

#Carregando informações armazenadas
try:
    with open ("dados_ex40.json","r") as arquivo:
        cadastroAlunos = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado, criando um novo!")
    #Dicionario que irá conter os nomes, notas e medias dos alunos
    cadastroAlunos = {"Nome":[],"Nota 1":[],"Nota 2":[],"Media":[],"Situacao":[]}

#Greetings
cabecalho(cor("Bem vindo ao calculador de notas da Prof(a) Alexa!",35))

#Programa principal
while True: 
    #Menu
    menu=int(input("[1] Cadastrar novo aluno(a)\n[2] Listar todos os alunos cadastrados\n[3] Sair do programa\nInsira: "))
    
    #Cadastrando novos alunos
    if menu == 1:
        #Limpando o terminal
        system("cls")
        
        #Tratamento de erro    
        while True:
            #Solicitando o nome do aluno e adicionando o mesmo ao dicionario
            nome_aluno = str(input("Digite o nome do aluno: "))
            
            if nome_aluno.isalpha():
                cadastroAlunos["Nome"].append(nome_aluno)
                break
            else:
                print(cor("\nErro! Digite somente palavras! (Ex: Alexa)\n",31))

        #Imprimindo o nome do(a) aluno(a)
        cabecalho(f"Aluno(a): {nome_aluno}",cent=0)
        
        #Solicitando duas notas ao usuario e adicionando as mesmas ao dicionario    
        #Tratamento de erro
        while True:
            try:    
                n1=float(input("Digite a primeira nota: "))
                cadastroAlunos["Nota 1"].append(n1)
                break
            except ValueError:
                print("Erro! Digite somente valores numericos: (Exemplo 5.0)")
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa")
                quit()
        #Tratamento de erro        
        while True:
            try:
                n2=float(input("Digite a segunda nota: "))
                cadastroAlunos["Nota 2"].append(n2)
                break
            except ValueError:            
                print("Erro! Digite somente valores numericos: (Exemplo 5.0)")
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa")
                quit()            

        #Calculando media
        media_notas = (n1+n2)/2
        cadastroAlunos["Media"].append(media_notas)
        print(f"\nMedia de notas: {media_notas}")
        
        #Situação do aluno
        if media_notas < 5.0:
            situacao = "Reprovado"
        elif 5.0 <= media_notas <= 6.9:
            situacao="Recuperação"
        else:
            situacao="Aprovado"
            
        #Adicionando a situação do aluno ao dicionario
        cadastroAlunos["Situacao"].append(situacao)
        
        #Imprimindo a situação do aluno
        print(f"O(a) aluno(a) {nome_aluno}, está {situacao}!")
        
        #Pausa de alguns segundos
        sleep(5)
        print()                
        
        #Salvando informações do aluno
        with open("dados_ex40.json","w") as arquivo:
            json.dump(cadastroAlunos,arquivo)
    
    #Listando todos os alunos cadastrados
    if menu == 2:
        
        #Limpando o terminal
        system("cls")
        
        #Listando o indice e nome do aluno cadastrado na lista
        print("\nSegue alunos cadastrados:")
        for i,n in enumerate(cadastroAlunos["Nome"]):
            print(f"{i}: {n}")
            
        #Perguntando ao usuario se o mesmo deseja ver as informações de todos os alunos ou se o mesmo deseja verificar de um aluno especifico
        c1 = str(input("\nDeseja listar as informações de todos os alunos cadastrados? [S/N] \nSelecione 'N' para selecionar um aluno especifico \nInsira: ")).upper()
        
        #Se o usuario escolher 'S', iremos exibir a lista inteira de todos os alunos cadastrados
        if c1 == "S":            
            #Limpando o terminal
            system("cls")
            
            #Imprimindo a lista de alunos com todas as notas e medias dos mesmos
            print(cor("\nLista de alunos cadastrados:",35))
            for i in range(len(cadastroAlunos["Nome"])):
                print(f"Nome do aluno(a): {cadastroAlunos['Nome'][i]}")
                print(f"Notas: 1º: {cadastroAlunos['Nota 1'][i]} - 2º: {cadastroAlunos['Nota 2'][i]}")
                print(f"Media das notas: {cadastroAlunos['Media'][i]}")
                print(f"Situação do aluno: {cadastroAlunos['Situacao'][i]}")
                print("*"*50)
            
            #Pausa de alguns segundos
            sleep(5)
            print()    
        
        #Caso o usuario tenha escolhido 'N', iremos dar ao usuario a opção de escolher um aluno especifico
        elif c1 == "N":  
        
            #De acordo com o valor numerico inserido (indice), iremos exibir as informações do aluno(a)
            c2 = int(input("\nSeguindo o valor numerico referente ao aluno \nSelecione o mesmo desejado: "))
            
            print("*"*50)
            print(f"Nome: {cadastroAlunos["Nome"][c2]}")
            print(f"Notas: 1º: {cadastroAlunos["Nota 1"][c2]} - 2º: {cadastroAlunos["Nota 2"][c2]}")
            print(f"Media: {cadastroAlunos["Media"][c2]}")
            print(f"Situação do aluno: {cadastroAlunos['Situacao'][c2]}")
            print("*"*50)
            
            sleep(5)
            print()
         
    #Sair do programa
    if menu == 3:
        print(cor("\nObrigado e volte sempre!",35))
        break