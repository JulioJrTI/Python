"""Desafio 18: Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo."""

import math
from os import system
from Modulos.Formatar import cor,cabecalho,emotes

#Limpando o terminal a cada execução do programa
system("cls")

#Greetings!
cabecalho(cor(f"Bem vindo ao calcular de Seno, Cosseno e Tangente da Prof(a) Alexa! {emotes(2)} ",35),quantC=68)

#Tratamento de erros
while True:
    try:
        #Solicitando um valor para o TA
        ta = float(input("Digite um valor para o Tangente Adjacente: "))
        break
    except ValueError:
        print(cor("Erro! Digite somente valores numericos (Exemplo: 6.9)",31))
    except KeyboardInterrupt:
        print(cor("\nO usuario cancelou o programa...",31))
        break

#Tratamento de erros
while True:
    try:
        #Solicitando um valor para o TO
        to = float(input("Digite um valor para o Tangente Oposto: "))
        break
    except ValueError:
        print(cor("Erro! Digite somente valores numericos (Exemplo: 6.9)",31))
    except KeyboardInterrupt:
        print(cor("\nO usuario cancelou o programa...",31))
        break        

#Calculando o valor de Ta ao quadrado
taQuadrado = (ta**2)

#Calculando o valor de To ao quadrado
toQuadrado = (to**2)

#Somando os valores de Ta e To acima
somaTaTo = (taQuadrado+toQuadrado)

#Calculando a raiz quadrada do resultado da soma acima
hipo = math.sqrt(somaTaTo)

print(cor(f"\nO Tangente Adjacente {ta} e Tangente Oposto {to} tem sua hipotenusa igual a ~{hipo:.2f}",32))

if hipo!=0: 
    #Calculando o seno ao dividir o tangente adjacente pelo resultado da hipotenusa
    seno = (ta / hipo)

    #Calculando o cosseno ao dividir o tangente oposto pelo resultado da hipotenusa
    cos = (to/hipo)
    
    #Se o valor do tangente oposto não for igual a 0
    if to!=0:
        #Calculando o tangente ao dividir o tangente adjacente pelo tangente oposto
        tan = (ta / to)
        print(cor(f"\nO valor do Tangente é igual a ~{tan:.2f}",36))
    else:
        print(cor("O tangente oposto é zero. Não é possivel calcular o Tangente!",31))
        
    print(cor(f"\nO valor do Seno é igual a ~{seno:.2f}\n\nO valor do Cosseno é igual a ~{cos:.2f}",34))    
else:
    print(cor("A hipotenusa é zero. Não é possivel calcular Seno e Cosseno!",31))

#Mensagem final
print(cor(f"\nFim do programa...{emotes(2)}"))