"""Desafio 46: Faça um programa que mostre na tela uma contagem regressiva 
para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundos entre eles."""

#Usando de modulos para a formatação do programa
from Modulos.formatar import cor,cabecalho,emotes
from Modulos.matematica import contador_reverso

#Limpando o terminal
from os import system
system("cls")

#Descobrindo o ano atual
from datetime import date

#Ano atual
ano_atual = date.today().year

#Greetings
cabecalho(cor("Pronto para o ano novo?"))

#Mensagem de erro
msg_erro=cor("\nErro! Digite somente valores numericos\n",31)

#Solicitando um numero inicial
while True:
    try:
        num_inicio=int(input("Digite um valor numerico inicial: "))
        break
    except ValueError:
        print(msg_erro)    
        
#Solicitando um numero final
while True:
    try:        
        num_fim=int(input("Digite um valor numerico final: "))
        break
    except ValueError:
        print(msg_erro)

print()

#Chamando a função de contador reverso
contador_reverso(num_inicio,num_fim,1)

#Mensagem que será exibida no final do contador
print(cor(f"\nFeliz {ano_atual}{emotes(2)} !!!",35))