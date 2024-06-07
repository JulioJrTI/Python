"""Desafio 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo."""

#Limpando o terminal cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Greetings
cabecalho(cor("Bem vindo ao analizador de triangulos da Prof(a) Alexa",35))

#Iremos armazenar as retas digitadas pelo usuario em uma lista
retas=[]

#Loop FOR, que irá solicitar ao usuario 3 numeros, e iremos armazena-los em uma lista
for i in range(3):    
    #Tratamento de erros
    while True:
        try:
            #Variavel será inicializada como STRING
            reta=input(f"Insira a {i+1}º reta: ")            
            
            #Se o usuario digitar uma virgula em vez de um ponto, iremos substituir essa virgula por um ponto
            if "," in reta:
                reta = reta.replace(",",".")
            
            #Convertendo a varivel STRING para FLOAT
            reta=float(reta)
            
            #Inserindo o valor digitado pelo usuario para uma lista
            retas.append(reta)
            break
        except ValueError:
            print(cor("Erro! Não digite valores alem de numeros!",31))
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa",34))
            quit()
    
#Formula matematica para descobrirmos se as retas inseridas pelo usuario podem ou não formar um triangulo
if (retas[0] + retas[1] > retas[2]) and (retas[2] + retas[0] > retas[1]) and (retas[2] + retas[1] > retas[0]):
    print(cor("Pode formar um triangulo",35))
else:
    print(cor("Não pode formar um triangulo",31))