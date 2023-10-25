"""Desafio 65: Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

def Linhas():
    print("-="*10)

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

maiorNum=0
menorNum=0

numLista=[]

print(f"{c1}Bem vindo ao calculador de maior, menor e media de numeros da Alexa!{c0}")
Linhas()
while True:
    while True:
        try:
            num=int(input("Digite um numero: "))
            numLista.append(num)
            break
        except:
            print(f"{c2}Erro! Digite somente numeros!{c0}")


    if maiorNum==0 or num>maiorNum:
        maiorNum=num
    if menorNum==0 or num<menorNum:
        menorNum=num    

    while True:        
        c=str(input("Deseja continuar? [S/N]")).upper()[0]
        if c.isalpha() and c in ["S","N"]:
            break  
        print(f"{c2}Erro! Digite somente S ou N!{c0}")    
    Linhas() 
    if c in "N":        
        break 

quantLista=len(numLista)
somaLista=sum(numLista)
media=somaLista/quantLista
print(f"O maior numero lido foi o numero {c1}{maiorNum}{c0}.")
print(f"O menor numero lido foi o numero {c1}{menorNum}{c0}.")
print(f"A media entre os numeros digitado é {c1}{media}{c0}.")
print(f"{c1}Obrigado e tenha um bom dia!{c0}")


