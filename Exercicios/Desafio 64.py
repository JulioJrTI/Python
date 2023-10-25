"""Desafio 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

quantNum=0
numeros=[]

def Linhas():
    print("-="*10)

print(f"{c1}Bem vindo ao digitador de numeros da Alexa!{c0}")
while True:    
    while True:
        try:            
            num=int(input("Digite um numero (ou digite 999 para sair): "))
            numeros.append(num)
            quantNum+=1
            break           
        except:
            print(f"{c2}Erro! Digite somente numeros.{c0}")

    esc=["Continuar","Sair do programa"]

    Linhas()
    for i,v in enumerate(esc):
        print(f"({i}) {v}")

    while True:    
        try:
            c=int(input("Digite sua escolha: "))
            if c in [0,1]:
                break
            else:
                print(f"{c2}Erro! Digite somente 1 ou 2.{c0}")
        except:
            print(f"{c2}Erro! Digite somente numeros.{c0}")
    Linhas()
    if c==1:        
        break

numeros_str=" > ".join(map(str,numeros))
print(f"{c1}Foram digitados {quantNum} numeros e",end="")
print(f" a soma entre eles: {numeros_str} é igual a {sum(numeros)}{c0}")
Linhas()
print(f"{c1}Obrigado e volte sempre!{c0}")