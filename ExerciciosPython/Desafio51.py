"""Desafio 51: Desenvolva um programa que leia o primeiro termos e a razão de uma PA (Progressão Aritmetica). 
No final, mostre os 10 primeiros termos dessa progressão."""

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

#Criando uma função que irá efetuar o calculo da PA
def calcular_pa(num=0, razao=0, quant=0):
    """
    Iremos calcular e imprimir a progressão aritimetica seguindo os parametros abaixo:
    num (Numero inicial), razao (De quanto em quanto iremos pular), quant (Quantidade de numeros a serem impressos) 
    
    """        

    if quant <=0:
        print(cor("Insira no 3º parametro a quantidade de numeros a serem impressos!",31))
    else:
        print(f"\nSegue {quant} termos de uma Progressão Aritmetica:")
        for n in range(quant):
            pa = num + n * razao
            print(f"{pa} > ",end="")
        print(cor("FIM"))

#Limpando o terminal a cada execução do programa
limpar_terminal()

#Programa principal
while True:
    
    #Greetings!
    cabecalho(cor("Bem vindo ao calculador de PAs da Prof(a) Alexa!",35))
    
    #Solicitando um numero inicial
    while True:
        try:
            num = int(input("Digite um numero inicial: "))
            break
        except ValueError:
            print(cor("Erro! Digite somentes valores numericos!",31))
    
    #Solicitando um numero para a razão (de quanto em quanto iremos pular)    
    while True:
        try: 
            razao = int(input("Digite a razão: "))
            break
        except ValueError:
            print(cor("Erro! Digite somentes valores numericos!",31))
            
    #Chamando da função para o calculo da PA
    calcular_pa(num,razao,10)
    
    #Continuar ou não o programa
    c = str(input("\nDeseja efetuar uma nova verificação? [S/N]")).upper()
    
    if c in "Nn":
        print(cor("\nOBRIGADO E VOLTE SEMPRE",35))
        break
    else:
        limpar_terminal()