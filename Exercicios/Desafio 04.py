"""Desafio 04: Faça um programa que leia algo pelo teclado e mostre na tela o seu primitivo e todas as informações possiveis sobre ele."""

color = "\033[1;32m"
colorEnd = "\033[m"

valores = []

while True:
    valores.append(input(f"Digite uma palavra ou numero, {len(valores) + 1}º: "))
    c = input('Deseja continuar? [S/N]')

    if c in "Nn":
        break

for i, v in enumerate(valores):
    print("+-" * 50)
    print(f"Valor: {color}{v}{colorEnd}\n"
          f"Tipo: {type(v)}\n"
          f"Somente espaços: {v.isspace()}\n"
          f"Somente numeros: {v.isnumeric()}\n"
          f"Somente palavras: {v.isalpha()}\n"
          f"São palavras e ou numeros: {v.isalnum()}\n"
          f"São palavras em maiu: {v.isupper()}\n"
          f"São palavras em minu: {v.islower()}\n"
          f"A primeira letra está em maiu: {v.istitle()}")
