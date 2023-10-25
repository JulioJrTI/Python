"""Desafio 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

numeros=[]

print(f"{c1}Bem vindo ao analizador de numeros da Alexa!{c0}")
while True:
    while True:
        try:    
            num=int(input(f"Digite um numero: (Ou digite 0 para sair)"))
            break
        except:
            print(f"{c2}Por favor digite somente numeros.{c0}")

    if num==0:
        break
       
    if num not in numeros:
        numeros.append(num)
    else:
        print(f"Numero repetido!")       


numeros.sort()

print(f"{c1}Segue lista de numeros digitados em ordem crescente: ",end="")
for i,v in enumerate(numeros):    
    if i == len(numeros)-1:
        print(v,end=".")
    else:
        print(v,end=", ")
print(c0)