"""Desafio 101: Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições."""

from datetime import date

#Função
def voto(a=0):
    print("_"*50)
    print(f"Com {idade} anos seu voto é: ",end="")
    if idade >=18 and idade <=70:
        print("OBRIGATORIO")
    elif idade >=16 and idade <=17 or idade >70:
        print("OPCIONAL")
    elif idade<16:
        print("NEGADO")   

#Calculo de idade
anoAtual=date.today().year
anoNascimento=int(input("Ano de nascimento: "))
idade=(anoAtual-anoNascimento)

#Imprimindo a função
voto(anoNascimento)