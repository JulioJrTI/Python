"""Desafio 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

anos={"Ano Bi":[],
      "Ano não bi":[]}

print(f"{color1}Bem vindo ao calculador de anos bissextos da Alexa!{colorEnd}")
while True:       
    
    ano=int(input("Digite o ano que deseja verificar: [0 para sair]"))

    if ano==0:
        break    

    if ano%4==0 and (ano%100!=0 or ano%400==0): #Se o ano for bissexto
        print(f"{color1}O ano {ano} é bissexto{colorEnd}!")
        anos["Ano Bi"].append(ano) #Iremos adicionar o ano digitado a chave 'Ano Bi'
        print("-="*5)

    else:
        print(f"{color2}O ano {ano} não é bissexto{colorEnd}!") #Se o ano não for bissexto
        anos["Ano não bi"].append(ano) #Iremos adicionar o ano digitado a chave 'Ano não Bi'
        print("-="*5)
print("-="*5)

print("Segue lista de anos digitados: ")
print(f"{color1}Anos bissextos: ",end="")
print(f"{anos['Ano Bi']}{colorEnd}")
print("-="*5)
print(f"{color2}Anos não bissextos: ",end="")
print(f"{anos['Ano não bi']}{colorEnd}")
