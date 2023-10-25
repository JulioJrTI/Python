"""Desafio 98: Faça um programa que tenha uma função chamda "contador()", que receba tres parametros: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar tres contagens através da função criada:

a) De 1 até 10, de 1 em 1

b) De 10 até 0, de 2 em 2

c) Uma contagem personalizada."""

from time import sleep

def Contador(i,f,p): #Criando uma função para o Inicio, Fim e Passo (pular de quanto em quanto)
    
    if p<0: #Se o valor de passo for menor que 0, o valor inserido irá ser multiplicado por -1
        p*=-1
    if p ==0: #Se o valor de passo for exatamento 0, o valor irá valer 1
        p=1    
    
    print("~"*20)
    print(f"Contagem de {i} até o {f} de {p} em {p}") #Imprimindo a mensangem que irá aparecer ao chamar a função   
    
    if i <f: #Se o inicio for menor que o fim
        cont=i #O valor de contador irá valer o valor do inicio
        while cont<=f: #Enquanto o contador for menor ou igual ao valor de fim
            print(f"{cont}",end=" ") #Iremos imprimir o contador
            sleep(0.5)
            cont+=p #E este contador irá ser sumado pelo valor do fim
        print("FIM!")
    else:
        cont=i #Valor de contador irá valer o valor do inicio
        while cont>=f: #Enquanto o contador for maior ou igual ao fim
            print(f"{cont}",end=" ") #Iremos imprimir o contador
            sleep(0.5)
            cont-=p #E este contador irá ser subtraido pelo valor do fim
        print("FIM!")

Contador(1,10,1) #Contador de 1 a 10, pulando de 1 em 1
Contador(10,0,2) #Contador de 10 a 0, pulando de 2 em 2

print("~"*20)
print(f"Agora é a sua vez de personalizar a contagem!") #Contador customizado
ini=int(input("Inicio: "))
fim=int(input("Fim: "))
pas=int(input("Passo: "))
Contador(ini,fim,pas) #Chamando o contador pelas variaveis acima
print("~"*20)