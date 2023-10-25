"""Desafio 96: Faça um programa que tenha uma função chamada "area()", que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

def Area(l,c): #A função "Area" irá receber duas variaveis: l (largura) e c (comprimento)
    a=l*c #Definindo que a variavel "a" irá a multiplicação de l e c
    print(f"A area do terreno é de {l}x{c} é de {a} metros quadrados.") #Definindo texto formatado da função

def Linhas():
    print("-="*10)


print("Controle de Terrenos")
Linhas()

largura=float(input("Digite a largura: "))
comprimento=float(input("Digite o comprimento: "))

Area(largura,comprimento) #Na função, as variaveis l e c irão receber a variaveis de input "largura" e "comprimento"

