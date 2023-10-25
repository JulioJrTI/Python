"""Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessaria para pinta-la,
sabendo que cada litro de tinta, pinta uma area de 2m²."""

color = "\033[1;32m"
colorEnd = "\033[m"

while True :
    largura = (float ( input ( "Digite a largura de sua parede: " ) ))
    altura = (float ( input ( "Digite a altura de sua parede: " ) ))

    area = (largura * altura)
    tinta = (area / 2)

    print ( "=-" * 30 )
    print (
        f"{color}Sua parede tem {largura}m de largura, {altura}m de altura e uma area de {area}m², será necessario {tinta}l de tinta para fazer a pintura.{colorEnd}" )
    c = input ( "Deseja fazer novo calculo? [S/N]" )
    if c in "Ss" :
        continue
    else :
        print ( f"{color}Obrigado e tenha um bom dia!{colorEnd}" )
        break
