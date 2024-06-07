"""Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²."""

from Modulos.Formatar import cor,cabecalho
import math

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Função que irá calcular uma area de acordo com a largura e altura
def CalcularArea(l,a):
    calcArea = (l*a)
    return calcArea

#Greetings!
cabecalho(cor("Bem vindo ao medidor de tinta da Prof(a) Alexa!",35))

#Tratamento de erros
while True:
    try:
        #Solicitando a largura ao usuario
        largura=float(input("Digite a largura da parede em metros: "))
        break
    except ValueError:
        print(cor("Erro! Digite um valor numerico valido para a largura! (Exemplo 6.9)",31))
    except KeyboardInterrupt:
        print(cor("\nUsuario encerrou o programa...",31))
        quit()

#Tratamento de erros
while True:
    try:
        #Solicitando a altura do usuario
        altura=float(input("Digite a altura da parede em metros: "))
        break
    except ValueError:
        print(cor("Erro! Digite um valor numerico valido para a altura! (Exemplo 6.9)",31))
    except KeyboardInterrupt:
        print(cor("Usuario encerrou o programa...",31))
        quit()

#Calculando a area, multiplicado a largura pela altura
area=CalcularArea(largura,altura)
quantTinta=(area/2)

print()

#Imprimindo resultado
cabecalho(cor(f"Será necessaria {math.ceil(quantTinta)}(l) de tinta para pintar uma area de {area}(m), com paredes medindo {largura}(m) de largura e {altura}(m) de altura!",35),cent=0,quantC=130)