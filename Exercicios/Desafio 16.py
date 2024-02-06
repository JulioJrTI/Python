"""Desafio 16: Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Exemplo: Digite um numero: 6.127. O numero 6.127 tem a parte inteira 6."""

#Biblioteca Matematica
import math

#Biblioteca usada para carregamento e armazenamento de informações
import json

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Função que irá arredondar um numero float
def numInt(n=0):
    numeroInt = math.floor(n)
    return numeroInt

#Funções de formatação
from Modulos.Formatar import cabecalho,cor

#Sistema de carregamento de informações
try:
    with open('DadosDesafio16.json','r') as arquivo:
        numDigitados = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado, criando um novo!")
    #Dicionario que irá converter os valores digitados e resultados de conversões
    numDigitados={"Numeros digitados":[],"Resultados das conversoes":[]}

#Greetings!
cabecalho(cor(("Bem vindo ao conversor de numeros da Alexa!"),35))

#Programa principal
while True:
    
    #Tratamentos de erros
    while True:
        try:
            #Solicitando um valor float (inicialmente, esta variavel será String) ao usuario 
            numReal = input("Digite um valor numerico real (Exemplo 6.127): ")
            break
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa...",31))
            quit()
        except ValueError:
            print(cor("Erro! Por favor digite somente valores numericos reais! (Exemplo 6.127)",31))
    
    #Tratamento de erro, se o usuario inserir uma virgula, iremos substituir essa virgula por um ponto
    if "," in numReal:
        numReal = numReal.replace(",",".")
    
    #Convertendo a variavel String para Float
    numReal = float(numReal)    
    
    #Armazenando o valor digitado pelo usuario em um dicionario
    numDigitados["Numeros digitados"].append(numReal)
    
    #Chamando da função que irá converter o valor digitado acima e retornando o resultado
    nInt=numInt(numReal)
    
    #Imprimindo o resultado
    cabecalho(f"O numero {numReal} tem a parte inteira {nInt}",cent=0,quantC=40)
    
    #Armazendo o resultado da conversão em um dicionario
    numDigitados["Resultados das conversoes"].append(nInt)
    
    #Sistema de salvamento de informações
    with open('DadosDesafio16.json','w') as arquivo:
        json.dump(numDigitados,arquivo)    
    
    #Tratamento de erros
    while True:            
        try:
            c = str(input("Deseja continuar? [S/N]")).upper()[0]
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa...",31))
            quit()        
        if c in ["S","N"]:
            break
        else:
            print(cor("Erro! Digite 'S' para continuarmos o programa ou 'N' para sairmos!"))            
    
    #Saindo do programa caso o usuario deseje
    if c in "Nn":
        print(cor("Obrigado e volte sempre!\n",35))
        break

#Exibindo o conteudo inserido no dicionario
cabecalho(cor("Resumo geral de numeros digitados e conversões:",35))
for num_digitado, resultado_conversao in zip(numDigitados["Numeros digitados"],numDigitados["Resultados das conversoes"]):
    print(f"Numero: {num_digitado}\t | Conversão: {resultado_conversao}")