"""Desafio 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionarios em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.

B) A media de idade do grupo.

C) Uma lista com todas as mulheres.

D) Uma lista com todas as pessoas com idade acima da média."""

from datetime import date

pessoas={"Nome":[],"Sexo":[],"Idade":[],"Lista de mulheres":[]}

color1="\033[1;32m"
color2="\033[1;31m"
colorF="\033[1;35m"
color0="\033[m"

quantPessoas=0

print(f"{color1}Bem vindo ao cadastrador de pessoas da Alexa!{color0}")
while True:    
    #Nome do usuario
    while True:
        nome=str(input("Digite seu nome: "))
        if nome.isalpha():
            pessoas["Nome"].append(nome)
            break
        else:
            print(f"{color2}Erro! digite seu nome sem inserir numericos!{color0}")        

    #Sexo do usuario
    while True:
        sexo=str(input(f"Olá {nome}, por favor digite seu sexo: [M/F]")).upper()[0]
        if sexo in ["M","F"]:
            pessoas["Sexo"].append(sexo)
            break
        else:
            print(f"{color2}Erro! Digite seu sexo escolhendo M ou F!{color0}")

    #Idade do usuario
    anoAtual=date.today().year
    while True:
        anoNascimento=int(input("Digite seu ano de nascimento: "))
        if len(str(anoNascimento))!=4:
            print(f"{color2}Erro! Digite seu ano de nascimento com 4 digitos!{color0}")
        else:
            idade=(anoAtual-anoNascimento)
            print(f"Vc tem {idade} anos de idade. ")
            pessoas["Idade"].append(idade)
            break

    #Copiando informações para uma lista exclusiva para mulheres
    if sexo=="F":
        mulheres=[nome,sexo,idade]
        pessoas["Lista de mulheres"].append(mulheres)

    #Quantidade de pessoas cadastradas no dicionario
    quantPessoas+=1

    #Opção para continuar cadastrando pessoas
    while True:
        c=str(input("Deseja continuar cadastrando? [S/N]")).upper()[0]
        if c in ["S","N"]:
            break
        else:
            print(f"{color2}Erro! Escolha 'S' para continuar ou 'N' para sair do programa!{color0}")
    
    print()
    
    if c in "Nn":
        break

print()

#Imprimindo a quantidade de pessoas cadastradas no dicionario
print(f"{color1}Foram cadastradas {quantPessoas} pessoas no total.{color0}")

#Media de idade
quantIdade=len(pessoas["Idade"])
somaIdade=sum(pessoas["Idade"])
mediaIdade=(somaIdade/quantIdade)
print(f"{color1}Media de idade de pessoas cadastradas: {mediaIdade}{color0}")

print()

#Resumo geral das pessoas cadastradas
print(f"{color1}Resumo geral:{color0}")
for i in range(len(pessoas["Nome"])):
    print(f"Nome: {pessoas['Nome'][i]}")
    print(f"Sexo: {pessoas['Sexo'][i]}")
    print(f"Idade: {pessoas['Idade'][i]}")
    print("-="*10)

print()

#Imprimindo uma lista exclusiva das mulheres
print(f"{colorF}Lista exclusiva das mulheres:{color0}")
for mulher in pessoas["Lista de mulheres"]:
    print(f"Nome: {mulher[0]}")
    print(f"Sexo: {mulher[1]}")
    print(f"Idade: {mulher[2]}")
    print("-="*10)

print()

#Criando uma lista exclusiva para pessoas com idade acima da media
print(f"{color1}Lista com pessoas com media acima da idade:{color0}")
pessoasAcimaMedia=[]
for i in range(len(pessoas["Nome"])):
    if pessoas["Idade"][i] > mediaIdade:
        pessoasAcimaMediaDict={"Nome": pessoas["Nome"][i],"Sexo":pessoas["Sexo"][i],"Idade":pessoas["Idade"][i]}
        pessoasAcimaMedia.append(pessoasAcimaMediaDict)

#Imprimindo a lista com pessoas acima da media de idade
for pessoa in pessoasAcimaMedia:
    print(f"Nome: {pessoa['Nome']}")
    print(f"Sexo: {pessoa['Sexo']}")
    print(f"Idade: {pessoa['Idade']}")
    print("-="*10)