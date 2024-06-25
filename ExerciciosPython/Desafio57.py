"""Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto."""

# Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Efeito de pausa
from time import sleep

# Carregando banco de dados
import json
try:
    with open ('dados_ex57.json', 'r') as arquivo:
        pessoas = json.load(arquivo)
except FileNotFoundError:
    print('ERRO! Arquivo não encontrado! Criando um novo.')
    # Dicionario contendo as pessoas cadastradas
    pessoas={'Nome':[],'Sexo':[]} 

# Greetings!
cabecalho(cor('Bem vindo ao analizador de sexo da Prof(a) Alexa!',35))

# Programa principal
while True:
    
    # Menu de escolhas
    while True:    
        menu = int(input('(1) Cadastrar novos usuarios\n'
                        '(2) Exibir usuarios cadastrados\n'
                        '(3) Sair do programa\n'
                        'Insira: '))
        if menu > 3:
            print(cor('Erro! Escolha somente um valor numerico de 1 a 3!\nSaindo do programa...',31))
            quit()
        else:
            break
    
    # Cadastrando novos usuarios
    if menu == 1:    
        print()
        # Solicitando o nome de uma pessoa
        while True:
            nomePessoa = str(input('Digite seu nome: '))
            
            if nomePessoa.isalpha():
                pessoas['Nome'].append(nomePessoa)
                break            
            else:
                print(cor('\nErro! Digite somentes palavras!\n',31))            

        # Solicitando o sexo de uma pessoa
        while True:    
            sexo = str(input('Digite seu sexo (M,F): ')).upper()[0]
            
            if sexo in ["M","F"]:
                pessoas['Sexo'].append(sexo)
                break
            else:
                print(cor('\nErro! Digite somente M (Sexo Masculino) ou F (Sexo Feminino)\n',31))
                
        # Salvando pessoas cadastradas no banco de dados
        with open('dados_ex57.json', 'w') as arquivo:
            json.dump(pessoas,arquivo)
        
        # Mensagem de sucesso no cadastro
        print(cor(f'Usuario(a) {nomePessoa} do sexo {sexo}, cadastrado(a)!',33))    
        
        # Continuar ou não a cadastrar pessoas
        c = str(input('Deseja continuar cadastrando? [S/N]')).upper()[0]
        
        # Saindo ou não do programa
        if c == "N":
            print(cor('OBRIGADO E VOLTE SEMPRE!',35))
            break
        else:
            print()
    
    # Lista completa de pessoas cadastradas 
    elif menu == 2:        
        cabecalho(cor('Segue lista de pessoas cadastradas:',34))
        for n, s in zip(pessoas['Nome'],pessoas['Sexo']):
            print(f'Nome: {n}')
            print(f'Sexo: {s}')
            print('_'*20)
        print()
        sleep(3)
            
    # Sair do programa
    elif menu == 3:
        print(cor('OBRIGADO E VOLTE SEMPRE!',35))
        break
        