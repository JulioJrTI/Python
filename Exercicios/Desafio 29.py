"""Desafio 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

color1="\033[1;32m"
colorRed="\033[1;31m"
colorEnd="\033[m"

print(f"{color1}Bem vindo ao acelerotrometro da Alexa!{colorEnd}")
while True:
    multas=[0,80,7]
    carro=int(input("Digite a velocidade de seu carro: Km\n"))
    multas[0]=carro    
    
    if multas[0] > multas[1]:
        print(f"{colorRed}Seu carro foi multado!{colorEnd}")
        print(f"Segue valor da multa {colorRed}R$ {(multas[0]-multas[1])*multas[2]:.2f}{colorEnd}")
    else:
        print(f"{color1}Tudo certo por aqui!")
        print(f"Obrigado e tenha um bom dia!{colorEnd}")

    c=str(input("Deseja efetuar nova verificação? [S/N]"))

    if c in "Ss":
        multas.clear()
    elif c in "Nn":
        print(f"{color1}Obrigado e tenha um bom dia \03!{colorEnd}")
        break