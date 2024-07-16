"""Desafio 58: Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer."""

# Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Efeito cosmetico de loading
from time import sleep

# Usando da biblioteca random para o sorteio de numero aleatorio por parte da maquina
from random import randint

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Rounds no game
rounds_ate_vitoria = 0

# Maquina irá sortear um numero aleatorio de 0 a 10
maquina = randint(0,10)

# Greetings!
cabecalho(cor('Bem vindo(a) ao game de adivinhação da Prof(a) Alexa Luzia!',35))

#Programa principal
while True:
   
    # Jogador irá inserir um numero qualquer de 0 a 10    
    while True:
        try:
            print(cor(f'Round {rounds_ate_vitoria+1}: '))
            player=int(input('Digite um numero de 0 a 10: '))
            break
        except ValueError:
            print(cor('ERRO! Digite somente valores numericos!',31))
    
    # Adicionando +1 a cada round até a vitoria do jogador
    rounds_ate_vitoria+=1

    # Logica para a vitoria ou derrota
    if player == maquina:
        print(cor('\nPlayer ganhou!',34))
        print(cor(f'\nForam necessarios {rounds_ate_vitoria} palpites até a vitoria.',35))
        break
    else:
        print(cor('\nMaquina ganhou!\n',31))