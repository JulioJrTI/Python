"""Desafio 61: Refaça o DESAFIO 51, lendo o primeiro termos e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas():
    print("=-"*20)

termo=0

print(f"{c1}Bem vindo ao contador de PAs da Alexa! 2.0{c0}")
while termo!=10:
    while True:
        try:
            n1=int(input("Digite o numero inicial: "))
            n2=int(input("De quanto em quantos numeros iremos pular: "))
            break
        except:
            print(f"{c2}Erro! Digite somente numeros.{c0}")
    
    Linhas()
    for n in range(1,11):
        pa=n1+(n-1)*n2
        if n==10:
            print(f"{pa}",end=" > FIM")
        else:   
            print(f"{pa}",end=" > ")
    print()
    Linhas()
    
    termo+=1

    while True:    
        c=str(input("Deseja efetuar nova verificação? [S/N]")).upper()[0]

        if c.isalpha() and c in ["S", "N"]:
            break
        else:
            print(f"{c2}Erro! Digite somente S ou N{c0}")

    if c in "Nn":
        print(f"{c1}Obrigado e tenha um dia!{c0}")
        break
