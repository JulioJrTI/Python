"""Desafio 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso o CTPS for diferente de ZERO, o dicionario receberá tambem o ano de contratação e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date

color1="\033[1;32m"
color2="\033[1;31m"
colorReset="\033[m"

pessoas={"Nome":[],"Ano de nascimento":[],"Idade":[],"Carteira de trabalho":[],"Ano de contratação":[],"Salario":[],"Ano de Aposentadoria":[]}

idadeApoMulher=62

print(f"{color1}Bem vindo ao cadastrador de pessoas da Alexa corp!{colorReset}")
while True:
    #Cadastrando o nome da pessoa ao dicionario
    while True:
        nomePessoa=str(input("Digite seu nome: "))
        if nomePessoa.isalpha():
            pessoas["Nome"].append(nomePessoa)
            break
        else:
            print(f"{color2}Por favor digite seu nome! (ex: 'Alexa Bliss'){colorReset}")

    #Cadastrando o ano de nascimento da pessoa ao dicionario
    while True:
        try:
            anoNascimento=int(input("Digite seu ano de nascimento: "))
            pessoas["Ano de nascimento"].append(anoNascimento)
            break
        except:
            print(f"{color2}Erro! Digite somente numeros! (ex: '1994'){colorReset}")    

    #Descobrindo a idade da pessoa e adicionando a mesma ao dicionario
    anoAtual=date.today().year 
    idade=(anoAtual-anoNascimento)
    pessoas["Idade"].append(idade)

    #Cadastrando a CT ao dicionario
    carteiraTrabalho=int(input("Digite sua carteira de trabalho: (Ou digite 0 caso não tenha)"))    

    #Caso o trabalhador já tenha trabalhado
    if carteiraTrabalho!=0:
        #Adicionando carteira de trabalho ao dicionario
        pessoas["Carteira de trabalho"].append(carteiraTrabalho)

        #Adicionando o ano de contratação ao dicionario
        while True:
            try:
                anoContratacao=int(input("Digite o ano em que foi contratado: "))
                pessoas["Ano de contratação"].append(anoContratacao)
                break
            except:
                print(f"{color2}Erro! Digite o ano em que foi contratado! (ex: '2017'){colorReset}")

        #Adicionando o salario ao dicionario
        while True:
            try:
                salario=float(input("Digite seu salario: R$"))
                pessoas["Salario"].append(salario)
                break
            except:
                print(f"{color1}Erro! Digite seu salario! (ex: 'R$2000'){colorReset}")

        #Descobrindo quantos faltam para a pessoa se aposentar
        quantanoApo=(idadeApoMulher-idade)
        print(f"Faltam {quantanoApo} anos para vc se aposentar!")

        #Descobrindo o ano em que a pessoa irá se aposentar e o adicionando ao dicionario
        anoApo=anoAtual+quantanoApo
        print(f"Vc irá se aposentar em {anoApo}!")
        pessoas["Ano de Aposentadoria"].append(anoApo)

    #Caso o trabalhando nunca tenha trabalhado
    else:
        pessoas["Salario"].append("N/A")
        pessoas["Ano de contratação"].append("N/A")
        pessoas["Carteira de trabalho"].append("N/A")
        pessoas["Ano de Aposentadoria"].append("N/A")

    #Continuar cadastrando ou não
    while True:
        c=str(input("Deseja continuar cadastrando? [S/N]")).upper()[0]
        if c in ["S","N"]:
            break
        else:
            print(f"{color2}Digite somente S ou N!{colorReset}")

    if c in "Nn":
        print(f"{color1}Obrigado por cadastrar!{colorReset}")
        break
        
print()
#Resumo geral
print(f"{color1}Resumo geral:{colorReset}")
for i in range(len(pessoas["Nome"])):
    print(f"Nome: {pessoas['Nome'][i]}")
    print(f"Idade: {pessoas['Idade'][i]}")    
    
    if pessoas["Carteira de trabalho"][i]!="N/A" or pessoas["Ano de contratação"][i]!="N/A" or pessoas["Salario"][i]!="N/A" or pessoas["Ano de Aposentadoria"][i]!="N/A":
        print(f"Carteira de trabalho: {pessoas['Carteira de trabalho'][i]}")
        print(f"Ano de contratação: {pessoas['Ano de contratação'][i]}")
        print(f"Salario: R${pessoas['Salario'][i]}")
        print(f"Ano em que a pessoa irá se aposentar: {pessoas['Ano de Aposentadoria'][i]}")    
    else:
        print(f"{color2}Pessoa não possui CT{colorReset}")
    print("-="*10)
   