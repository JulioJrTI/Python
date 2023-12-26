"""Desafio 02: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vidas."""

from Modulos import Formatar
from time import sleep

homensLista=[]
mulheresLista=[]

print(Formatar.cor(Formatar.cabecalho("Bem vindo ao cadastrador de pessoas da Alexa!",35),35))
while True:
    while True:
        nomePessoa=str(input("Digite seu nome: (Ou digite exit para sair)\n"))
        if nomePessoa.isalpha():
            break
        else:
            print(Formatar.cor("Erro! Por favor digite um nome!",31))

    if nomePessoa=="exit":
        print("Finalizando o programa...")
        sleep(0)#1        
        print(Formatar.cor(Formatar.cabecalho("Obrigado e volte sempre!"),32))
        sleep(0)#1     
        break
    else:
        print(Formatar.cabecalho(f"Cadastrando {nomePessoa}..."))
        
        sleep(0)#2
        
        if nomePessoa[-1]=="a":
            c=str(input("Vc é uma mulher? [S/N] "))
            if c in "Ss":
                print(Formatar.cor(f"{nomePessoa}! Seja bem vinda ao Python!",35))        
                mulheresLista.append(nomePessoa)
            elif c in "Nn":
                print(Formatar.cor(f"{nomePessoa}, Bem vindo ao Python!",34))
                homensLista.append(nomePessoa)
        else:
            print(Formatar.cor(f"{nomePessoa}, Bem vindo ao Python!",34))
            homensLista.append(nomePessoa)
        
        sleep(0)#2

print(Formatar.cor(Formatar.cabecalho("Exibindo agora a lista de pessoas cadastradas: "),35))

print(Formatar.cor("Homens cadastrados:",34))
if len(homensLista)>=1:
    for i,h in enumerate(homensLista):
        print(f"{i}: {h}")
else:
    print("Não foram cadastrados homens!")
    
print()

print(Formatar.cor("Mulheres cadastradas:",35))
if len(mulheresLista)>=1:
    for i,m in enumerate(mulheresLista):
        print(f"{i}: {m}")
else:
    print("Não foram cadastrados mulheres!")
    
Formatar.linhas()

