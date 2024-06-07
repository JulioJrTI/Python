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

#Efeito cosmetico de delay
from time import sleep

#Controle boolean se iremos aplicar juros ou não ao produto
juros=False

#Programa principal
while True:
    
    #Greetings
    cabecalho(cor("Bem vindo ao supermercado da Alexa!",35))

    #Preço original do produto
    while True:    
        try:            
            preco_produto = float(input("Digite o preço do produto (Exemplo 150.00): R$ "))
            break
        except ValueError:
            print(cor("Erro! Insira somente valores monetarios! (Exemplo 150.00)",31))

    #Metodo de pagamento    
    mp_lista=["[0] A vista dinheiro/cheque",
            "[1] Cartão de credito"]

    #Imprimindo menu de escolhas
    print(cor("\nMetodo de pagamento",33))
    for menu in mp_lista:
        print(menu)
    mp = int(input("Insira: "))

    #A vista dinheiro/cheque
    if mp == 0:
        desconto = 10
        preco_com_desconto = preco_produto-(preco_produto*10/100)    

    #A vista ou parcelado no cartão de credito
    if mp == 1:
        quant_parcela = int(input("\nQuantas vezes deseja parcelar: "))
        
        #A vista no cartão
        if quant_parcela == 1:
            desconto = 5
            preco_com_desconto = preco_produto-(preco_produto*5/100)
        
        #Em até 2x no cartão
        elif quant_parcela == 2:
            desconto = 0
            preco_com_desconto = preco_produto
            parcela = preco_com_desconto / quant_parcela
        
        #Acima de 2x no cartão
        else:        
            acrescimo=20
            preco_com_juros = preco_produto+(preco_produto*acrescimo/100)
            parcela = preco_com_juros / quant_parcela
            juros=True            
            
    #Resumo a pagar
    print("\033[1;32m")
    print(f"\nOpção escolhida: {mp_lista[mp][3:]}")
    sleep(1)
    print(f"Preço original do produto: R${preco_produto:.2f}")    
    if mp == 1:
        if quant_parcela >= 2:
            if juros:
                print(f"{acrescimo}% de acréscimo")
                print(f"A pagar: R${preco_com_juros:.2f}")
            else:
                print(f"{desconto}% de desconto")
                print(f"A pagar: R${preco_com_desconto:.2f}")
            print(f"Parcelas a pagar: {quant_parcela}x de R${parcela:.2f}")
        else:
            print(f"{desconto}% de desconto")
            print(f"A pagar: R${preco_com_desconto:.2f}")
    elif mp == 0:
        print(f"{desconto}% de desconto")
        print(f"A pagar: R${preco_com_desconto:.2f}")
    print("\033[m")
    
    #Continuar ou não o programa
    c = str(input("\nDeseja continuar? [S/N]")).upper()[0]
    
    if c in "S":
        system("cls")    
    elif c in "N":
        print(cor("\nOBRIGADO E VOLTE SEMPRE!",35))
        break