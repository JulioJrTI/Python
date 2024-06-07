"""Desafio 51: Desenvolva um programa que leia o primeiro termos e a razão de uma PA (Progressão Aritmetica). No final, mostre os 10 primeiros termos dessa progressão."""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;31m"
colorEnd="\033[m"

PAs={"PAs digitadas":[]} #Iremos armazenar as PAs dentro de listas em um dicionario

print(f"{color1}Bem vindo ao calculador de PAs da Alexa!{colorEnd}")
while True:
    PAsLista=[] #Cada PA irá ser armazenada em uma lista
    n1=int(input("Digite um numero: "))
    n2=int(input("De quanto em quanto iremos pular: "))    
        
    for n in range(1,11):
        pa=n1+(n-1)*n2
        if n==10: #Iremos tirar o ">" do ultimo valor da PA           
            print(f"{color1}{pa}{colorEnd}",end="")  
        else:        
            print(f"{color1}{pa}{colorEnd}",end=" > ")    
        PAsLista.append(pa)
    
    PAs["PAs digitadas"].append(PAsLista) #Armazenando todas listas de PAs em um dicionario    
    
    while True: #Mecanica de erro
        c = str(input("\nDeseja continuar? [S/N]")).upper()[0]
        if c in "SN":
            break
        print(f"{color3}Erro! Digite S ou N.{colorEnd}")
    if c in "Nn":        
        print(f"{color1}<<<<< Volte Sempre >>>>>{colorEnd}")
        break

print("=-"*10)
print(f"{color1}PAS digitadas: {colorEnd}") #Exibindo todas as PAs digitadas na ordem, armazenadas em listas dentro de um dicionario
for i,pa_Lista in enumerate(PAs["PAs digitadas"]):
    print(f"{color2}PA {i}: {pa_Lista}{colorEnd}")