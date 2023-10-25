"""Desafio 05: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor."""

from time import sleep

color1 = "\033[1;32m"
color2 = "\033[1;33m"
colorEnd = "\033[m"

maior = 0
menor = 0

for n in range ( 5 ) :
    numero = int ( input ( f"Digite o {n + 1}º numero: " ) )
    print ( f"{color2}O numero {numero} vem antes do numero {numero + 1} e depois do numero {numero - 1}.{colorEnd}" )
    sleep ( 1 )

    if n == 0 :  # Iremos verificar quais foram os maiores e menores numeros digitados pelo input
        maior = numero
        menor = numero
    else :
        if numero > maior :
            maior = numero
        if numero < menor :
            menor = numero

print ( f"{color1}O maior numero digitado foi o {maior}.{colorEnd}" )
print ( f"{color2}O menor numero digitado foi o {menor}.{colorEnd}" )
