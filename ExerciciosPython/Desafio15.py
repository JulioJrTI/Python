"""Desafio 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

#Importando funções de formatação e cores
import json
from Modulos.Formatar import cabecalho,cor
from time import sleep

#Limpando o terminal cada execução do programa
from os import system
system("cls")

#Carregando informações se existirem
try:
    with open('dados_locacao.json','r') as arquivo:
        cadastroPessoas = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo de dados não encontrados. Será criado um novo!")
    #Dicionario contendo os dados de uma pessoa
    cadastroPessoas={"Nome do cliente":[],
                     "Quantidade de dias alugados":[],
                     "Quantidade de KMs percorridos":[],
                     "Valor total a pagar":[]}

#Greetings!
cabecalho(cor("Bem vindo ao programa de locação de carros da Alexa!",35))

#Programa principal
while True:    
    
    #Tratamento de erros
    while True:
        try:
            #Menu principal    
            c=int(input("[1] Cadastrar cliente"
                        "\n[2] Verificar cliente cadastrado"
                        "\n[3] Sair do programa"
                        "\nDigite sua escolha: "))        
            print()
            if c in [1,2,3]:
                break
            else:
                print(cor("Erro! Digite um valor de escolha de 1 a 3!",31))
        except ValueError:
            print(cor("Erro! Digite somente valores numericos!",31))
    
    #Cadastrando novos clientes
    if c==1:
        #Tratamento de erro
        while True:
            nomePessoa=str(input("Digite o nome do cliente: "))
            if nomePessoa.isalpha():
                cadastroPessoas["Nome do cliente"].append(nomePessoa)
                break
            else:
                print("Erro! Valor invalido! Digite o nome de uma pessoa corretamente (Exemplo: Alexa)")

        #Tratamento de erros
        while True:
            try:
                #Solicitando ao usuario que insira a quantidade de dias alugados
                quantDias=int(input("Digite a quantidade de dias alugados: "))
                cadastroPessoas["Quantidade de dias alugados"].append(quantDias)
                break
            except ValueError:
                print(cor("Erro! Por favor digite um valor numerico valido!",31))            

        #Calculando o valor a pagar pela quantidade de dias alugados 
        diasPagar=(quantDias*60)
        print(f"Total de dias alugados: {quantDias} dias")
        print(f"Valor a pagar: R${diasPagar:.2f}")

        #Tratamento de erros
        while True:
            try:
                #Solicitando ao usuario que insira a quantidade de KMs percorridos
                quantsKm=float(input("\nDigite a quantidade de KMs percorridos: "))
                cadastroPessoas["Quantidade de KMs percorridos"].append(quantsKm)
                break
            except ValueError:
                print(cor("Erro! Por favor digite um valor numerico valido!",31))
            

        #Calculando o valor a pagar pela quantidade de KMs percorridos
        kmsPagar=(quantsKm*0.15)
        print(f"Total de KMs percorridos: {quantsKm}")
        print(f"Valor a pagar: R${kmsPagar:.2f}")

        #Calculando total a pagar e imprimindo o resultado
        print("\nCalculando valor total...")
        sleep(1)
        totalPagar=(diasPagar+kmsPagar)
        cadastroPessoas["Valor total a pagar"].append(totalPagar)
        cabecalho(cor(f"Total a pagar: R${totalPagar:.2f}",34),cent=0,quantC=25)
        
        #Salvando informações
        with open('dados_locacao.json','w') as arquivo:
            json.dump(cadastroPessoas,arquivo)
        
    #Verificando clientes cadastrados
    elif c==2:
        print("Lista de clientes cadastrados:")
        for i, n in enumerate(cadastroPessoas["Nome do cliente"]):
            print(f"{i}: {n}")
        print()
        
        c1=int(input("Digite o numero referente ao cliente cadastrado: "))
        
        print(cor(f"Nome: {cadastroPessoas['Nome do cliente'][c1]}"))
        print(cor(f"Total a pagar: R${cadastroPessoas['Valor total a pagar'][c1]:.2f}"))
        print()
    
    #Saindo do programa
    elif c==3:
        print(cor("Obrigado e volte sempre!",35))
        break