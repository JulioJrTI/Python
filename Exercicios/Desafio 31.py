"""Desafio 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

print(f"{color1}Bem vindo ao calculador de viagem da Alexa!{colorEnd}")
while True:
    viagem=int(input("Digite a distancia de sua viagem (ou digite 0 para sair): Km "))

    if viagem==0:
        print(f"{color1}Obrigado e volte sempre!{colorEnd}")
        break

    Km200=0.50
    Km201=0.45

    print("=-"*10)
    if viagem<=200:
        print(f"{color1}Viagem inferior ou igual a 200Kms")
        print(f"Segue valor da viagem: R${(viagem)*Km200:.2f}{colorEnd}")
    else:
        print(f"{color2}Viagem superior a 200Kms")
        print(f"Segue valor da viagem: R${(viagem)*Km201:.2f}{colorEnd}")

    