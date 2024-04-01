"""Desafio 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Greetings
cabecalho(cor("Bem vindo(a) ao speed-o-meter da Alexa Luzia!",35))

#Tratamento de erro
while True:    
    try:
        velCarro = int(input("Digite a velocidade percorrida pelo carro: "))
        break
    except ValueError:
        print(cor("Erro! Digite somente valores numericos!",31))

if velCarro > 80:
    print(cor("Vc foi multado!",31))
    multa = 7    
    aPagar = float((velCarro-80)*multa)
    print(cor(f"KMs percorridos acima do limite: {velCarro-80}KMs\nValor a pagar: R${aPagar:.2f}",31))
else:
    print(cor(f"Tudo certo!\nKMs percorridos: {velCarro}KMs"))




