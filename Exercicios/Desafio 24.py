"""Desafio 24: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santa"."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

lista=[]
print("=-"*10,f"{color1}Bem vindo a localizador de nomes da Alexa!{colorEnd}","=-"*10)
while True:
    cidade=str(input("Digite o nome de sua cidade: (Ou digite 0 para sair)")).lower()

    if cidade=="0":
        print(f"{color1}Obrigado e volte sempre!{colorEnd}")
        break

    cidadeSplit=cidade.split()

    lista.append(cidadeSplit)

    if lista[0][0]=="santa":
        print(f"{color1}Sua cidade começa com 'Santa'{colorEnd}")
        lista.clear()
    else:
        print(f"{color2}Sua cidade não começa com 'Santa'{colorEnd}")
        lista.clear()
