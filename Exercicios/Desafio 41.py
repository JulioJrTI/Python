"""Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 20 anos: Sênior
-Acima: Master"""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Trabalhando com datas (ano atual, nascimento, idade)
from datetime import date

#Ano Atual
ano_Atual = date.today().year

#Cadastrando todas as informações dos atletas em um dicionario
atletas = {"Nome":[],"Ano de nascimento":[],"Idade":[],"Categoria":[]}

#Greetings
print("Bem vindo a Confederação Nacional de Natação!")

#Nome do atleta
nome_atleta = str(input("Digite o nome do atleta: "))
atletas["Nome"].append(nome_atleta)

#Solicitando o ano de nascimento do atleta
ano_Nascimento = int(input(f"Digite o ano de nascimento do(a) atleta {nome_atleta}: "))
atletas["Ano de nascimento"].append(ano_Nascimento)

#Idade do atleta
idade = (ano_Atual-ano_Nascimento)
print(f"O(a) atleta {nome_atleta}, possui {idade} anos de idade.")
atletas["Idade"].append(idade)

#Verificando a categoria do atleta
if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Junior"
elif idade <= 20:
    categoria = "Senior"
else:
    categoria = "Master"

#Imprimindo a categoria    
print(f"A categoria do atleta {nome_atleta} é {categoria}!")
atletas["Categoria"].append(categoria)