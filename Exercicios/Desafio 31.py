"""Desafio 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Greetings!
cabecalho(cor("Bem vindo ao preçometro de viagens da Alexa Luzia!",35))

#Tratamento de erros
while True:
    try:
        distanciaKM = int(input("Digite a distancia de sua viagem (Km): "))
        break
    except ValueError:
        print(cor("Erro! Digite somente valores numericos!",31))
    except KeyboardInterrupt:
        print("\nO usuario cancelou o programa.")
        quit()

#Calculando valor a pagar de acordo com a quantidade KMs percorridos
if distanciaKM <=200:
    aPagar = distanciaKM*0.50
else:
    aPagar = distanciaKM*0.45
    
#Imprimindo valor a pagar
print(cor(f"Valor total a pagar em uma viagem de {distanciaKM}KMs: R${aPagar:.2f}",35))