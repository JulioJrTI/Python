from random import randint
from time import sleep

#Definindo uma lista
numeros=list()
 
#Definindo uma função que irá acrescentar a lista acima numeros aleatorios
def sorteia(lista):
    print("Sorteando 5 valores na lista: ",end="")
    for cont in range(0,5): #Iremos pedir 5 numeros aleatorios
        n=randint(1,10)
        lista.append(n) #Adicionando os numeros aleatorios a lista anexada a função
        print(f"{n}",end=" ",flush=True)
        sleep(0.3)
    print("PRONTO!")

#Definindo uma função que irá identificar os numeros pares da função acima e soma-los
def somaPar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f"Somando os valores pares de {lista}, temos {soma}.")

#Imprimindo a função de numeros aleatorios
sorteia(numeros)

#Imprimindo a função que irá identificar os numeros pares da função acima e soma-los
somaPar(numeros)