"""Desafio 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

numerosGeral=[[],[]]

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

print(f"{c1}Bem vindo ao listador de numeros da Alexa!{c0}")
while True:
    while True:
        try:
            num=int(input("Digite um numero: (Ou digite 0 para sair)"))
            break
        except:
            print(f"{c2}Erro! Digite somente numeros!{c0}")    

    if num==0:
        break
    else:
        if num%2==0:
            numerosGeral[0].append(num)
        elif num%2==1:
            numerosGeral[1].append(num)
        

print(f"Listas gerais: {numerosGeral}")
print(f"Numeros pares: {numerosGeral[0]}")
print(f"Numero impares: {numerosGeral[1]}")