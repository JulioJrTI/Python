"""Desafio 26: Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cor,cabecalho

#Greetings!
cabecalho(cor("Bem vindo ao analizador de frases da Prof(a) Alexa!",35))

#Tratamento de erro
while True:
    #Solicitando uma frase qualquer ao usuario
    frase=str(input("Digite uma frase: ")).upper()
    
    if frase.isalpha() or " " in frase:
        break
    else:
        print(cor("\nErro! Por favor digite somente palavras!\n",31))

#Variavel que irá conter a quantidade de vezes que a letra 'A' foi digitada
letraA_quantidade=0

#Fatiando a frase inserida inicialmente e usando loop for para identificar a letra 'a'
for letra_A in frase:
    if letra_A.count("A"):
        letraA_quantidade+=1    

if letraA_quantidade == 0:
    print(cor(f"Seu nome não contem a letra 'A'!",31))
else:
    #Imprimindo a quantidade de vezes a letra 'A' foi digitada    
    print(cor(f"\nA letra 'A' aparece {letraA_quantidade} vezes.",35))

    #Imprimindo a posição que a letra 'A' aparece pela primeira vez
    print(cor(f"\nA letra 'A' aparece pela primeira vez na posição {frase.find("A")+1}º posição.",35))

    #Imprimindo a posição que a letra 'A' aparece pela ultima vez
    print(cor(f"\nA letra 'A' aparece pela ultima vez na posição {frase.rfind("A")+1}º posição.",35))