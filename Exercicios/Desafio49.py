"""Desafio 49: Refaça o DESAFIO 09, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço FOR."""

color1="\033[1;32m"
color2="\033[1;34m"
color3="\033[1;31m"
colorEnd="\033[m"

enfeite="-="*10

print(f"{color2}Bem vindo a tabuada da Alexa!")

while True:
    numero=int(input(f"{color2}Digite um numero qualquer para sabermos sua tabuada: {colorEnd}"))
    
    print(enfeite)
    print(f"{color2}Tabuada do {numero}:{colorEnd}")
    for n in range(1,11):
        tabuada=numero*n
        print(f"{color1}{numero}x{n}={tabuada}{colorEnd}")
    print(enfeite)    

    while True:
        c=str(input("Deseja continuar? [S/N]"))
        if c in "Nn":
            print(f"{color1}Obrigado e volte sempre!{colorEnd}")
            quit()
        if c in "Ss":
            break
        print(f"{color3}Input errado, tente novamente!{colorEnd}")
