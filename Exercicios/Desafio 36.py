"""
Desafio 36: Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.
"""

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Greetings!
cabecalho(cor("Bem vindo ao sistema bancario da Alexa!",35))

#Iremos cadastrar cada pessoa em um dicionario
cadastroPessoas={"Nome":[],"Valor da Casa":[],"Salario":[],"Anos de parcelamento":[],"Resultado":[]}

#Solicitando o nome do cliente
nome_cliente = input("Digite seu nome: ")
cadastroPessoas["Nome"].append(nome_cliente)

#Tratamentos de erros
while True:
    try:
        #Solicitando o valor da casa que o usuario deseja comprar
        valor_casa = float(input(f"Olá{nome_cliente}, Digite o valor da casa que deseja financiar: R$"))
        cadastroPessoas["Valor da Casa"].append(valor_casa)
        break
    except ValueError:
        print(cor("Erro! Digite somente valores monetarios (Ex: 1500,00)",31))
    except KeyboardInterrupt:
        print("\nO usuario cancelou o programa")

#Tratamentos de erros
while True:
    try:
        #Solicitando o valor salarial do usuario
        salario=float(input("Digite seu salario: R$"))
        cadastroPessoas["Salario"].append(salario)
        break
    except ValueError:
        print(cor("Erro! Digite somente valores monetarios (Ex: 1500,00)",31))
    except KeyboardInterrupt:
        print("\nO usuario cancelou o programa")
        
#Tratamentos de erros
while True:
    try:
        #Perguntando ao usuario em quantos anos o mesmo irá pagar a casa
        anos_aPagar = int(input("Em quantos anos deseja parcelar: "))
        cadastroPessoas["Anos de parcelamento"].append(anos_aPagar)
        break
    except ValueError:
        print(cor("Erro! Digite somente valores numericos (Ex: 5)",31))
    except KeyboardInterrupt:
        print("\nO usuario cancelou o programa")

#Para calcularmos a prestação, iremos dividir o valor total da casa com a quantidade de anos a pagar, multiplicado por 12 (meses)
prestacao = valor_casa/(anos_aPagar*12)

#Para calcularmos o minimo necessario para que seja aprovada o financiamento
minimo = salario*30/100

#Se o valor da prestação for abaixo ou igual ao minimo de 30% do salario do usuario, a compra é aprovada, caso contrario é negada
if prestacao <= minimo:
    resultado="Compra Aprovada!"
else:
    resultado="Compra Negada!"
cadastroPessoas["Resultado"].append(resultado)

print(cadastroPessoas)