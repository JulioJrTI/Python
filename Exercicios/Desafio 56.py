"""Desafio 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A media de idade do grupo.

- Qual é o nome do homem mais velho.

- Quantas mulheres tem menos de 20 anos."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

pessoas={'Nome':[],'Idade':[],'Sexo':[]} #Iremos armazenar as informações em um dicionario.

homemMaisVelhoNome=[] #Iremos armazenar o nome do homem mais velho em uma lista.
homemMaisVelho=0 #Iremos armazenar a idade do homem mais velho em uma variavel.

mulheresMenosVinteNome=[] #Iremos armazenar os nomes das mulheres com idade inferior a 20 anos em uma lista.
mulheresMenosVinte=0 #Iremos armazenar a quantidade de mulheres com idade inferior a 20 anos em uma variavel.

print(f"{c1}Bem vindo ao cadastrador de pessoas da Alexa!{c0}")
for p in range(4):
    while True: #Mecanica de erro            
        nome=str(input('Digite seu nome: '))
        pessoas['Nome'].append(nome) #Armazenando o nome do usuario em um dicionario.
        if nome.isalpha(): #Se o valor digitado no input for PALAVRAS ou LETRAS.
             break #O programa irá continuar.
        else: #Caso contrario, iremos exibir uma mensagem de erro.        
            print(f"{c2}Erro! Digite somente seu nome.{c0}")
    
    while True: #Mecanica de erro
        try: #Se o valor em input for diferente de numeros, iremos exibir uma mensangem de erro.
            idade=int(input(f'Olá {c1}{nome}{c0}, digite sua idade: '))
            pessoas['Idade'].append(idade) #Armazenando a idade do usuario em um dicionario.
            break
        except:
            print(f"{c2}Erro! Digite sua idade em numeros.{c0}")
    
    while True: #Mecanica de erro        
        sexo=str(input('Digite seu sexo: [M/F]')).upper()[0]
        pessoas['Sexo'].append(sexo) #Armazenando o sexo do usuario em um dicionario.
        if sexo in ["M","F"]: #Se o valor input for M ou F.
            break #O programa irá continuar.
        else: #Caso contrario iremos exibir uma mensagem de erro.      
            print(f"{c2}Erro! Digite somente M ou F.{c0}")
    
    print("-="*10)

    if sexo=="M": #Se o usuario for um homem
        if p==0: 
            homemMaisVelho=idade
            homemMaisVelhoNome=nome
        else:
            if idade>homemMaisVelho:
                homemMaisVelho=idade
                homemMaisVelhoNome=nome

    if sexo=="F": #Se o usuario for uma mulher
        if idade<=20:
            mulheresMenosVinte+=1 #Iremmos armazenar a quantidade de mulheres com idade inferior ou igual a 20
            mulheresMenosVinteNome.append(nome) #E tambem seus nomes

#Iremos saber a media de idade das pessoas cadastradas
totalPessoas=len(pessoas['Idade']) #Iremos pegar a quantidade de valores inseridos no dicionario
somaIdades=sum(pessoas['Idade']) #Iremos somar esses valores
media=somaIdades/totalPessoas #E iremos dividir essas variaveis

print(f'A media de idade do grupo é de {media} anos.')
print("-="*10)

if homemMaisVelho!=0: #Se existir um homem no dicionario, iremos exibir as seguintes informações
    print(f'A idade do homem mais velho é de {homemMaisVelho} anos e seu nome é {homemMaisVelhoNome}.')
else:
    print("Não temos homens cadastrados na lista")

print("-="*10)

if mulheresMenosVinte!=0: #Se existir mulheres no dicionario e se suas idades forem igual ou abaixo de 20
    print(f'Temos {mulheresMenosVinte} mulheres com idade inferior ou igual a 20: ',end="")
    for i, p in enumerate(mulheresMenosVinteNome):
        if i==len(mulheresMenosVinteNome)-1:
            print(p,end=". ")
        elif i==len(mulheresMenosVinteNome)-2:
            print(p,end=" e ")
        else:
            print(p,end=", ")
    print()
else:
    print("Não temos mulheres cadastradas na lista, ou todas são maiores de 18 anos.")

print("-="*10)

print(f'{c1}Lista de pessoas cadastradas:{c0}')
for i in range(len(pessoas['Sexo'])):
    print(f"Nome: {pessoas['Nome'][i]}")
    print(f"Idade: {pessoas['Idade'][i]}")
    print(f"Sexo: {pessoas['Sexo'][i]}")
    print('=-'*10)
print("<<<< FIM >>>>")