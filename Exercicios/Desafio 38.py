"""
Desafio 38: Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
"O primeiro valor é maior"
"O segundo valor é maior"
"Não existe valor maior, os dois são iguais"
"""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cor,cabecalho

#Greetings!
cabecalho(cor("Bem vindo ao comparador de numeros da Prof(a) Alexa",35))

#Criando uma função que irá comparar numeros de acordo com a quantidade inserida como parametro
def maior_menor(quant=2):
    """
    Função que irá comparar numeros (quantidade de numeros inserida como parametro) e no final irá dizer qual foi o maior e menor numero digitado
    
    quant = Quantidade de numeros a serem comparados    
    
    """    
    
    #Armazenando o maior e menor numero em variaveis
    maior=float('inf')
    menor=float('-inf')

    #Solicitando numeros (de acordo com o valor em parametro) ao usuario
    for n in range(quant):        
        #Tratamento de erros
        while True:
            try:
                num=int(input(f"Digite o {n+1}º numero: "))
                break
            except ValueError:
                print(cor("Erro! Digite somente valores numericos!",31))
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa...")
        
        #Efetuando a comparação dos numeros digitados acima
        if n==0:
            maior=num
            menor=num
        else:
            if num > maior:
                maior=num
            if num < menor:
                menor=num

    #Imprimindo os resultados
    if maior==menor:
        print(cor(f"\nNão existe valor maior, os {quant} numeros são iguais",35))
    else:
        print(cor(f"\nMaior: {maior}",31))
        print(cor(f"Menor: {menor}",34))
    
#Programa principal
while True:    
    
    #Tratamento de erro
    while True:
        try:    
            quant_numeros=int(input("Quantos iremos iremos comparar: "))
            break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos!",31))
        except KeyboardInterrupt:
            print("\nO usuario cancelou o programa...")
    
    #Chamando a função para a comparação dos numeros
    maior_menor(quant_numeros)
    
    #Escolha ao usuario para que o programa continue ou não
    while True:
        c=str(input("\nDeseja continuar? [S/N]")).upper()
        
        if c in ["S","N"]:            
            print()
            break
        else:
            print(cor("Erro! Digite somente 'S' para continuar ou 'N' para sair do programa!",31))
    
    if c == "N":
        print(cor("Obrigada e volte sempre!",35))
        break