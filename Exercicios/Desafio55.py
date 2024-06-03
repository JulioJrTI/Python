"""Desafio 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

c1="\033[1;32m"
c2="\033[1;33m"
c0="\033[m"

pessoas={"Nome":[],"Peso":[]} #Iremos armazenar os nomes e pesos das pessoas

maiorPeso=0 #Variavel para o maior peso
maiorPesoNome=[] #Iremos armazenar o nome da pessoa com o maior peso nesta lista

menorPeso=0 #Variavel para o menor peso
menorPesoNome=[] #Iremos armazenar o nome da pessoa com o menor peso nesta lista

print(f"{c1}Bem vindo ao medidor de peso da Alexa!{c0}")
for p in range(5):    
    nome=str(input("Digite seu nome: "))
    pessoas["Nome"].append(nome) #Armazenando o nome da pessoa ao dicionario

    peso=float(input(f"Olá {c1}{nome}{c0}, digite seu peso: Kg"))
    pessoas["Peso"].append(peso) #Armezenando o peso da pessoa ao dicionario

    print("-="*10)

    if p==0:
        maiorPeso=peso
        menorPeso=peso
        maiorPesoNome=nome
        menorPesoNome=nome
    else:
        if peso > maiorPeso:
            maiorPeso=peso
            maiorPesoNome=nome
        if peso < menorPeso:
            menorPeso=peso
            menorPesoNome=nome

print("Lista de pessoas cadastradas:")
for i in range(len(pessoas["Nome"])):
    print(f"{c1}{pessoas['Nome'][i]}{c0} pesa {c2}{pessoas['Peso'][i]}Kg{c0}")
print(f"Maior Peso: {c1}{maiorPesoNome}{c0} pesa {c2}{maiorPeso}{c0}")
print(f"Menor peso: {c1}{menorPesoNome}{c0} pesa {c2}{menorPeso}{c0}")
print("<<<< Fim >>>>")

