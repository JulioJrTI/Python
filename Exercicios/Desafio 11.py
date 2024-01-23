"""Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²."""

print("Bem vindo ao medidor de tinta da Prof(a) Alexa!")

#Solicitando a largura ao usuario
largura=float(input("Digite a largura da parede em metros: "))

#Solicitando a altura do usuario
altura=float(input("Digite a altura da parede em metros: "))

#Calculando a area, multiplicado a largura pela altura
area=(largura*altura)
quantTinta=(area/2)

#Imprimindo resultado
print(f"Será necessaria {quantTinta}(l) de tinta para pintar uma area de {area}(m), com paredes medindo {largura}(m) de largura e {altura}(m) de altura!")

print(f"Com paredes medindo {largura}(m) de largura e {altura}(m) de altura, será necessario {quantTinta}(l)")