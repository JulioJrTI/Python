"""Desafio 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa."""

#Usando de funções de matematica
import math

#Usando de funções de formatação
from Modulos.Formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Greetings!
cabecalho(cor("Bem vindo ao calculador de Hipotenusa da Prof(a) Alexa!",35))

#Programa principal
while True:
    #Tratamento de erros
    while True:
        try:    
            #Solicitando um valor float para o Cateto Oposto
            ca = float(input("Digite um valor para o Cateto Oposto: "))
            break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos! (Exemplo 4)",31))
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa...",31))
            quit()

    #Tratamento de erros
    while True:
        try:
            #Solicitando um valor float para o Cateto Adjacente
            co = float(input("Digite um valor para o Cateto Adjacente: "))
            break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos! (Exemplo 3)",31))
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa...",31))
            quit()

    #Calculando o valor do Cateto Oposto ao quadrado
    caQuadrado = (ca**2)

    #Calculando o valor do Cateto Adjacente ao quadrado
    coQuadrado = (co**2)

    #Somando os resultados das variaveis acima
    somaCaCo = (caQuadrado+coQuadrado)

    #Calculando a Hipotenusa ao calcular a Raiz Quadrada do valor acima
    hipo=math.sqrt(somaCaCo)
    
    #Imprimindo o resultado da hipotenusa
    cabecalho(f"Em um triângulo retângulo, com um cateto adjacente de {cor(ca)} unidades de medida \ne um cateto oposto de {cor(co)} unidades de medida, a hipotenusa, que é o lado oposto ao ângulo reto, \né calculada como a raiz quadrada da soma dos quadrados dos catetos. \nNo caso dado, a hipotenusa é igual a {cor(hipo)} unidades de medida.",quantC=100)
    
    while True:
        c=str(input("Deseja continuar? [S/N]")).upper()[0]
        
        if c in ["S","N"]:
            break
        else:
            print(cor("Erro! Digite S para continuar o programa ou N para sair!",31))
        
    if c in "N":
        print(cor("Obrigado e volte sempre!",35))
        break