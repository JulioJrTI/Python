"""Desafio 09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada."""

while True :
    numero = int ( input ( "Digite qual tabuada deseja estudar: [Digite 0 para sair]" ) )
    while numero != 0 :
        print ( "=-" * 30 )
        for n in range ( 1, 11 ) :
            print ( f"{numero}x{n}={numero * n}" )
        break
    print ( "=-" * 30 )
    if numero == 0 :
        print ( "Obrigado e bons estudos!" )
        break
