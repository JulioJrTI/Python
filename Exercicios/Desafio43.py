"""Desafio 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso Ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida"""

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Efeito de cosmetico de loading
from time import sleep

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Salvamento e carregamento de informações
import json

#Carregando informações referentes ao dicionario contendo dados dos usuarios cadastrados
try:
    with open("dados_ex43.json","r") as arquivo:
        cadastro_pessoas = json.load(arquivo)
except FileNotFoundError:
    print("ERRO! ARQUIVO NÃO ENCONTRADO, CRIANDO UM NOVO!")
    #Dicionario contendo as informações referentes as pessoas cadastradas
    cadastro_pessoas={"Nome":[],
                    "Peso":[],
                    "Altura":[],
                    "IMC":[]}

#Greetings!
cabecalho(cor("Bem vindo ao medidor de peso da Prof(a) Alexa!",35))

#Programa principal
while True:    
    
    #Menu de escolhas ao usuario
    menu = int(input("[1] Cadastrar novos usuario\n"
                     "[2] Listar usuarios cadastrads\n"
                     "[3] Sair do programa\n"
                     "Insira: "))
    
    #Cadastrar novos usuarios
    if menu == 1:
        #Solicitando o nome da pessoa
        while True:        
            nomePessoa = str(input("Digite seu nome: "))        
            if nomePessoa.isalpha():
                cadastro_pessoas["Nome"].append(nomePessoa)
                break
            else:
                print(cor("\nErro! Digite somente palavras! (Exemplo: Alexa)\n",31)) 

        #Solicitando o peso
        while True:
            try:
                peso=float(input("Digite seu peso: "))
                cadastro_pessoas["Peso"].append(peso)
                break
            except ValueError:
                print(cor("\nErro! Digite somente valores numericos! (Exemplo: 6.9)\n",31))

        #Solicitando a altura
        while True:
            try: 
                altura=float(input("Digite sua altura: "))
                cadastro_pessoas["Altura"].append(altura)
                break
            except ValueError:
                print(cor("\nErro! Digite somente valores numericos! (Exemplo: 6.9)\n",31))

        #Calculando o IMC ao dividir peso pela altura (ao quadrado)
        imc_calculo = peso/(altura**2)
        #print(imc_calculo)

        #Condições para status do IMC
        if imc_calculo < 18.5:
            imc = str(imc_calculo)[:5] + cor(" = Abaixo do peso",36)
        elif 18.5 <= imc_calculo < 25:
            imc = str(imc_calculo)[:5] + cor(" = Peso Ideal",34)
        elif 25 <= imc_calculo < 30:
            imc = str(imc_calculo)[:5] + cor(" = Sobrepeso",33)  
        elif 30 <= imc_calculo < 40:
            imc = str(imc_calculo)[:5] + cor(" = Obesidade",32)
        else:
            imc = str(imc_calculo)[:5] + cor(" = Obesidade morbida",31)

        #Cadastrando o IMC ao dicionario
        cadastro_pessoas["IMC"].append(imc)
        
        #Salvando informações
        with open("dados_ex43.json","w") as arquivo:        
            json.dump(cadastro_pessoas,arquivo)

        #Imprimindo as informações da pessoa
        print(f"{nomePessoa}, tem {peso}(kg) e {altura:.2f}(m) de altura e seu IMC é {imc}.")
    
    #Lista completa de usuarios
    if menu == 2:
        #Lista completas das pessoas cadastradas
        system("cls")        
        print(cor("Lista de usuarios cadastrados!",35))
        for i in range(len(cadastro_pessoas["Nome"])):
            print(f"Nome: {cadastro_pessoas['Nome'][i]}")
            print(f"Peso: {cadastro_pessoas['Peso'][i]}")
            print(f"Altura: {cadastro_pessoas['Altura'][i]}")
            print(f"IMC: {cadastro_pessoas['IMC'][i]}")
            print("*"*50)
        sleep(5)
    
    #Sair do programa
    if menu == 3:
        print(cor("OBRIGADO E VOLTE SEMPRE!",35))
        quit() 