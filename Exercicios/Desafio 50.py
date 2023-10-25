"""Desafio 50: Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o."""

color1="\033[1;32m"
color2="\033[1;33m"
colorRed="\033[1;31m"
colorEnd="\033[m"

numeros={"Numeros Pares":[],"Numeros Impares":[]} #Iremos armazenar os numeros pares e impares em listas dentro de um dicionario

print(f"{color1}Bem vindo ao programa identificador de pares e impares da Alexa!{colorEnd}")
for n in range(0,6): #Pedindo 6 numeros, de 0 a 5
    while True: #Mecanica de erro    
        try: #Se qualquer valor digitado não for um integer, ele irá exibir uma mensagem de erro
            num=int(input(f"Digite o {n+1}º numero: "))        
            break
        except:
            print(f"{colorRed}Input errado, por favor digite uma int{colorEnd}")
    
    if num%2==0: #Numeros pares serão armazenados em uma lista dentro de um dicionario
        numeros["Numeros Pares"].append(num)  
    else: #Numeros impares serão armazenados em uma lista dentro de um dicionario
        numeros["Numeros Impares"].append(num)

print("-="*10)    
for k,v in numeros.items(): #Exibindo keys e valores usando loop FOR
    print(f"{k}: {v}")
print(f"{color2}<<< Volte sempre! >>>{colorEnd}")