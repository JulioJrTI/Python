"""Desafio 86: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

numeros=[[],[],[],[],[],[],[],[],[]]

print(f"{c1}Bem vindo ao organizador de numeros da Alexa!{c0}")
for n in range(9):
    while True:
        try:
            num=int(input(f"Digite o {n+1}º numero: "))
            numeros[n].append(num)
            break
        except:
            print(f"{c2}Erro! Por favor digite somente numeros!{c0}")

#Organizando os numeros em ordem crescente
numeros.sort()

print(f"{c1}Segue lista de numeros digitados:{c0}")
print(*numeros[0:3],sep="")
print(*numeros[3:6],sep="")
print(*numeros[6:9],sep="")
