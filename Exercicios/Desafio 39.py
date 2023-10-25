"""Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

-Se ele ainda vai se alistar ao serviço militar.

-Se é a hora de se alistar.

-Se já passou do tempo do alistamento.

Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

from datetime import date

pessoas={"Nomes":[],"Ano de nascimento":[],"Idade":[],"Ano de alistamento":[]}

print(f"{color1}Bem vindo ao alistador militar da Alexa!{colorEnd}")
while True:
    nome=input("Digite seu nome: ")
    pessoas["Nomes"].append(nome)

    anoNascimento=int(input("Digite seu ano de nascimento: "))
    pessoas["Ano de nascimento"].append(anoNascimento)

    anoAtual=date.today().year

    idade=anoAtual-anoNascimento
    pessoas["Idade"].append(idade)


    if idade >= 18:
        c=str(input("Vc é maior de idade, vc já se alistou? [S/N]"))
        if c in "Ss":
            anoAlistamento=anoAtual-(idade-18)
            pessoas["Ano de alistamento"].append(anoAlistamento)
            print()
            print(f"Se passaram {idade-18} anos deste que vc se alistou.")
            print(f"Vc se alistou em {anoAlistamento}")
            
        elif c in "Nn":
            anoAlistamento=f"{color2}Deveria ter se alistado em {anoAtual-(idade-18)}{colorEnd}"
            pessoas["Ano de alistamento"].append(anoAlistamento)
            print(f"{anoAlistamento}.")
            
    elif idade < 18:
        print(f"Faltam {18-idade} anos para vc se alistar.")

    print()    
    c=str(input("Deseja continuar efetuando nova verificações: [S/N]")).lower()
    if c in "n":
        print()
        break

print(f"{color1}Segue lista de usuarios cadastrados:{colorEnd}")
print("=-"*10)
for i in range(len(pessoas["Nomes"])):
    print(f"{color1}Nome: {pessoas['Nomes'][i]}")
    print(f"Ano de nascimento: {pessoas['Ano de nascimento'][i]}")
    print(f"Idade: {pessoas['Idade'][i]}")
    if pessoas['Ano de alistamento']:
        print(f"Ano de alistamento: {pessoas['Ano de alistamento'][i]}{colorEnd}")
    print("=-"*10)
    print(f"{color1}Obrigado e tenha um bom dia!{colorEnd}")