"""Desafio 66: Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas():
    print("-="*10)

numLista=[]
numTotal=0
numSoma=0
num=0

print(f"{c1}Bem vindo ao somador de numeros da Alexa!{c0}")
while True:   
    while True:
        try:
            num=int(input("Digite um numero: (ou digite 999 para sair)"))
            break           
        except:
            print(f"{c2}Erro! Digite somente numeros!{c0}")
    
    if num!=999:
        numTotal+=1
        numSoma+=num
        numLista.append(num)    
    elif num==999:
             break

Linhas()
print("Segue numeros digitados e sua soma entre eles: ")
simboloEsp=" + ".join(map(str,numLista))
print(f"{simboloEsp} = {numSoma}")
Linhas()
print(f"Foram digitados {numTotal} numeros no total.")
Linhas()
print(f"{c1}Obrigado e tenha um bom dia!{c0}")