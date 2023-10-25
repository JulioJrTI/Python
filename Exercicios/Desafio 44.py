"""Desafio 44: Elabore um programa que calcule o valor a ser pago por produto, considerando o seu preço normal e condição de pagamento:

-A vista dinheiro/cheque: 10% de desconto.

-A vista no cartão: 5% desconto.

-Em até 2x no cartão: Preço normal.

-3x ou mais no cartão: 20% de juros."""

color1="\033[1;32m"
colorRed="\033[1;31m"
colorEnd="\033[m"
enfeite="-="*10

print(f"{color1}Bem vindo a loja da Alexa!{colorEnd}")
while True:
    produto=float(input("Digite o valor de seu produto: R$"))

    print("Como deseja efetuar o pagamento:")
    c1=int(input(f"[1] A vista dinheiro/cheque com 10% de desconto\n"
    "[2] A vista no cartão com 5% de desconto\n"
    "[3] Em 2x no cartão, sem juros\n"
    "[4] 3x ou mais no cartão com 20% de juros\n"))

    print(enfeite)
    print(f"Valor do produto R${produto:.2f}")
    if c1==1:
        desconto=10
        novoValor=produto-(produto*desconto/100)
        print(f"Produto recebeu 10% de desconto")
    if c1==2:
        desconto=5
        novoValor=produto-(produto*desconto/100)
        print(f"Produto recebeu 5% de desconto")
    if c1==3:
        parcelas=2
        novoValor=produto/parcelas
        print(f"Produto será pago em 2x, valor das parcelas: R${novoValor:.2f}")
    if c1==4:
        while True:
            parcelas=int(input(("Em quantas vezes deseja parcelar: ")))
            if parcelas >=3:
                break        
            else:    
                print(f"{colorRed}Está opção somente é valida para pagamentos superiores a 3x ou mais, tente novamente{colorEnd}")     
        parcelasValor=produto/parcelas
        novoValor=parcelasValor+(parcelasValor*20/100)
        print(f"Produto será pago em {parcelas}x, valor das parcelas R${novoValor:.2f} com 20% de juros.")

    if c1==1 or c1==2:
        print(f"Segue valor para pagamento: R${novoValor:.2f}")
    print(enfeite)
    
    c2=str(input("Deseja continuar: [S/N]"))

    if c2 in "Nn":
        print(f"{color1}Obrigado e volte sempre!{colorEnd}")
        break









