"""Desafio 80: Crie um programa onde o usuário possa digitar cinco valores numérios e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

c1="\033[1;32m"
c2="\033[1;33m"
c0="\033[m"

numeros=[]

print(f"{c1}Bem vindo ao listador de numeros da Alexa!{c0}")
for _ in range(5):
    n=int(input("Digite um numero: (ou digite 0 apra sair)"))
    
    if not numeros:
        numeros.append(n)
        print(f"{c2}Adicionando ao final da lista...{c0}")
    else:
        for pos, num in enumerate(numeros):
            if n<=num:
                numeros.insert(pos,n)
                print(f"{c2}Adicionando na posição {c0}{c1}{pos}{c0} {c1}da lista.{c0}")
                break
        else:
            numeros.append(n)
            print(f"{c2}Adicionando ao final da lista...{c0}")
print("<<< FIM >>>")
print(f"{c1}Os valores digitados em ordem foram {numeros}.{c0}")