"""
Desafio 37: Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
[1] para binario
[2] para octal
[3] para hexadecimal
"""

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor

#Função que irá converter um valor inserido como parametro para bi, octa e hex tbm inserido como parametro
def conversor_numero(num,base):
    """
    Função simples que irá converter um valor numerico (inserido como primeiro parametro) para a base escolhida (bi, oct, hex) no segundo parametro.
    
    num = Numero que será convertido
    conv = Base para a conversao: bin, oct, hex    
    """
    
    if base=='bin':
        return bin(num)[2:]
    elif base=='oct':
        return oct(num)[2:]
    elif base == 'hex':
        return hex(num)[:2]
    else:
        return None

#Greetings!
cabecalho(cor("Bem vindo ao conversor de numeros da Prof(a) Alexa!",35))

#Programa principal
while True:   

    #Tratamento de erro
    while True:
        try:            
            #Solicitando um numero inteiro para o usuario
            num=int(input("Insira um numero inteiro (Ex: 6): "))
            break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos!",31))
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa",34))

    #Tratamento de erro
    while True:    
        try:
            #Menu de escolhas para a conversão
            c=int(input(cor(f"\nDeseja converter o numero '{num}' para:\n[1] Binario\n[2] Octal\n[3] Hexadecimal\nInsira sua escolha: ")))
            
            if c > 3:
                print(cor("Escolha invalida!",31))
            else:
                break
        except ValueError:
            print(cor("Erro! Digite somente valores numericos para a escolha de conversão!",31))
        except KeyboardInterrupt:
            print(cor("\nO usuario cancelou o programa",34))            
        
    #Cada numero inserido pelo usuario como escolha, ira receber a base para conversão
    choice={1:'bin',
            2:'oct',
            3:'hex'}
    
    #Base irá receber o valor escolhido acima
    base = choice[c]    
    
    #Convertendo e imprimindo o valor inserido de acordo com a escolha de base acima
    numero_convertido = conversor_numero(num,base)
    cabecalho(cor(f"O numero '{num}' convertido para '{base}' é igual a '{numero_convertido}'.",35),cent=0,quantC=50)

    #Continuar ou não o programa
    c2=str(input("\nDeseja continuar? [S/N]")).upper()

    if c2 == "N":
        print(cor("\nObrigado e volte sempre!",35))
        break