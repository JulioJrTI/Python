"""Desafio 18: Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo."""

import math

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
colorEnd="\033[m"

triangulo=[[],[],[],[]]

while True:
    angulo=int(input("Digite um valor para o angulo: "))
    triangulo[0].append(angulo)
    
    seno=math.sin(angulo)
    triangulo[1].append(seno)
    print(f"{color1}Seno: {triangulo[1][-1]}")    
    
    cosseno=math.cos(angulo)
    triangulo[2].append(cosseno)
    print(f"{color2}Cosseno: {triangulo[2][-1]}")
    
    tangente=math.tan(angulo)
    triangulo[3].append(tangente)
    print(f"{color3}Tangente: {triangulo[3][-1]}{colorEnd}")
    print("=-"*30)
    
    c=int(input("Deseja efetuar alguma alteração?\n1)Alterar angulo\n2)Sair do programa\n"))

    if c==1:
        triangulo[0].pop()
        triangulo[1].pop()
        triangulo[2].pop()
        triangulo[3].pop()
    elif c==2:
        print(f"{color1}Obrigado e volte sempre!{colorEnd}")
        break