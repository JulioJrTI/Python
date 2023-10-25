"""Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

chave=True

numeros=list()

print("Bem vindo a calculadora da Alexa!")
while True:
    while chave:
        for n in range(2):
            numero=int(input(f"Digite o {n+1}º numero: "))
            numeros.append(numero)
            chave=False
    sleep(2)
    print("O que deseja fazer com estes numeros?")    
    c1=int(input(" \
    [1] Somar\n \
    [2] Multiplicar\n \
    [3] Maior\n \
    [4] Novos numeros\n \
    [5] Sair do programa\n"))
        
    print("-="*10)
    if c1==1:
        soma=numeros[0]+numeros[1]
        print(f'A soma dos numeros digitados é igual a {soma}.')
    elif c1==2:
        multip=numeros[0]*numeros[1]
        print(f'A multiplicação dos numeros digitados é igual a {multip}.')
    elif c1==3:
        maiorN=max(numeros[0],numeros[1])
        print(f'O maior numero entre os numeros digitados é {maiorN}.')
    elif c1==4:
        numeros.clear()
        chave=True
        print('Digite os novos numeros: ')        
    elif c1==5:
        print('Obrigado e volte sempre!')
        break
    print("-="*10)

