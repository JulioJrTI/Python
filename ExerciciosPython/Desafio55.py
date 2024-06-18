"""Desafio 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

# Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Greetings!
cabecalho(cor('Bem vindo ao medidor de peso da Prof(a) Alexa!',35))

# Maior e Menor peso serão armazenadas em variaveis
maiorPeso=0
menorPeso=0

# Solicitando o peso de cinco pessoas
for i in range(5):
    
    while True:    
        try:
            peso = float(input(f'\nPessoa Nº{i+1}: Digite o peso: '))
            break
        except ValueError:
            print(cor('\nErro! Digite somente valores numericos para o peso! (Exemplo: 6.9)\n',31))
    
    # Calculando maior e menor peso
    if i==0:
        maiorPeso=peso
        menorPeso=peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

# Resumo de peso            
print(cor('\nResumo: ',33))
print(f'O maior peso inserido foi de {maiorPeso}Kg')
print(f'O menor peso inserido foi de {menorPeso}Kg')