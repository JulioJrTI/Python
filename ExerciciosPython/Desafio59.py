"""Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

# Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Efeito de pausa
from time import sleep

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Controle de inserção de numeros
inserirNumeros = True

# Greetings!
cabecalho(cor('Bem vindo ao calcular de numeros da Prof(a) Alexa Luzia!',35))

# Programa principal
while True:
    
    # Controle de inserção de numeros
    while inserirNumeros:    
        
        # Adicionando os dois a um lista
        numeros = []       
        
        # Solicitando dois numeros ao usuario
        for n in range(2):
            while True:
                try:
                    num = int(input(f'Digite o {n+1}º numero: '))
                    numeros.append(num)
                    inserirNumeros = False
                    break
                except ValueError:
                    print(cor('Erro! Digite somente valores numericos!',31))
        
    # Menu de escolhas
    print(cor('\nQual processo efetuar com estes numeros?',34))
    while True:
        try:
            menu=int(input(('[1] Soma\n'
                            '[2] Multiplicar\n'
                            '[3] Maior\n'
                            '[4] Novos numeros\n'
                            '[5] Sair\n'
                            'Escolha: ')))
            if menu > 5:
                print(cor('Erro! Escolha invalida, tente novamente!',31))
            else:
                break
        except ValueError:
            print(cor('Erro! Digite somente valores numericos!',31))
            
    # Variaveis referentes aos numeros inseridos na lista
    n1, n2 = numeros[0], numeros[1]
    
    # Soma
    if menu == 1:        
        soma = n1 + n2
        cabecalho(cor(f'A soma dos numeros {n1} e {n2} é igual a {soma}'))        
    
    # Multiplicar
    elif menu == 2:
        multiplicar = n1 * n2
        cabecalho(cor(f'O resultado da multiplicação dos numeros {n1} e {n2} é igual {multiplicar}'))        
    
    # Maior
    elif menu == 3:
        maiorNumero = max(n1,n2)
        cabecalho(cor(f'O maior numero digitado é o numero {maiorNumero}'))        
        
    # Novos numeros
    elif menu == 4:
        inserirNumeros = True
        print('\nDigite novos numeros:')
    
    # Sair do programa
    elif menu == 5:
        print(cor('OBRIGADO E VOLTE SEMPRE!',35))
        break
    
    # Efeito de pausa entre os resultados
    sleep(2)