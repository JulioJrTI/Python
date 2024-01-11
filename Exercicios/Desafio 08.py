"""Desafio 08: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

from Modulos.Matematica import conversaoMetros
from Modulos.Formatar import cor,cabecalho

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Programa principal
cabecalho(cor("Bem vindo ao conversor de Metros para Cm e Mm da Prof(a) Alexa!",35))
while True:
        
        #Tratamento de erros
        while True:
                try:
                        #Solicitando um valor float (ou int) ao usuario
                        valorM=input("Digite um valor em metros: (m)")
                        
                        #Se o usuario inserir uma virgula em vez de ponto como separador, iremos substituir esta virgula
                        if "," in valorM:                                                               
                                valorM = valorM.replace(",",".")                                
                        valorM = float(valorM)
                        break
                
                #Valor Invalido
                except(ValueError):
                        print(cor("Erro! Digite somente numeros!",31))
                
                #Usuario forçou reset do programa
                except (KeyboardInterrupt):
                        print(cor("Usuario cancelou o programa.",31))
                        quit()
                        
        #Chamando a função que irá converter o valor inserido em input acima e imprimindo resultado
        conversaoMetros(valorM)
        
        #Tratamento de erro
        while True:        
                #Escolha de continuar ou não o programa
                c=str(input("Deseja continuar? [S/N]")).upper()
                
                #Caso o usuario tenha escolhido S ou N, iremos sair do loop de tratamento de erro
                if c in ["S","N"]:
                        break
                
                #Caso tenha inserido valor invalido, iremos exibir um erro
                else:
                        print(cor("Por favor digite somente S ou N como escolha!",31))
        
        #Sair do programa
        if c in "Nn":
                print(cor("Obrigado e volte sempre!"))
                break