"""Desafio 49: Refaça o DESAFIO 09, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço FOR."""

#Usando de modulos para a formatação do programa
from Modulos.formatar import limpar_terminal,cabecalho,cor

#Limpando o terminal a cada execução do programa
limpar_terminal()

#Efeito cosmetico de delay
from time import sleep

#Greetings!
cabecalho(cor("Bem vindo ao estudo de tabuada da Prof(a) Alexa!",35))

#Programa principal
while True:

    #Solicitando um valor numerico para a tabuada
    while True:
        try:
            num = int(input("\nDigite um valor numerico para o calculo da tabuada: "))
            break
        except ValueError:
            print(cor("\nErro! Digite valores numericos validos!\n",31))

    #Usando loop FOR para o calculo da tabuada
    print(cor(f"\nTabuada do {num}:"))
    for n in range(1,11):
        #Calculando resultado multiplicando o valor indicado pelo usuario multiplicado pelo valor do loop FOR
        res = num*n
        
        #Imprimindo tabuada
        print(cor(f"{num} x {n} = {res}",33))
        
    #Continuar ou não o programa
    sleep(3)
    c = str(input("\nDeseja continuar? [S/N]")).upper()    
    if c in "Nn":
        print(cor("\nOBRIGADO E VOLTE SEMPRE!\n",35))
        break