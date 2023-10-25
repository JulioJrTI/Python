"""Desafio 97: Faça um programa que tenha uma função chamada "escreva()", que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.

Ex: escreva("Olá, Mundo!")

Saida: ----------

Olá, Mundo!

----------"""

def escreva(msg):
    tam=len(msg)+4
    print("~"*tam)    
    print(f"  {msg}")
    print("~"*tam)

escreva("Alexa soltou um pum bem gostoso.")
escreva("Tem cheiro de flores")