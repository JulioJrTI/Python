"""Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5!=5x4x3x2x1=120"""

# Usando de modulos para a formatação do programa
from Modulos.formatar import limpar_terminal,cabecalho,cor

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Função que irá calcular o fatorial de um numero (inserido como parametro)
def fatorial(num=0):
    """
    Função que irá calcular o fatorial de um numero (inserido como parametro)
    """

    # Variavel referente ao resultado da fatorial irá sempre por padrão receber o valor de 1
    fatorial = 1

    # Imprimindo o fatorial do numero inserido como parametro
    if num == 0:
        print(cor('Insira um valor numerico acima de 0 como parametro da função!',31))
    else:
        print()
        cabecalho(cor(f'Fatorial do numero {num}:',35))
        print(cor(f'{num}!= '),end='')
        for i in range(num,0,-1):
            fatorial*=i        
            if i == 1:    
                print(cor(f'{i}',34),end=' = ')
            else:
                print(cor(f'{i}',34),end=' x ')        
        print(cor(fatorial,33),'\n')        

# Greetings!
cabecalho(cor('Bem vindo ao calculador de fatoriais da Prof(a) Alexa!',35))

# Solicitando um numero e chamando a função contendo esse numero como parametro
while True:
    try:
        num = int(input('Digite um numero: '))
        fatorial(num)
        break
    except ValueError:
        print(cor('Insira um valor numerico valido!',31))