"""Desafio 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

#Importando funções de formatação e cores
from Modulos.Formatar import cabecalho,cor
from time import sleep

#Limpando o terminal cada execução do programa
from os import system
system("cls")

#Greetings!
cabecalho(cor("Bem vindo ao programa de locação de carros da Alexa!",35))

#Tratamento de erros
while True:
    try:
        #Solicitando ao usuario que insira a quantidade de dias alugados
        quantDias=int(input("Digite a quantidade de dias alugados: "))
        break
    except ValueError:
        print(cor("Erro! Por favor digite um valor numerico valido!",31))
    except KeyboardInterrupt:
        print(cor("\nUsuario encerrou o programa...",31))
        quit()

#Calculando o valor a pagar pela quantidade de dias alugados 
diasPagar=(quantDias*60)
print(f"Total de dias alugados: {quantDias} dias")
print(f"Valor a pagar: R${diasPagar:.2f}")

#Tratamento de erros
while True:
    try:
        #Solicitando ao usuario que insira a quantidade de KMs percorridos
        quantsKm=float(input("\nDigite a quantidade de KMs percorridos: "))
        break
    except ValueError:
        print(cor("Erro! Por favor digite um valor numerico valido!",31))
    except KeyboardInterrupt:
        print(cor("\nUsuario encerrou o programa...",31))
        quit()

#Calculando o valor a pagar pela quantidade de KMs percorridos
kmsPagar=(quantsKm*0.15)
print(f"Total de KMs percorridos: {quantsKm}")
print(f"Valor a pagar: R${kmsPagar:.2f}")

#Calculando total a pagar e imprimindo o resultado
print("\nCalculando valor total...")
sleep(1)
totalPagar=(diasPagar+kmsPagar)
cabecalho(cor(f"Total a pagar: R${totalPagar:.2f}",34),cent=0,quantC=25)