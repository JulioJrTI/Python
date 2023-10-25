"""Desafio 15: Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

color = "\033[1;32m"
colorEnd = "\033[m"

print ( f"{color}Bem vindo ao carrometro da Alexa!{colorEnd}" )
while True :
    kmRodado = int ( input ( "Digite a quantidade de KM percorridos: " ) )
    kmPreco = kmRodado * 0.15

    diasAlugados = int ( input ( "Digite a quantidade de dias alugados: " ) )
    diasPreco = diasAlugados * 60

    aPagar = kmPreco + diasPreco

    print ( f"{color}A pagar: R${aPagar:.2f}{colorEnd}" )

    c = int ( input ( "[1]Deseja efetuar nova verificação\n"
                      "[2]Sair do programa\n" ) )

    if c == 1 :
        continue
    elif c == 2 :
        print ( f"{color}Obrigado e volte sempre!{colorEnd}" )
        break
