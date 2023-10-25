"""Desafio 47: Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50."""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
colorEnd="\033[m"
enfeite="-="*10

numeros={"Numeros pares":[],"Numeros impares":[]}

for n in range(1,51):
    if n%2==0:
        numeros["Numeros pares"].append(n)
    else:
        numeros["Numeros impares"].append(n)

print()
print(f"{color3}Numeros pares e impares de 1 a 50: {colorEnd}")       

print(enfeite)
print(f"{color1}Numeros pares: {numeros['Numeros pares']}{colorEnd}")

print(enfeite)
print(f"{color2}Numeros impares: {numeros['Numeros impares']}{colorEnd}")