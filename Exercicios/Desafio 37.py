"""Desafio 37: Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
[1] para binario
[2] para octal
[3] para hexadecimal"""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;31m"
colorEnd="\033[m"


chave1=True
numeros={"Numeros inteiros":[],"Numeros binarios":[],"Numeros octadecimais":[],"Numeros hexadecimais":[]}

print(f"{color1}Bem vindo ao conversor de numeros binarios da Alexa!{colorEnd}")
while True:    
    if chave1==True:
        numero=int(input("Digite um numero qualquer: "))
        numeros["Numeros inteiros"].append(numero)
        chave1=False
    
    while True:    
        print(f"{color1}Escolha o metodo de conversão:")
        c=int(input("[1] para binario\n[2] para octal\n[3] para hexadecimal\n"))

        if c in [1,2,3]:
            break
        print(f"{color3}Input invalido, tente novamente!{colorEnd}")

    if c==1:
        numeroConvertido=bin(numero)
        numeros["Numeros binarios"].append(numeroConvertido)
        print("-="*5)
        print(f"Segue numero convertido para binario: {numeroConvertido}")
        print("-="*5)
    elif c==2:
        numeroConvertido=oct(numero)
        numeros["Numeros octadecimais"].append(numeroConvertido)
        print("-="*5)
        print(f"Segue numero convertido para octadecimal: {numeroConvertido}")
        print("-="*5)
    elif c==3:
        numeroConvertido=hex(numero)
        numeros["Numeros hexadecimais"].append(numeroConvertido)
        print("-="*5)
        print(f"Segue numero convertido para hexadecimal: {numeroConvertido}")
        print("-="*5)    

    while True:    
        c2=int(input(f"{color2}Deseja efetuar nova conversão?\n[1]Converter numero para outra base\n[2]Escolher novo numero\n[3]Sair do programa\n {colorEnd}"))

        if c2 in [1,2,3]:
            break
        print(f"{color3}Input invalido, tente novamente!{colorEnd}")
    
    if c2==1:
        continue
    elif c2==2:
        chave1=True   
    elif c2==3:
        print(f"{color3}Segue lista ordenada de numeros digitados e convertidos:")
        print("Numeros inteiros: ",numeros["Numeros inteiros"])
        print("Numeros binarios: ",numeros["Numeros binarios"])
        print("Numeros octadecimais: ",numeros["Numeros octadecimais"])
        print(f"Numeros hexadecimais: ",numeros["Numeros hexadecimais"])
        print(f"{colorEnd}")
        break

    