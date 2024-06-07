"""Desafio 69: Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.

B) Quantos homens foram cadastrados."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas(msg):
    l=len(msg)
    print("~"*l)

pessoas={"Nome":[],"Sexo":[],"Idade":[]}

pessoasIdade18=[]
pessoasHomens=[]

print(f"{c1}Bem vindo ao cadastrados de pessoas da Alexa!{c0}")
while True:
    while True:
        nome=str(input("Digite seu nome: "))
        if nome.isalpha():
            pessoas["Nome"].append(nome)
            break
        else:
            print(f"{c2}Erro! Digite somente palavras!{c0}")        
    
    while True:        
        sexo=str(input(f"Olá {c1}{nome}{c0}, digite seu sexo: [M/F]")).upper()[0]
        if sexo.isalpha() and sexo in ["M","F"]:        
            pessoas["Sexo"].append(sexo)
            break
        else:
            print(f"{c2}Erro! Digite somente M ou F!{c0}")            
    
    while True:
        try:
            idade=int(input("Digite sua idade: "))
            pessoas["Idade"].append(idade)
            break
        except:
            print(f"{c2}Erro! Digite somente numeros!{c0}")

    if sexo=="M":
        homem=[nome,sexo,idade]
        pessoasHomens.append(homem)
    if idade>=18:
        dezoito=[nome,sexo,idade]
        pessoasIdade18.append(dezoito)
    

    c=str(input("Deseja continuar cadastrando? [S/N]")).upper()[0]

    if c in "Nn":
        break

print()
print(f"{c1}Segue lista de pessoas cadastradas:{c0}")
print(f"{c2}Total: {len(pessoas['Nome'])}{c0}")
for i in range(len(pessoas["Nome"])):
    print(f"Nome: {pessoas['Nome'][i]}")
    print(f"Sexo: {pessoas['Sexo'][i]}")
    print(f"Idade: {pessoas['Idade'][i]}")
    Linhas(f"{c1}{pessoas['Nome'][i]}{c0}")

if len(pessoasIdade18)<1:
    print("Não foram cadastradas pessoas com idade superior ou igual a 18.")
else:
    print(f"{c1}Lista de pessoas com idade superior ou igual a 18:{c0}")
    print(f"{c2}Total: {len(pessoasIdade18)}{c0}")
    for pessoas in pessoasIdade18:
        nome,sexo,idade=pessoas
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Idade: {idade}")
        Linhas(nome)    

if len(pessoasHomens)<1:
    print("Não foram cadastrados homens.")
else:
    print(f"{c1}Homens cadastrados na lista:{c0}")
    print(f"{c2}Total: {len(pessoasHomens)}{c0}")
    for homens in pessoasHomens:
        nome,sexo,idade=homens
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Idade: {idade}")
        Linhas(nome)

print(f"{c1}<<<< Fim >>>>{c0}")