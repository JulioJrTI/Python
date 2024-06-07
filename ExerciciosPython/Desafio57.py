"""Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto."""

c1="\033[1;34m"
c2="\033[1;35m"
c3="\033[1;31m"
c0="\033[m"

pessoas={'Nome':[],'Sexo':[]}

print(f"{c2}Bem vindo ao cadastrador de pessoas da Alexa!{c0}")
while True:    
    while True:
        nome=str(input("Digite seu nome: "))
        if nome.isalpha():
            pessoas["Nome"].append(nome)
            break
        else:
            print(f"{c3}Erro! Digite somente palavras.{c0}")   
    
    while True:        
        sexo=str(input(f"Olá {nome}, digite seu sexo: [M/F]")).upper()[0]
        if sexo in ["M","F"]:
            pessoas["Sexo"].append(sexo)
            break
        else:
            print(f"{c3}Erro! Escolha M ou F!{c0}")
    if sexo in "Mm":
        print(f"Seu sexo é {c1}Masculino!{c0}")
    else:
        print(f"Seu sexo é {c2}Feminino!{c0}")

    while True:        
        c=str(input("Deseja continuar? [S/N]")).upper()[0]
        if c in ["S","N"]:
            break
        else:        
            print(f"{c3}Erro! Digite somente S ou N.{c0}")

    if c in "Nn":        
        break

print()
print("Lista de pessoas cadastradas:")
for i, lista in enumerate(pessoas["Nome"]):    
    print(i+1,end="- ")
    print(f"Nome: {pessoas['Nome'][i]} - ",end="")
    print(f"Sexo: {pessoas['Sexo'][i]}")    
print("<<<< FIM >>>>")