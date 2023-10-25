"""Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

-Até 9 anos: Mirim

-Até 14 anos: Infantil

-Até 19 anos: Junior

-Até 20 anos: Sênior

-Acima: Master"""

from datetime import date

color1="\033[1;32m"
color2="\033[1;33m]"
colorEnd="\033[m"

anoAtual=date.today().year

atleta={"Nome do atleta":[],"Idade":[],"Ranking":[]}
print(f"{color1}Bem vindo as olimpiadas de natação da Alexa!{colorEnd}")
while True:
    nome=input("Digite o nome do atleta: ")
    atleta["Nome do atleta"].append(nome)

    anoNascimento=int(input("Em qual ano vc nasceu: "))
    idade=anoAtual-anoNascimento
    atleta["Idade"].append(idade)    

    if idade <=9:
        ranking="Mirim"        
    elif idade <=14:
        ranking="Infantil"        
    elif idade <=19:
        ranking="Junior"        
    elif idade==20:
        ranking="Senior"        
    else:
        ranking="Master"        
    atleta["Ranking"].append(ranking) 
    
    print("Ranking: ",ranking)    
    
    c = str(input("Deseja continuar? [S/N]"))

    if c in "Nn":
        break
print()
print(f"{color1}Lista de atletas:{colorEnd}")
for i in range(len(atleta["Nome do atleta"])):
    print(f"Nome do atleta: {atleta['Nome do atleta'][i]}")
    print(f"Idade: {atleta['Idade'][i]}")
    print(f"Ranking: {atleta['Ranking'][i]}")
    print("-="*10)


