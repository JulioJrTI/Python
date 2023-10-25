"""Desafio 08: Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros."""

color1 = "\033[1;32m"
color2 = "\033[1;33m"
colorEnd = "\033[m"

centrimetro = 100
milimetro = 1000

while True :
    metro = int ( input ( "Digite um valor em metros: " ) )
    print ( f"{color1}{metro} metros: {centrimetro * metro}cm.\n"
            f"{color2}{metro} metros: {milimetro * metro}mm."
            f"{colorEnd}" )
    break
