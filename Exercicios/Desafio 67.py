"""Desafio 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usúario. O programa será interrompido quando o número solicitado for negativo."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas():
    print("-="*10)

print(f"{c1}Bem vindo ao calculador de Tabuadas da Alexa!{c0}")
while True:    
    while True:
        try:
            num=int(input("Tabuada: (ou digite 0 para sair)"))
            break
        except:
            print(f"{c2}Erro! Digite somente numeros!{c0}")

    if num==0:
        print(f"{c1}Obrigado e volte sempre!{c0}")
        break
    
    Linhas()
    print(f"Segue tabuada do {num}:")
    for n in range(1,11):
        print(f"{num}x{n}={num*n}")
    Linhas()
