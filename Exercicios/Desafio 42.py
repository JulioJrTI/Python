"""Desafio 42: Refaça o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
-Equlaterio: Todos os lados iguais
-Isosceles: Dois lados iguais
-Escaleno: Todos os lados diferentes

Desafio 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.

"""

#Limpando o terminal a cada execução do programa
from os import system

#Usando modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Chamando da função que irá calcular as retas de um triangulo
from Modulos.matematica import retas_triangulo

system("cls")

#Greetings!
cabecalho(cor("Bem vindo ao calculador de triangulos da Prof(a) Alexa!",35))

#Programa principal
while True:
    
    #Adicionando as retas a uma lista temporaria
    retas=[]

    #Solicitando retas de um triangulo ao usuario
    for i in range(3):
        while True:
            try:
                reta=float(input(f"Digite a {i+1}º reta: "))        
                retas.append(reta)
                break
            except ValueError:
                print(cor("\nErro! Digite somente valores numericos (Exemplo: 3.69)\n",31))
            except KeyboardInterrupt:
                print(cor("\nO usuario encerrou o programa..."))
                quit()     
            

    #Imprimindo o tipo usando da função criada para calcularmos o triangulo
    if retas_triangulo(retas[0],retas[1],retas[2]):
        if retas[0]==retas[1]==retas[2]:
            print(cor("Equalaterio!",34))
        elif retas[0]==retas[1] or retas[0]==retas[2] or retas[1]==retas[2]:
            print(cor("Isosceles!",33))
        else:
            print(cor("Escaleno!",35))
            
            
    #Continuar ou não o programa
    c = str(input("\nDeseja continuar? [S/N]")).upper()[0]
    print()
    
    if c in "N":
        print(cor("\nOBRIGADO E VOLTE SEMPRE!",35))
        break