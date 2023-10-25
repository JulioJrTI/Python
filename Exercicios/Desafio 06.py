"""Desafio 06: Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada."""

from math import sqrt

color1 = "\033[1;32m"
color2 = "\033[1;33m"
color3 = "\033[1;34m"
colorEnd = "\033[m"

numeros = []

while True :
    numeros.append ( int ( input ( f"Digite o {len ( numeros ) + 1}º numero: " ) ) )
    c = input ( "Deseja continuar? [S/N]" )

    if c in "Nn" :
        break

for i, v in enumerate ( numeros ) :
    print ( "-=" * 50 )
    print ( f"{color1}O dobro do numero {v} é igual a {v * 2}." )
    print ( f"{color2}O triplo do numero {v} é igual a {v * 3}." )
    print ( f"{color3}A raiz quadrada do numero {v} é igual a {sqrt ( v ):.2f}."
            f"{colorEnd}" )
