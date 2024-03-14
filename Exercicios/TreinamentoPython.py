color1="\033[1;32m"
color2="\033[1;33m"
color3="\033[1;34m"
color4="\033[1;35m"
colorEnd="\033[m"
enfeite="=-"*10

numeros=[]
chave=True

print(f"{color1}Bem vindo ao enumerador de numeros da Alexa!{colorEnd}")
while True:
    if chave:
        numero=int(input("Digite um numero de 0 a 9999: "))
        chave=False
    numeros.append([numero//1%10])
    numeros.append([numero//10%10])
    numeros.append([numero//100%10])
    numeros.append([numero//1000%10])

    print(f"{color1}Unidade: {numeros[0]}{colorEnd}")
    print(f"{color2}Dezena: {numeros[1]}{colorEnd}")
    print(f"{color3}Centena: {numeros[2]}{colorEnd}")
    print(f"{color4}Milhar: {numeros[3]}{colorEnd}")

    print(enfeite)

    c=str(input("Deseja efetuar nova verificação? [S/N]"))

    if c in "Ss":
        chave=True
        numeros.clear()
    elif c in "Nn":
        print(f"{color1}Obrigado e tenha um bom dia!{colorEnd}")
        break