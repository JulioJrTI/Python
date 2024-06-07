"""Desafio 63: Escreva um programa que leia um número n inteiro qualquer e mostre na tela o n primeiro elementos de uma Sequencia de Fibonacci.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8"""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas():
    print("-="*10)

seqDic={"Numeros digitados":[],"Sequencias":[]}

print(f"{c1}Bem vindo ao calculador de sequencias fibonacci da Alexa!{c0}")
while True:
    while True:    
        try:
            quant=int(input("Digite a quantidade de numeros que iremos exibir: "))
            seqDic["Numeros digitados"].append(quant)
            break
        except:
            print(f"{c2}Erro, digite somente numeros!{c0}")       
    
    t1=0
    t2=1
    cont=3

    sequencia=[t1,t2]
    Linhas()
    print(f"Sequencia de {quant}:")
    print(f"{t1} > {t2} > ",end="")
    while cont<=quant:
        t3=t1+t2
        sequencia.append(t3)
        print(f"{t3}",end=" > ")
        t1=t2
        t2=t3
        cont+=1
    print("FIM")    
    Linhas()
    
    seqDic["Sequencias"].append(sequencia)
    
    escolhas=["Continuar"],["Sair do programa"]

    for i,Escolhas in enumerate(escolhas):
        print(f"({i}) {Escolhas}")

    while True:
        try:
            c=int(input())
            break
        except:
            print(f"{c2}Erro, digite somente numeros!{c0}")

    if c==1:
        break

print(f"{c1}Segue resumo de sequencias de fibonacci: {c0}")
Linhas()
for i in range(len(seqDic["Numeros digitados"])):
    print(f"Quantidade inserida: {seqDic['Numeros digitados'][i]}")
    sequencia=seqDic["Sequencias"][i]
    sequencia_str=" > ".join(map(str,sequencia))
    print(f"Sequencias: {sequencia_str}",end="")
    print(" > FIM")
    Linhas()
print(f"{c1}Obrigado e volte sempre!{c0}")
