"""Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 20 anos: Sênior
-Acima: Master"""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Sistema de armazenamento de informações
import json

#Trabalhando com datas (ano atual, nascimento, idade)
from datetime import date

#Efeito cosmetico de pausa
from time import sleep

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Ano Atual
ano_Atual = date.today().year

#Carregando arquivo contendo as informações cadastradas no programa
try:
    with open("dados_ex41.json","r") as arquivo:
        atletas = json.load(arquivo)
except FileNotFoundError:
    print("Erro! Arquivo não encontrado, criando um novo!")
    #Cadastrando todas as informações dos atletas em um dicionario
    atletas = {"Nome":[],"Ano de nascimento":[],"Idade":[],"Categoria":[]}

#A partir da segunda chamada do menu, iremos adicionar uma pausa de alguns segundos antes do mesmo aparecer
sec_time = False

#Greetings
cabecalho(cor("Bem vindo a Confederação Nacional de Natação!",35))

#Programa principal
while True:
    
    #Tratamento de erro
    while True:
        
        #A partir da segunda chamada do menu
        if sec_time:
            sleep(5)
            print()
        
        #Menu principal
        menu = int(input("[1] Cadastrar novo atleta\n[2] Listar atletas cadastrados\n[3] Sair do programa\nInsira: "))        
        
        sec_time=True 
        
        if menu in range(1,4):            
            break
        else:
            print(cor("Erro! Digite '1' para cadastrarmos novos atletas,\n'2' para listarmos todos os atletas cadastrados\nou '3' para sair do programa\n",31))
    
    #Cadastrando novos atletas
    if menu == 1:    
        #Tratamento de erro
        while True:
            #Nome do atleta
            nome_atleta = str(input("Digite o nome do atleta: "))
            
            if nome_atleta.isalpha():
                atletas["Nome"].append(nome_atleta)
                break
            else:
                print(cor("\nErro! Digite somente nomes! (Exemplo: Alexa)\n",31))
            
        #Tratamento de erro
        while True:        
            try:
                #Solicitando o ano de nascimento do atleta
                ano_Nascimento = int(input(f"Digite o ano de nascimento do(a) atleta {nome_atleta}: "))
                atletas["Ano de nascimento"].append(ano_Nascimento)
                break
            except ValueError:
                print(cor("\nErro! Digite somente valores numericos para a data de nascimento (Exemplo: 1994)\n",31))

        #Idade do atleta
        idade = (ano_Atual-ano_Nascimento)
        print(cor(f"\nO(a) atleta {nome_atleta}, possui {idade} anos de idade.",34))
        atletas["Idade"].append(idade)

        #Verificando a categoria do atleta
        if idade <= 9:
            categoria = "Mirim"
        elif idade <= 14:
            categoria = "Infantil"
        elif idade <= 19:
            categoria = "Junior"
        elif idade <= 20:
            categoria = "Senior"
        else:
            categoria = "Master"

        #Imprimindo a categoria    
        print(cor(f"A categoria do atleta {nome_atleta} é {categoria}!\n",34))
        atletas["Categoria"].append(categoria)
        
        #Salvando as informações em um arquivo .json
        with open("dados_ex41.json","w") as arquivo:
            json.dump(atletas,arquivo)        
        
    #Listando atletas cadastrados
    if menu == 2:
        #Limpando o terminal
        system("cls")
        
        #Listando o indice e nome dos atletas cadastrados
        print("Lista de atletas cadastrados:")
        for i, n in enumerate(atletas["Nome"]):
            print(f"{i}: {n}")
        
        #Escolha ao usuario
        c1 = str(input("\nInsira o valor de indice referente ao atleta cadastrado para exibirmos seu status (Ou digite X para exibirmos a lista inteira)")).upper()
        
        if c1.isdigit() and int(c1) < len(atletas["Nome"]):        
            #Exibindo o atleta de acordo com o valor de indice digitado acima
            system("cls")
            print(f"\nInformações sobre o atleta {atletas['Nome'][int(c1)]}")
            print(f"Nome: {atletas['Nome'][int(c1)]}")
            print(f"Ano de Nascimento: {atletas['Ano de nascimento'][int(c1)]}")
            print(f"Idade: {atletas['Idade'][int(c1)]}")
            print(f"Categoria: {atletas['Categoria'][int(c1)]}") 
        #Exibindo todos os atletas cadastrados e suas informações
        elif c1 == "X":
            system("cls")
            for i in range(len(atletas["Nome"])):
                print(f"Nome: {atletas["Nome"][i]}")
                print(f"Ano de Nascimento: {atletas["Ano de nascimento"][i]}")
                print(f"Idade: {atletas["Idade"][i]}")
                print(f"Categoria: {atletas["Categoria"][i]}")
                print("*"*50)                
        else:
            print(cor("\nErro! Digite somente o valor em indice informado ao lado do nome do atleta ou digite 'X' para listarmos todos os atletas cadastrados!",31))
            print("\nVoltando ao menu...")        
    
    #Saindo do programa
    if menu == 3:
        print(cor("\nOBRIGADO E VOLTE SEMPRE!",35))
        break