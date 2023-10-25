"""Desafio 13: Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento."""

color = "\033[1;32m"
colorEnd = "\033[m"

funcionarioNome = []
funcionarioSalario = []
aumento = 15

while True :
    print ( "=-" * 50 )
    funcionario = str ( input ( "Digite o nome do funcionario: " ) )
    funcionarioNome.append ( funcionario )

    salario = float ( input ( "Digite o salario deste funcionario: R$" ) )
    funcionarioSalario.append ( salario )

    c = input ( "Deseja continuar? [S/N]" )

    if c in "Nn" :
        break

for nome, salario in zip ( funcionarioNome, funcionarioSalario ) :  # Combinando as duas listas em fileiras verticais
    print ( f"Nome: {nome}" )
    print ( f"Salario: R${salario:.2f}" )
    novoSalario = salario + (salario * aumento / 100)
    print ( f"{color}Seu salario sofreu um aumento de 15%, segue novo salario: R${novoSalario:.2f}.{colorEnd}" )
    print ( "=-" * 30 )
