"""
Desafio 36: Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.
"""

#Iremos carregar e salvar informações do programa
import json

#Efeito de atraso
from time import sleep

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Sistema de carregamento de informações (do dicionario)
try:
    with open("dados_ex36","r") as arquivo:
        cadastroPessoas = json.load(arquivo)
except FileNotFoundError:
    print(cor("Arquivo de dados não encontrado, será criando um novo.",31))
    #Iremos cadastrar cada pessoa em um dicionario
    cadastroPessoas={"Nome":[],"Valor da Casa":[],
                    "Salario":[],
                    "Anos de parcelamento":[],
                    "Parcelamento Mensal":[],
                    "Resultado":[]}

#Função que irá exibir os detalhes de cada pessoa cadastrada (ou pessoa especifica usando o valor em index como parametro)
def listaPessoas(index=0,todos=False):
    """
    Essa função irá imprimir todos os valores do dicionario OU, caso o parametro 'todos' seja FALSE, iremos imprimir o valor em index (primeiro paratro)
    
    index = Indice do dicionario
    todos = Caso TRUE, iremos imprimir todos os clientes cadastrados no dicionario    
    
    """
    
    if index==0 and todos:    
        for i in range(len(cadastroPessoas["Nome"])):
                print(f"\nNome do cliente: {cadastroPessoas['Nome'][i]}")
                print(f"Valor da casa que o cliente deseja financiar: R${cadastroPessoas['Valor da Casa'][i]}")
                print(f"Salario atual do cliente: R${cadastroPessoas['Salario'][i]}")
                print(f"Quantidade de anos a parcelar: {cadastroPessoas['Anos de parcelamento'][i]} anos")
                print(f"Parcelamento mensal: R${cadastroPessoas['Parcelamento Mensal'][i]}")
                print(f"Resultado: {cadastroPessoas['Resultado'][i]}")
                print("*"*10)
    else:        
        print(f"\nNome do cliente: {cadastroPessoas['Nome'][index]}")
        print(f"Valor da casa que o cliente deseja financiar: R${cadastroPessoas['Valor da Casa'][index]}")
        print(f"Salario atual do cliente: R${cadastroPessoas['Salario'][index]}")
        print(f"Quantidade de anos a parcelar: {cadastroPessoas['Anos de parcelamento'][index]} anos")
        print(f"Parcelamento mensal: R${cadastroPessoas['Parcelamento Mensal'][index]}")
        print(f"Resultado: {cadastroPessoas['Resultado'][index]}")
        print("*"*10)


#Greetings!
cabecalho(cor("Bem vindo ao sistema bancario da Alexa!",35))

#Programa principal
while True:
    
    #Sistema de escolhas
    c=int(input("(1) Cadastrar novos clientes\n(2) Exibir todos os clientes cadastrados\n(3) Exibir em detalhes todos os clientes cadastrados\n(4) Sair do programa\nInsira a sua escolha: "))
    
    #Cadastrando novos clientes
    if c == 1:
        system("cls")
        #Tratamento de erro
        while True:
            #Solicitando o nome do cliente
            nome_cliente = input("Digite seu nome: ")
            
            if nome_cliente.isalpha():
                cadastroPessoas["Nome"].append(nome_cliente)
                break
            else:
                print(cor("Erro! Digite somente palavras! (Ex: Alexa)",31))

        #Tratamentos de erros
        while True:
            try:
                #Solicitando o valor da casa que o usuario deseja comprar
                valor_casa = float(input(f"Olá {nome_cliente}, Digite o valor da casa que deseja financiar: R$"))
                cadastroPessoas["Valor da Casa"].append(f"{valor_casa:.2f}")
                break
            except ValueError:
                print(cor("Erro! Digite somente valores monetarios (Ex: 1500,00)",31))
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa")

        #Tratamentos de erros
        while True:
            try:
                #Solicitando o valor salarial do usuario
                salario=float(input("Digite seu salario: R$"))
                cadastroPessoas["Salario"].append(f"{salario:.2f}")
                break
            except ValueError:
                print(cor("Erro! Digite somente valores monetarios (Ex: 1500,00)",31))
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa")
                
        #Tratamentos de erros
        while True:
            try:
                #Perguntando ao usuario em quantos anos o mesmo irá pagar a casa
                anos_aPagar = int(input("Em quantos anos deseja parcelar: "))
                cadastroPessoas["Anos de parcelamento"].append(anos_aPagar)
                break
            except ValueError:
                print(cor("Erro! Digite somente valores numericos (Ex: 5)",31))
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa")

        #Para calcularmos a prestação, iremos dividir o valor total da casa com a quantidade de anos a pagar, multiplicado por 12 (meses)
        prestacao = valor_casa/(anos_aPagar*12)
        cadastroPessoas["Parcelamento Mensal"].append(f"{prestacao:.2f}")

        #Para calcularmos o minimo necessario para que seja aprovada o financiamento
        minimo = salario*30/100

        #Se o valor da prestação for abaixo ou igual ao minimo de 30% do salario do usuario, a compra é aprovada, caso contrario é negada
        if prestacao <= minimo:
            resultado=cor("Compra Aprovada!",35)
        else:
            resultado=cor("Compra Negada!",31)
        cadastroPessoas["Resultado"].append(resultado)
        print(resultado)

        #Salvando cadastros de clientes
        with open("dados_ex36","w") as arquivo:
            json.dump(cadastroPessoas,arquivo)

    #Exibir todos os clientes cadastrados
    if c == 2:
        system("cls")
        print(cor("Lista de pessoas cadastradas:",35))
        for i,n in enumerate(cadastroPessoas["Nome"]):
            print(f"{i}: {n}")
        c1 = int(input("Insira o valor numerico referente a pessoa para que seja exibida as informações cadastrais da mesma: "))
        listaPessoas(c1)
    
    #Exibir em detalhes todos os clientes cadastrados
    elif c == 3:
        system("cls")
        print(cor("Lista completa e detalhada de todas as pessoas cadastradas",35))
        listaPessoas(todos=True)
    
    #Saindo do programa
    elif c == 4:
        print(cor("Obrigado e volte sempre!",35))
        break
    
    elif c > 4:
        print(cor("Escolha invalida!",31))
        sleep(2)
        system("cls")