"""Desafio 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A media de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos."""

# Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Iremos calcular a idade da pessoa com o ano de nascimento da mesma
from datetime import date

# Cadastrando as pessoas em um dicionario
cadastroPessoas = {"Nome":[],"Sexo":[],"Idade":[]}

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Greetings!
cabecalho(cor('Bem vindo ao cadastrador de pessoas da Prof(a) Alexa!',35))

# Solicitando os dados de quatro pessoas
for i in range(4):
    print(cor(f"{i+1}º pessoa:",33))
    
    # Cadastrando o nome da pessoa no dicionario
    pessoaNome = str(input("Digite seu nome: "))
    cadastroPessoas["Nome"].append(pessoaNome)
    
    # Cadastrando a idade da pessoa no dicionario
    anoNascimento = int(input("Digite seu ano de nascimento: "))
    idade = (date.today().year) - anoNascimento
    cadastroPessoas["Idade"].append(idade)
        
    #Cadastrando o sexo da pessoa no dicionario
    sexo = str(input("Digite seu sexo (M-F): ")).upper()
    cadastroPessoas["Sexo"].append(sexo)

print() 

# Resumo geral  
cabecalho("Resumo:")

# Media de idade
idades = cadastroPessoas["Idade"]
soma_idades = sum(idades)
quant_pessoas = len(idades)
media = (soma_idades / quant_pessoas)
print(cor(f"\nA media de idade do grupo é de {media} anos.",33))

# Homem mais velho
homem_mais_velho_nome = ""
homem_mais_velho_idade = 0
for i in range(quant_pessoas):
    if cadastroPessoas["Sexo"][i].upper() == 'M' and cadastroPessoas["Idade"][i] > homem_mais_velho_idade:
        homem_mais_velho_idade =cadastroPessoas["Idade"][i]
        homem_mais_velho_nome=cadastroPessoas["Nome"][i]
if homem_mais_velho_nome:
    print(cor(f"\nO homem mais velho é {homem_mais_velho_nome} com {homem_mais_velho_idade} anos.",34))
else:
    print("\nNenhum homem cadastrado.")
    
# Mulheres com menos de 20 anos de idade
mulheres_menos_20 = []
for i in range(quant_pessoas):
    if cadastroPessoas["Sexo"][i].upper() == 'F' and cadastroPessoas["Idade"][i] < 20:
        mulheres_menos_20.append((cadastroPessoas["Nome"][i],cadastroPessoas["Idade"][i]))
if mulheres_menos_20:
    print(cor("\nMulheres com menos de 20 anos:",35))
    for nome, idade in mulheres_menos_20:
        print(f"{nome} com {idade} anos.")
else:
    print("\nNenhuma mulher com menos de 20 anos foi cadastrada.")