"""Desafio 03: Crie um programa que leia dois numeros e mostre a soma entre eles."""

numeros = []

while True :
    for n in range ( 2 ) :  # Um loop de 2 numeros
        numeros.append ( int ( input (
            f"Digite o {len ( numeros ) + 1}º numero: " ) ) )  # Usando o len() para sabermos a ordem dos numeros
    for i, n in enumerate ( numeros ) :  # Tratando da ordem dos numeros inseridos na lista
        if i == len ( numeros ) - 1 :  # Se for o ultimo numero da lista, iremos mostrar este numeros sem o sinal de +
            print ( n, end=" " )
        else :  # Caso sejam os primeiros
            print ( f"{n} + ", end="" )
    print ( f"= {sum ( numeros )}" )  # Iremos mostrar a soma dos numeros na lista
    break
