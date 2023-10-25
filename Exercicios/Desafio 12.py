"""Desafio 12: Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto."""

while True :
    produto = float ( input ( "Digite o valor de seu produto: R$" ) )
    desconto = int ( input ( "Quanto será o desconto: " ) )
    novo_desconto = produto - (produto * desconto / 100)
    print ( "-=" * 30 )
    print (
        f"O produto que antes custava R${produto:.2f}, \nagora com {desconto}% de desconto irá custar: R${novo_desconto:.2f}" )
    print ( "-=" * 30 )
    c = input ( "Deseja efetuar novo calculo: [S/N]" )

    if c in "Nn" :
        print ( "Obrigado e tenha um bom dia!" )
        break
