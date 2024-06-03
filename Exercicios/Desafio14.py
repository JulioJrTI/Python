"""Desafio 14: Escreva um programa que converta uma temperatura digita em ºC e converta para ºF."""

#Usando algumas funções de formatação
from Modulos.Formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Greetings!
cabecalho(cor("Bem vindo ao conversor de temperaturas da Prof(a) Alexa!",35))

#Função que irá converter um valor de temperatura ºC para ºF
def conversaoF(temp=0):
    #Se não inserirmos um valor como parametro, iremos solicitar o mesmo ao usuario
    if temp==0:
        while True:
            try:
                #Solicitando um valor de temperatura ºC ao usuario
                temp=int(input("Digite uma temperatura em ºC: "))
                break            
            except ValueError:
                print(cor("Erro! Por favor digite um valor valido (Por exemplo 32, para 32ºC)",31))
            except KeyboardInterrupt:
                print(cor("\nUsuario encerrou o programa...",31))
                quit()
    CpF = temp*9/5+32
    return f"{temp}ºC é igual a {CpF}ºF"

#Programa principal
while True:
    #Tratamento de erro
    while True:
        try:
            #Solicitando um valor de temperatura ºC ao usuario
            t=int(input("Digite uma temp: "))
            break        
        except ValueError:
            print(cor("Erro! Por favor digite um valor valido (Por exemplo 32, para 32ºC)",31))
        except KeyboardInterrupt:
            print(cor("\nUsuario encerrou o programa...",31))
            quit()
    
    #Imprimindo o resultado
    cabecalho(cor(conversaoF(t),35),cent=0,quantC=25)
    
    #Tratamento de erro
    while True:
        #Escolha do usuario se deseja ou não continuar o programa
        c=str(input("Deseja continuar? [S/N]")).upper()[0]
        
        if c in ["S","N"]:
            break
        else:
            print(cor("Erro! Por favor escolha S (para continuar o programa) ou N (para sairmos do programa)!",31))
    
    if c in "Nn":
        print(cor("Obrigado e volte sempre!",35))
        break