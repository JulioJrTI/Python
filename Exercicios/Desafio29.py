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

#Criando uma função que irá multar (valor inserido como parametro) o usuario caso o mesmo tenha ultrapassado o limite indicado como parametro
def multador_carro(kmPercorrido=0,limite=0,multa=0):
    """
    Parametros:
    kmPercorrido = A quantidade de KMs percorridos pelo usuario
    limite = Caso o usuario ultrapasse o limite inserido, o mesmo será multado
    multa = Valor monetario para a multa (Será cobrado por cada KMs acima do limite)
    
    """
    
    if kmPercorrido > limite:
        print(cor("Vc foi multado!",31))            
        aPagar = float((kmPercorrido-80)*multa)
        print(cor(f"KMs percorridos acima do limite: {kmPercorrido-80}KMs\nValor a pagar: R${aPagar:.2f}",31))
    else:
        print(cor(f"Tudo certo!\nKMs percorridos: {kmPercorrido}KMs"))
    
#Tratamento de erro
while True:    
    try:
        velocidadeCarro = int(input("Digite a velocidade percorrida pelo carro: "))
        break
    except ValueError:
        print(cor("Erro! Digite somente valores numericos!",31))

#Chamando da função criada
multador_carro(velocidadeCarro,80,7)