"""Desafio 05: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor."""

import os
from Modulos.Formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
os.system("cls")

#Iremos armazenar os numeros digitados em uma lista
numeros=[] 

#Chave para verificarmos numeros ou finalizar o programa
chave=True 

#Programa principal
cabecalho(cor("Bem vindo ao analisador de numeros da Alexa!"),63)
while True:
    #Perguntando ao usuario a quantidade de numeros que iremos armazenar em uma lista
    while True:
        try:    
            quantNum = int(input("Deseja digitar quantos numeros: ")) 
            break
        except KeyboardInterrupt: #Caso o usuario cancele o programa no meio de sua execução
            print(cor("Ok, volte sempre!",31))
            quit()
        except: #Caso o usuario digite algo alem de numeros
            print(cor("Por favor digite um valor numerico valido!",31))        
        
    #Perguntando os numeros de acordo com a quantidade desejada acima
    while True:
        try:
            for n in range(quantNum): 
                numeros.append(int(input(f"Digite o {n}º numero: ")))
            print()
            break    
        except KeyboardInterrupt: #Caso o usuario cancele o programa no meio de sua execução
            print(cor("Ok, volte sempre!",31))
            quit()        
        except: #Caso o usuario digite algo alem de numeros, e tambem iremos limpar a lista a cada erro
            numeros.clear()
            print(cor("Erro! Digite um numero valido!",31))
        
    #Lista de numeros digitados
    cabecalho(cor("Segue lista de numeros digitados:",33),53)
    for i, n in enumerate(numeros):
            print(f"{i}º = {n}")    
    
    while chave: #Chave que irá controlar se o usuario deseja verificar mais do que um numero ou sair do programa
        print()        
        c=int(input(f"Deseja verificar qual numero: (Ou digite {cor(len(numeros),31)} para sair)"))
        print()
        
        if c == len(numeros): #Se o usuario digitar o numero escolhido acima para sair do programa
            print(cor("Obrigado e volte sempre!",35))
            chave=False            
        elif c > len(numeros): #Se o usuario digitar um numero (alem do numero de saida) que esteja fora do range da lista
            print(cor(f"Erro! Escolha somente do numero 0 até {len(numeros)-1}",31))                
        else: #Caso entrada esteja correta, iremos exibir o resultado do numero desejado        
            cabecalho(cor(f"O numero {numeros[c]} tem como sucessor o numero {numeros[c]+1} e antecessor o numero {numeros[c]-1}!",34),0)
    
    #Saida do programa        
    break 