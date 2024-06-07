"""Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

from Modulos.Formatar import cor,cabecalho
from Modulos.Dinheiro import conversaoReais,conversaoDolar

#Cotação atual
cotacaoAtual = 4.93 # 1$USD = R$4,93

cabecalho(cor("Bem vindo a carteira da Alexa!",35))
while True:

    #Tratamento de erros
    while True:    
        try:
            #Menu de escolhas
            c=int(input("[1] Converter Reais para Dolar\n[2] Converter Dolar para Reais\n[3] Alterar a cotação atual\n[4] Sair do programa\nDigite sua escolha: "))
            
            #Se o usuario escolher um valor entre 1 e 4, o programa irá proseguir
            if c in [1,2,3,4]:
                break
            #Caso contrario, iremos exibir uma mensagem de erro
            else:
                print(cor("Erro! Por favor insira um valor entre 1 e 4 para a escolha desejada!",31))
       
        #Se o usuario inserir qualquer valor alem de numeros, iremos exibir uma mensagem de erro
        except ValueError:
            print(cor("Erro! Insira somente valores numericos!",31))
        except KeyboardInterrupt:
                print(cor("\nUsuario saiu do programa.",31))
                quit()
    
    #Conversão de R$ para $USD
    if c == 1:
        #Tratamento de erro
        while True:
            try:
                #Perguntando ao usuario o valor total em REAIS em sua carteira
                carteiraReais=float(input("Digite quantos R$ vc tem em sua carteira: "))
                break
            except ValueError:
                print(cor("Erro! Por favor digite somente valores monetarios! Exemplo: 10.50",31))
            except KeyboardInterrupt:
                print(cor("\nUsuario saiu do programa.",31))
                quit()

        #Usando de uma função para converter R$ para $USD
        cDolar = conversaoDolar(carteiraReais,cotacaoAtual)
        
        #Imprimindo o resultado
        cabecalho(f"Com R${carteiraReais:.2f} reais vc irá conseguir comprar ${cDolar:.2f} em dolar.",cent=0)
        
    #Conversão de $USD para R$
    if c == 2:
        #Tratamento de erro
        while True:
            try:
                #Perguntando ao usuario o valor total em DOLARES em sua carteira
                carteiraDolar=float(input("Digite quantos $USD vc tem em sua carteira: "))
                break
            except ValueError:
                print(cor("Erro! Por favor digite somente valores monetarios! Exemplo: 10.50",31))
            except KeyboardInterrupt:
                print(cor("\nUsuario saiu do programa.",31))
                quit()
        
        #Usando de uma função para converter USD$ para R$
        cReais = conversaoReais(carteiraDolar,cotacaoAtual)
        
        #Imprimindo o resultado
        cabecalho(f"Com {carteiraDolar:.2f}$ vc irá conseguir comprar R${cReais:.2f} em reais.",cent=0)
        
    #Alteração na cota atual
    if c == 3:
        print(f"Cotação atual: {cotacaoAtual}")
        
        #Tratamento de erro
        while True:
            try:
                cotacaoAtual=float(input("Digite a nova cotação: 1$USD = R$"))
                break
            except ValueError:
                print(cor("Erro! Por favor digite somente valores monetarios! Exemplo: 5.55",31))
            except KeyboardInterrupt:
                print(cor("\nUsuario saiu do programa.",31))
                quit()
    
    #Sair do programa
    if c == 4:
        print(cor("\nObrigado e volte sempre!",35))
        break