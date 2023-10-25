"""Desafio 42: Refaça o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:

-Equlaterio: Todos os lados iguais

-Isosceles: Dois lados iguais

-Escaleno: Todos os lados diferentes"""

color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
color4="\033[1;31m"
colorEnd="\033[m"
enfeite="=-"*10

print(f"{color1}Bem vindo ao calculador de triangulos 2.0 da Alexa!{colorEnd}")
while True:
    numeros=[]
    for n in range(3):
        n=float(input(f"Digite o {n+1} numero: "))
        numeros.append(n)    
    
    triangulo={"Numeros":numeros}

    if triangulo["Numeros"][0] < triangulo["Numeros"][1] + triangulo["Numeros"][2] and \
            triangulo["Numeros"][1] < triangulo["Numeros"][0] + triangulo["Numeros"][2] and \
            triangulo["Numeros"][2] < triangulo["Numeros"][0] + triangulo["Numeros"][1]:
        print(enfeite)
        print("Pode formar um triangulo!")
        if triangulo["Numeros"][0]==triangulo["Numeros"][1]==triangulo["Numeros"][2]:
            print(f"{color1}Equlaterio, todos os lados são iguais.{colorEnd}")    
        elif triangulo["Numeros"][0]!=triangulo["Numeros"][1]!=triangulo["Numeros"][2]:
            print(f"{color3}Escaleno, todos os lados são diferentes.{colorEnd}")
        else:
            print(f"{color2}Isosceles, dois lados são iguais.{colorEnd}")
        print(enfeite)
    else:
        print(f"{color4}Não pode formar um triangulo!{colorEnd}")

    c=str(input("Deseje efetuar nova verificação? [S/N]"))

    if c in "Ss":
        triangulo["Numeros"].clear()    
    if c in "Nn":
        print(f"{color1}Obrigado e volte sempre!{colorEnd}")
        break