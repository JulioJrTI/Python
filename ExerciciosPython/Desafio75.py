"""Desafio 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

print(f"{c1}Bem vindo ao contador de numeros da Alexa!{c0}")

n1=int(input("Digite o primeiro numero: ")) #Pedindo o primeiro numero
n2=int(input("Digite o segundo numero: ")) #Pedindo o segundo numero
n3=int(input("Digite o terceiro numero: ")) #Pedindo o terceiro numero
n4=int(input("Digite o quarto numero: ")) #Pedindo o quarto numero
numeros=(n1,n2,n3,n4) #Armazenando os 4 numeros em uma tupla

#Posição do primeiro valor 3
if 3 in numeros: #Se for encontrado o numero 3 na tupla
    numeroTres=numeros.index(3) #Iremos saber o index do numero 3
    print(f"{c1}O numero 3 aparece pela primeira vez no {numeroTres}º index.{c0}")
else: #Caso o numero 3 nao tenha sido inserido
    print(f"{c2}O numero 3 não foi digitado.{c0}")

#Quantas vezes apareceu o valor 9
if 9 in numeros: #Se for encontrado o numero 9
    numeroNove=numeros.count(9) #Contando a quant de numeros 9 na lista
    print(f"{c1}O numero 9 apareceu {numeroNove} vezes.{c0}")
else: #Caso o numero 9 nao tenha sido inserido
    print(f"{c2}O numero 9 não foi digitado.{c0}")

#Lista de numeros pares
numerosPares=[] #Iremos armazenar os numeros pares em uma lista
for numeroPar in numeros: #Usando identação para com a tupla
    if numeroPar%2==0: #Caso haja numeros pares na tupla
        numerosPares.append(numeroPar) #Iremos armazenar esses numeros na lista

if numerosPares: #Caso a lista de numeros pares não esteja vazia
    print(f"{c1}Lista de numeros pares inseridos: {numerosPares}.{c0}")
else: #Caso contrario
    print(f"{c2}Não foram digitados numeros pares.{c0}")
    
