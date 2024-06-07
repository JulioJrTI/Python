"""Desafio 98: Faça um programa que tenha uma função chamda "contador()", que receba tres parametros: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar tres contagens através da função criada:

a) De 1 até 10, de 1 em 1

b) De 10 até 0, de 2 em 2

c) Uma contagem personalizada."""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
color0="\033[m"

#Criando a função
def contador(ini,fim,step):    
    
    #Mecanica de erro, se o usuario digitar algum valor abaixo de 1, este valor irá valer como "0"
    if step < 0:
        step*=-1
    
    if step==0:
        step=1

    #Imprimindo as regras da função
    print(f"Contador de {ini} a {fim}, de {step} em {step} passos: ",end="")
    
    #Condição para o contador
    if ini < fim:
        contador=ini
        while contador <= fim:
            print(contador,end=" > ")
            contador+=step
        print("FIM")        
    else:
        contador=ini
        while contador>=fim:
            print(contador,end=" > ")
            contador-=step
        print("FIM") 
    
print(color1)

#Contador de 1 a 10, de 1 em 1
contador(1,10,1)

print(color2)

#Contador de 10 a 0, de 2 em 2
contador(10,0,2)

print(color3)

#Contador customizado
comeco=int(input("De qual numero iremos começar o contador: "))
final=int(input("Qual será o numero final: "))
passo=int(input("Qual sera o intevalo na contagem: "))
contador(comeco,final,passo)

print(color0)