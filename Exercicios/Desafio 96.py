"""Desafio 96: Faça um programa que tenha uma função chamada "area()", que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

#Definindo uma função que irá calcular a area do terreno
def area(l,c): #A função irá receber a largura e comprimento
    area=l*c #Iremos calcular a area multiplicando os valores anteriores
    print(f"Area: {area}") #Imprimindo o resultado final

#Modo manual e imprimindo o resultados
area(6,9)

#Pedindo ao input os valores necessarios e imprimindo os resultados
largura=float(input("Digite a largura: "))
comprimento=float(input("Digite o comprimento: "))
area(largura,comprimento)