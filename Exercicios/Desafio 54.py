"""Desafio 54: Crie um programa que leia o ano de nascimento de sete pessoas, No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import datetime

c1="\033[1;32m"
c2="\033[1;33m"
c0="\033[m"

anoAtual=datetime.today().year

dezoitoMais=0 #Iremos armazenar a quantidade de pessoas com mais de 18 anos
dezoitoMenos=0 #Iremos armazenar a quantidade de pessoas com menos de 18 anos

pessoas={"Nome":[],"Idade":[],"Status":[]} #Iremos armazenar todas as informações das pessoas no dicionario

print(f"{c1}Bem vindo a lista de pessoas da Alexa!{c0}")
for p in range(7):
    while True: #Mecanica de erro       
        nomePessoa=str(input(f"Digite seu nome: "))        
        if nomePessoa.isalpha(): #Se o valor digitado acima for PALAVRAS, o programa irá continuar
            break
        else: #Caso contrario, erro.
            print("ERRO! Digite seu nome.")
    
    pessoas["Nome"].append(nomePessoa)
    
    while True: #Mecanica de erro
        try:
            anoNascimento=int(input(f"Olá {c1}{nomePessoa}{c0}, Digite seu ano de nascimento: "))
            break
        except:
            print("ERRO! Digite sua idade em numeros!")
    
    idade=anoAtual-anoNascimento #Iremos saber a idade do usuario ao subtrair o ano atual - o ano de nascimento
    pessoas["Idade"].append(idade)

    print("-="*10)

    if idade >=18:
        dezoitoMais+=1
        pessoas["Status"].append(f"{c1}Maioridade{c0}")
    else:
        dezoitoMenos+=1
        pessoas["Status"].append(f"{c2}Menoridade{c0}")

print(f"{c1}Temos {dezoitoMais} pessoas maiores de 18.{c0}")
print(f"{c2}Temos {dezoitoMenos} pessoas com idade inferior a 18.{c0}")
print("-="*10)

print("Lista de pessoas:")
for i in range(len(pessoas['Nome'])):
    print(f"Nome: {pessoas['Nome'][i]}")
    print(f"Idade: {pessoas['Idade'][i]}")
    print(f"Status: {pessoas['Status'][i]}")
    print("-="*10)
print(f"{c1}<<<< FIM >>>>{c0}")