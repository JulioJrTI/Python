"""Desafio 54: Crie um programa que leia o ano de nascimento de sete pessoas, No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

# Usando biblioteca datetime para o calculo da idade
from datetime import date

# Usando modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Quantidade de pessoas com idade superior e inferior a dezoito irão ser cadastradas em variaveis
adulto = 0
nao_adulto = 0

# Greetings!
cabecalho(cor('Bem vindo ao calculador de idade da Prof(a) Alexa!',35))

# Solicitando e calculando a idade de sete pessoas
for i in range(7):
    
    # Solicitando o ano de nascimento do usuario
    while True:
        try:
            anoNascimento = int(input(f'Pessoa Nº{i+1}: Digite seu ano de nascimento: '))
            break
        except ValueError:
            print(cor('\nERRO! Digite somente valores numericos para a idade (Exemplo: 1994)\n',31))

    # Calculando a idade
    idade = (date.today().year) - anoNascimento
    
    print(cor(f'Vc tem {idade} anos de idade.\n',33))
    
    if idade >= 18:        
        adulto+=1
    else:        
        nao_adulto+=1        

# Resumo da idade das pessoas cadastradas
if adulto > 0:
    print(f'Foram identificados {adulto} pessoas com idade maior ou igual a dezoito',end="")
    if nao_adulto > 0:
        print(f' e {nao_adulto} pessoas com idade inferior a dezoito.')
    else:
        print('\nNão foram identificados pessoas com idade inferior a dezoito')
else:
    print('Não foram identificandos pessoas com idade superior ou igual a dezoito')