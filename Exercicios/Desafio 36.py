"""Desafio 36: Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

from time import sleep

print("Bem vindo ao calculador de compras de imoveis da Alexa!")
while True:
    casa=float(input("Digite o valor da casa que deseja comprar: R$"))
    salario=float(input("Digite seu salario atual: R$"))
    anos=int(input("Digite a quantidade de anos que deseja parcelar sua compra: "))

    programa={"Casa":casa,"Salario":salario,"Anos":anos}    

    prestacao=programa["Casa"]/(programa["Anos"]*12)
    minimo=programa["Salario"]*30/100    
    
    print()
    print(f"A casa que seja comprar custa R${programa['Casa']:.2f}")
    sleep(1)
    print(f"A casa será paga em {programa['Anos']} anos.")
    sleep(1)
    print(f"Segue valor da prestaçã o: R${prestacao:.2f}")
    sleep(1)    

    if prestacao<=minimo:
        print(f"{color1}Compra aprovada!{colorEnd}")
        print()
    else:
        print(f"{color2}Compra negada!{colorEnd}")
        print()

    c=str(input("Deseja efetuar nova verificação: [S/N]"))

    if c in "Ss":
        continue
    elif c in "Nn":
        print(f"{color1}Obrigado e volte sempre!{colorEnd}")
        break