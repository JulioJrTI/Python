"""Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.
Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo."""

#Usando da biblioteca datetime identificarmos ano atual e idade dos usuarios
from datetime import date
anoAtual = date.today().year

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Efeito cosmetico de loading
from time import sleep

#Sistema de salvamento/carregamento de informações
import json

#Carregando informações referentes ao dicionario
try:
    with open("dados_ex39.json","r") as arquivo:
        cadastroPessoas = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado, criando um novo!")        
    #Dicionario contendo os dados das pessoas cadastradas
    cadastroPessoas={"Nome":[],"Idade":[],"Alistamento":[],"Data de Alistamento":[]} 

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Greetings!
cabecalho(cor("Bem vindo ao alistamento militar da comandante Alexa!",35))

#Programa principal
while True:
    
    #Tratamento de erros
    while True:
        #Menu do programa
        menu=int(input("[1] Cadastrar novo usuario\n[2] Listar todos os usuarios cadastrados\n[3] Sair do programa\nInsira: "))
        
        if menu <=3:
            break
        else:
            print(cor("Escolha invalida! Insira numero entre 1 e 3!",31))
    
    #Cadastrando novos usuarios
    if menu == 1:
        #Tratamento de erros
        while True:
            #Solicitando nome
            nomePessoa = str(input("Digite seu nome: "))
            
            if nomePessoa.isalpha():
                cadastroPessoas["Nome"].append(nomePessoa)
                break
            else:
                print(cor("\nErro! Digite somente nomes! (Ex: Alexa)\n",31))
                
        #Tratamento de erros
        while True:
            try:
                #Solicitando ano de nascimento
                anoNascimento = int(input(f"\nOlá {nomePessoa}, Digite o ano de seu nascimento: "))
                
                #User is not Dracula, The Prince of Darkness
                if anoNascimento > 1900:
                    break
                else:
                    print(cor("\nErro! Ano de nascimento invalido!",31))
                
            except ValueError:
                print(cor("\nErro! Digite somente numeros! (Ex: 1994)\n",31))
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa")
                quit()

        #Calculando idade
        idade = (anoAtual-anoNascimento)
        cadastroPessoas["Idade"].append(idade)

        #Se idade for igual ou maior a 18
        if idade >=18:
            
            #Tratamento de erro
            while True:        
                alistamento=str(input(f"\nVc possui {idade} anos de idade, vc se alistou? [S/N]")).upper()
                
                if alistamento in ["S","N"]:
                    break
                else:
                    print(cor("Erro! Digite somente 'S' para Sim ou 'N' para Não!",34))          
            
            if alistamento=="S":
                #Se a pessoa se alistou, iremos retornar como True o item referente ao mesmo no dicionario
                cadastroPessoas["Alistamento"].append("SIM")
                
                #Calculando o ano de alistamento
                anoAlistamento=anoNascimento+18            
                
                #Adicionando o ano de alistamento ao dicionario
                cadastroPessoas["Data de Alistamento"].append(anoAlistamento)
                
                #Imprimindo o ano que o usuario se alistou e quantos anos se passaram desde o ano de alistamento
                print(cor(f"\nVc se alistou no ano de {anoAlistamento}.",34))
                print(cor(f"Se passaram {anoAtual-(anoNascimento+18)} anos desde o alistamento.\n",34))
            elif alistamento=="N":
                #Calculando o ano de alistamento
                anoAlistamento=anoNascimento+18
                
                #Se a pessoa não se alistou, iremos retornar como False o item referente ao mesmo no dicionario
                cadastroPessoas["Alistamento"].append("NÃO")
                
                #Adicionando o ano de alistamento ao dicionario
                cadastroPessoas["Data de Alistamento"].append(anoAlistamento)
                
                #Imprimindo o ano que o usuario deveria ter se alistado
                print(cor(f"\nVc deveria ter se alistado no ano de {anoNascimento+18}!\n",31))
        
        #Se idade for menor a 18
        else:
            print(cor(f"Faltam {18-idade} anos até o alistamento obrigatorio!",34))
            
        #Salvando informações
        with open("dados_ex39.json", "w") as arquivo:
            json.dump(cadastroPessoas,arquivo)
        
        print(cor(f"Usuario {nomePessoa} cadastrado(a)!\nRetornando ao menu!\n",35))
        sleep(4)   
    
    #Listando todos os usuarios cadastrados
    if menu == 2:
        system("cls")
        cabecalho(cor("Usuarios cadastrados:",35))
        for i in range(len(cadastroPessoas["Nome"])):
            print("*"*50)
            print(f"Nome: {cadastroPessoas['Nome'][i]}")
            print(f"Idade: {cadastroPessoas['Idade'][i]}")
            print(f"{cadastroPessoas['Nome'][i]} se alistou: {cadastroPessoas['Alistamento'][i]}")
            print(f"Ano de alistamento: {cadastroPessoas['Data de Alistamento'][i]}")
            print()
        sleep(5)
            
    #Sair do programa
    if menu == 3:
        print("\nSaindo do programa...")
        sleep(2)
        print(cor("\nObrigado e volte sempre!",35))
        sleep(1)
        quit()