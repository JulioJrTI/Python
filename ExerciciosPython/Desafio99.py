"""Desafio 99: Faça um programa que tenha uma função chamada "maior()", que receba vários parametros com valores inteiros. Seu programa tem que analisar todos os valroes e dizer qual deles é o maior."""

from time import sleep

#Criando a função
def maior(*num): #Usando do *, a função irá receber mais de um numero
    #A variavel do Contador inicialmente irá receber 0
    cont=0 
    
    #A variavel do maior numero irá inicialmente receber 0
    maior=0 
    
    print(f"\nAnalisando os valores passados...")
    
    #Desempacotando os numeros digitados no parametro da função
    for valor in num:
        print(f"{valor}",end=" ",flush=True) #Flush é um efeito cosmetico para o sleep abaixo
        sleep(0.3)
        
        if cont==0: #Primeira parte do loop
            maior=valor
        else:
            if valor > maior:
                maior=valor
        cont+=1
    
    #Imprimindo resumo
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")
    
    print()

#Chamado varias vezes a função com varios numeros
maior(5,6,7,8,9)
maior(6,9)
maior()
