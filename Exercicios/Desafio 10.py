"""Desafio 10: Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""

color1 = "\033[1;32m"
colorEnd = "\033[m"

cart = []
dolar = 4.85

print ( f"{color1}Bem vindo a carteira da Alexa!{colorEnd}" )
print ( "=-" * 30 )

while True :
    cart.append ( float ( input ( "Digite a quantidade total guardada na carteira: R$" ) ) )
    for v in cart :
        conv = v / dolar
        print ( f"{color1}Com R${v:.2f} podemos efetuar USD ${conv:.2f} em compras.{colorEnd}" )
    print ( "=-" * 30 )
    c = str ( input ( "Deseja efetuar nova conversão? [S/N]" ) )
    if c in "Ss" :
        cart.pop ()
    else :
        print ( f"{color1}Obrigado e boas compras!{colorEnd}" )
        break
