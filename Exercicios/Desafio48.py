"""Desafio 48: Faça um programa que calcule a soma entre todos os numeros impares 
que são multiplos de tres e que se encontram no intervalo de 1 até 500."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Greetings!
cabecalho(cor("Bem vindo ao somador de numeros impares da Prof(a) Alexa!",35))

#Criando uma função que irá somar e exibir numeros impares que são multiplos de 3
def somar_numerosImpares(i=0,f=0,m=3):
    
    """
    Iremos somar os numeros impares que são multiplos por 3
    Parametros: i=(Numero inicial),f=(Numeros final),m=(Multiplos, por padrão será multiplos de 3)
    
    """
    
    if f==0:
        print(cor("Erro! Digite um valor numerico final no segundo parametro!",31))
    else:
        #Variavel irá receber a soma de todos os numeros impares que são multiplos de tres
        somaNumeros=0

        print(cor(f"Numeros impares de {i} a {f} que são multiplos de {m} e seu resultado de soma: ",34,),end="")
        
        #Usando loop FOR para calcularmos os numeros impares multiplos de tres
        for num in range(i,f+1):
            if num%2==1 and num%m==0:
                print(num,end=" > ")
                somaNumeros+=num

        #Imprimindo resultado da soma        
        print(f"\b\b= {cor(somaNumeros)}")
    
#Chamando da função criada
somar_numerosImpares(1,500)        