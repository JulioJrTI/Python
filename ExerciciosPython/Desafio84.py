"""Desafio 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves."""

from tabulate import tabulate

color_1="\033[1;32m"
color_2="\033[1;31m"
color_Reset="\033[m"

pessoas={"Nome":[],"Peso":[],"Pessoas de Maior Peso":[],"Pessoas de Menor Peso":[]}
quantPessoas=0

print(f"{color_1}Bem vindo ao listador de pesos da Alexa!{color_Reset}")
while True:
    pessoaNome=str(input("Digite seu nome: "))
    pessoas['Nome'].append(pessoaNome)

    pessoaPeso=float(input(f"Olá {pessoaNome} Digite seu peso: "))
    pessoas["Peso"].append(pessoaPeso)

    quantPessoas+=1  

    if quantPessoas==1 or pessoaPeso>pessoas["Pessoas de Maior Peso"][1]:
        pessoas["Pessoas de Maior Peso"]=[pessoaNome,pessoaPeso]
    if quantPessoas==1 or pessoaPeso<pessoas["Pessoas de Menor Peso"][1]:
        pessoas["Pessoas de Menor Peso"]=[pessoaNome,pessoaPeso]
    
    c=str(input("Deseja continuar cadastrando? [S/N]:"))

    if c in "Nn":
        print()
        break

#Quantidade de Pessoas cadastradas no dicionario
print(f"{color_1}Foram cadastradas {quantPessoas} pessoas na lista:")

#Transformando o dicionario em uma lista
tabela=list(zip(pessoas["Nome"],pessoas["Peso"]))

#Criando uma tabula com a lista/dicionario
print(tabulate(tabela,headers=["Nome","Peso"],tablefmt="grid"))

#Resumindo a pessoa mais pesada
print(f"Pessoa mais pesada: {pessoas['Pessoas de Maior Peso'][0]} com {pessoas['Pessoas de Maior Peso'][1]}kg.")

#Resumindo a pessoa mais leve
print(f"Pessoa mais leve: {pessoas['Pessoas de Menor Peso'][0]} com {pessoas['Pessoas de Menor Peso'][1]}kg.{color_Reset}")