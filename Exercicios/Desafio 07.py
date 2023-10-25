"""Desafio 07: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""

color1 = "\033[1;32m"
color2 = "\033[1;33m"
colorEnd = "\033[m"

notas = []

for n in range ( 2 ) :
    notas.append ( int ( input ( f"{color1}Digite a {n + 1}º nota: {colorEnd}" ) ) )
media = (notas[0] + notas[1]) / 2
print ( f"{color2}Media de notas: {media}{colorEnd}" )
