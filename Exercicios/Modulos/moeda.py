"""Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse modulo e use algumas dessas funções."""

#Função que irá aumentar o valor digitado de acordo com a taxa
def aumentar(preco,taxa):
    res=preco+(preco*taxa/100)
    return res
    
#Função que irá diminuir o valor digitado de acordo com a taxa
def diminuir(preco,taxa):
    res=preco-(preco*taxa/100)
    return res    

#Função que irá exibir o dobro do numero digitado
def dobro(preco):
    res=preco*2
    return res    

#Função que irá exibir a metade de um numero digitado 
def metade(preco):
    res=preco/2
    return res
    