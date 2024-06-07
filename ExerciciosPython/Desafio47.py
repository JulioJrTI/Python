"""Desafio 47: Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Greetings!
cabecalho(cor("Bem vindo ao calculador de pares e impares da Prof(a) Alexa!",35))

#Função que irá imprimir numeros pares usando parametros como pontos de inicio e final
def print_num_pares(n=0,f=0):
    """
    Calculando os numeros pares seguindo valores de inicio e fim (parametros)
    Parametros: n=(numero inicial), f=(numero final)
    
    """
    
    #Calculando os numeros pares e os imprimindo
    if f==0:
        print(cor("Erro! Insire um valor final no segundo parametro!",31))
    else:
        #Imprimindo os numeros pares
        print(cor(f"Numeros pares de {n} a {f}:",35).center(65))
        for num in range(n,f+1):
            if num%2==0:
                print(num,end=" > ")
        print("\b\b ")

#Chamando da função para imprimirmos os numeros pares de 0 a 50
print_num_pares(0,50)