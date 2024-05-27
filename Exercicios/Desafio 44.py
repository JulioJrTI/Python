"""Desafio 44: Elabore um programa que calcule o valor a ser pago por produto, considerando o seu preço normal e condição de pagamento:
-A vista dinheiro/cheque: 10% de desconto.
-A vista no cartão: 5% desconto.
-Em até 2x no cartão: Preço normal.
-3x ou mais no cartão: 20% de juros."""

#Usando modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Greetings
cabecalho(cor("Bem vindo ao supermercado da Alexa!",35))

#Preço original do produto
preco_produto = float(input("Digite o preço do produto: R$ "))

#Metodo de pagamento
mp_lista=["[0] A vista dinheiro/cheque",
    "[1] A vista no cartão",
    "[2] Parcelado no cartão"]

print(mp_lista)
mp = int(input("Insira: "))

#A vista dinheiro/cheque
if mp == 0:
    desconto = 10
    preco_com_desconto = preco_produto-(preco_produto*10/100)

#A vista no cartão
if mp == 1:
    desconto = 5
    preco_com_desconto = preco_produto-(preco_produto*5/100)
    
if mp == 2:
    quant_parcela = int(input("Quantas vezes deseja parcelar: "))
    
    if quant_parcela <= 2:
        

print(f"Opção escolhida: {mp_lista[mp][3:]}")
print(f"Preço original do produto: R${preco_produto:.2f}")
print(f"-{desconto}% desconto")
print(f"A pagar: R${preco_com_desconto:.2f}")