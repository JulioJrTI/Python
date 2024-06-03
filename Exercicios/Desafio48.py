"""Desafio 48: Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 até 500."""

color1="\033[1;32m"
color2="\033[1;33m"
colorEnd="\033[m"

soma=0
numeros={"Numeros impares e multiplos de tres":[]}

for n in range(1,500):
    if n%2==1 and n%3==0:
        numeros["Numeros impares e multiplos de tres"].append(n)
        soma+=n
print(f"{color1}Numeros impares e multiplos de 3: {colorEnd}{numeros['Numeros impares e multiplos de tres']}")
print(f"{color2}Soma total: {soma}{colorEnd}")
        