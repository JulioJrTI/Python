"""Desafio 33: Faça um programa que leia três número e mostre qual é o maior e qual é o menor."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cor,cabecalho

#Greetings
cabecalho(cor("Bem vindo ao analizador de numeros maiores e menores da Prof(a) Alexa",35))

#As variaveis de maior e menor irão receber por padrão o valor de 0
maior=menor=0

#Usando loop FOR para solicitarmos dois numeros ao usuario
for n in range(2):
    while True:
        try:
            num = int(input(f"Digite o {n+1}º numero: "))
            break
        except ValueError:
            print(cor("\nErro! Digite somente valores numericos! (Ex: 4)\n",31))
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa.",34)) 
    
    #Na primeira parte do loop, as variaveis de maior e menor irão receber o mesmo valor inserido pelo usuario
    if n==0:
        maior=num
        menor=num
    
    #Na segunda parte do loop, iremos fazer uma comparação
    else: 
        #Se o valor inserido pelo usuario na segunda parte do loop for maior que o valor armazenado na variavel do maior numero, esta mesma variavel irá receber o numero de maior valor        
        if num > maior:
            maior = num
        
        #Se o valor inserido pelo usuario na segunda parte do loop for menor que o valor armazenado na variavel do menor numero, esta mesma variavel irá receber o numero de menor valor
        if num < menor:
            menor = num
        
#Imprimindo os resultados
if maior==menor:
    print(cor("\nO usuario digitou os mesmos numeros, por favor tente novamente.",31))
else:
    print(cor(f"\nApos feita a analize dos numeros digitados, o maior numero digitado foi {maior} e o menor numero digitado foi {menor}.",35))