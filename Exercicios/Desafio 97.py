"""Desafio 97: Faça um programa que tenha uma função chamada "escreva()", que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.

Ex: escreva("Olá, Mundo!")

Saida: 
----------
Olá, Mundo!
----------"""

#Definindo uma função que irá receber um texto ao ser chamada e efeitos cosmeticos de acordo com o tamanho da frase
def escreva(EscrevaUmTextoAqui):
    print("-"*len(EscrevaUmTextoAqui))
    print(EscrevaUmTextoAqui)
    print("-"*len(EscrevaUmTextoAqui))

escreva("Alexa ganhou um presente!")