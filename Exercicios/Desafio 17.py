"""Desafio 17: Faça um programa que leia o comprimento do cateto oposto 
e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa."""

import math

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
colorEnd="\033[m"

trianguloRetangulo=[[],[],[]]

c2=False

while True:
    co=float(input(f"{color1}Digite o cateto oposto: {colorEnd}"))
    trianguloRetangulo[0].append(co)
    
    ca=float(input(f"{color2}Digite o cateto adjacente: {colorEnd}"))
    trianguloRetangulo[1].append(ca)
    
    h=math.hypot(co,ca)
    trianguloRetangulo[2].append(h)

    print("=-"*30)
    print(f"{color1}Cateto oposto: {trianguloRetangulo[0]}")
    print(f"{color2}Cateto adjacente: {trianguloRetangulo[1]}")
    print(f"{color3}Hipotenusa: {trianguloRetangulo[2]}{colorEnd}")
    c2=True

    print("=-"*30)
    while c2:
        print("=-"*30)
        c=int(input("Deseja efetuar alguma alteração? \n1-Alterar o cateto oposto\n2-Alterar o cateto adjacente\n3-Resetar o programa\n4-Sair do programa\n"))
        c2=False
        print("=-"*30)

        if c==1:
            trianguloRetangulo[0].clear()
            co=float(input(f"{color1}Digite o cateto oposto: {colorEnd}"))
            trianguloRetangulo[0].append(co)
            h=math.hypot(co,trianguloRetangulo[1][-1])
            trianguloRetangulo[2][-1]=h
            print(f"{color3}Hipotenusa: {trianguloRetangulo[2]}{colorEnd}")
            c2=True
            
        elif c==2:
            trianguloRetangulo[1].clear()
            ca=float(input(f"{color2}Digite o cateto adjacente: {colorEnd}"))
            trianguloRetangulo[1].append(ca)
            h=math.hypot(ca,trianguloRetangulo[2][-1])
            trianguloRetangulo[2][-1]=h
            print(f"{color3}Hipotenusa: {trianguloRetangulo[2]}{colorEnd}")
            c2=True
            
        elif c==3:
            trianguloRetangulo[0].clear()
            trianguloRetangulo[1].clear()
            trianguloRetangulo[2].clear()
        elif c==4:
            print(f"{color1}Obrigado e tenha um bom dia!")
            exit()