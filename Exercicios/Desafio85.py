"""Desafio 85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

numeros=[[],[]]

print(f"{c1}Bem vindo ao listador de numeros pares e impares da Alexa!{c0}")
for n in range(7):
    while True:
        try:
            num=int(input(f"Digite o {n+1}º numero: "))
            break
        except:
            print(f"{c2}Erro! Por favor digite somente numeros!{c0}")

    if num%2==0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

#Ordernar Listas
numeros[0]=sorted(numeros[0])
numeros[1]=sorted(numeros[1])

#Numeros pares
print(f"{c1}Numeros Pares: {c0}",end="")
for i, numerosPares in enumerate(numeros[0]):
    if i<len(numeros[0])-1:
        print(f"{numerosPares}",end=", ")
    else:
        print(f"{numerosPares}.")

#Numeros impares
print(f"{c1}Numeros Impares: {c0}",end="")
for i,numerosImpares in enumerate(numeros[1]):
    if i<len(numeros[1])-1:
        print(f"{numerosImpares}",end=", ")
    else:
        print(f"{numerosImpares}",end=".")