"""Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5!=5x4x3x2x1=120"""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

fatorial=1

print(f"{c1}Bem vindo ao calculador de fatoriais da Alexa!{c0}")
while True:
    numero=int(input("Digite um numero: "))    

    print(f"{c2}{numero}{c0}!=",end="")
    for n in range(numero,0,-1):    
        print(f"{c1}{n}{c0}",end="")
        if n > 1:
            print("x",end="")    
        fatorial*=n
    print(f"={c2}{fatorial}{c0}")

    while True:
        print("=-"*10)
        c=str(input("Deseja continuar? [S/N]")).upper()[0]
        print("=-"*10)

        if c in ["S","N"]:
            break
        else:
            print(f"{c2}Erro, digite somente S ou N para continuar ou sair do programa.{c0}")
    
    if c in "S":
        fatorial=1    
    elif c in "N":
        print(f"{c1}Obrigado e volte sempre!{c0}")
        break



