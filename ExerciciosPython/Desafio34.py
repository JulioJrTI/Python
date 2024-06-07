"""Desafio 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

import json

#Greetings!
cabecalho(cor("Bem vindo ao calculador de salarios da gerente Alexa!",35))

#Carregando arquivo (ou criando um novo) contendo todas as informações cadastradas no dicionario
try:
    with open('DadosDesafio34.json','r') as arquivo:
        colaboradores = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo de dados não encontrado. Será criado um novo!")
    #Dicionario onde os nomes, salarios atuais, aumentos e novos salario serão cadastrados
    colaboradores={"Nome do colaborador":[],
                   "Salario Atual":[],
                   "Aumento":[],
                   "Novo Salario":[]}

#Programa principal
while True:
    
    #Tratamento de erros
    while True:
        try:
            #Cadastrando o nome do colaborador
            nomeColaborador = input("Digite o nome do(a) colaborador(a): ")
            
            if nomeColaborador.isalpha():
                colaboradores["Nome do colaborador"].append(nomeColaborador)
                break
            else:
                print(cor("Erro! Digite corretamente o nome do colaborador! (Ex: Alexa)",31))        
        except KeyboardInterrupt:
            print(cor("\nUsuario cancelou o programa",34))
            quit()
    
    #Tratamento de erros
    while True:    
        try:
            #Cadastrando o salario atual do colaborador
            salarioAtual=float(input(f"Digite o salario atual do colaborador(a) {nomeColaborador}: R$"))
            colaboradores["Salario Atual"].append(f"{salarioAtual:.2f}")
            break
        except ValueError:
            print(cor("Erro! Digite valores monetarios validos (Ex: 1500)",31))
        except KeyboardInterrupt:
            print(cor("\nUsuario cancelou o programa",34))
            quit()            
    
    #Variavel referente ao percentual do aumento, seguindo a logica abaixo
    aumento=0
    
    #Calculando o aumento do salario e o nome salario, e cadastrando os mesmos ao dicionario
    if salarioAtual > 1250:
        aumento=10
        colaboradores["Aumento"].append(aumento)       
        
    elif salarioAtual <= 1250:
        aumento=15
        colaboradores["Aumento"].append(aumento)
        
    novoSalario=float(salarioAtual+(salarioAtual*aumento/100))
    colaboradores["Novo Salario"].append(f"{novoSalario:.2f}")
    
    print(cor(f"\nCom {aumento}% de aumento, o salario do(a) colaborador {nomeColaborador} é de R${novoSalario:.2f}\n",35))
    
    #Tratamento de erro
    while True:
        #Dando escolha ao usuario para que o mesmo continue ou não cadastrando mais colaboradores
        c=input("Deseja continuar cadastrando: [S/N]").upper()[0]
        
        if c in ["S","N"]:
            break
        else:
            print(cor("Erro! Digite 'S' para continuar cadastrando ou 'N' para sairmos do programa",31))
    
    if c=="N":
        #Salvando informações e saindo do programa
        with open('DadosDesafio34.json', 'w') as arquivo:
            json.dump(colaboradores,arquivo)
        print(cor("Obrigado e volte sempre!",35))
        break
    
print(cor("\nLista dos colaboradores:",34))
for i in range(len(colaboradores["Nome do colaborador"])):
    print(f"Nome do colaborador: {colaboradores['Nome do colaborador'][i]}")
    print(f"Salario atual: R${colaboradores['Salario Atual'][i]}")
    print(f"Aumento de salario: {colaboradores['Aumento'][i]}%")
    print(f"Novo salario: R${colaboradores['Novo Salario'][i]}")
    print(cor("*"*10))