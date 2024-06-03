"""Desafio 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Criando uma função que irá verificar se um numero é PAR ou IMPAR
def numero_ParImpar(num=0):
    resp=[f"\nO numero {num} é PAR!\n",
          f"\nO numero {num} é IMPAR!\n"]
    
    if num%2==0:
        print(cor(f"{resp[0]}",34))
    else:
        print(cor(f"{resp[1]}",35))

#Greetings!
cabecalho(cor("Bem vindo ao analizador de numeros PAR e IMPAR da Prof(a) Alexa Luzia!",35))

#Programa principal
while True:
    
    #Tratamento de erro
    while True:
        try:
            numero=int(input("Digite um numero qualquer (ou digite 0 para sair): "))
            break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos!",31))
        except KeyboardInterrupt:
            print(cor("\nUsuario cancelou o programa.",34))
            quit()
    
    if numero==0:
        print(cor("Obrigado e volte sempre!",35))
        break
    else:    
        #Chamando da função criada para verificarmos se o valor (inserido como parametro) é par ou impar
        numero_ParImpar(numero)