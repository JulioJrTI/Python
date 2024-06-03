"""Desafio 01: Crie um programa que escreva "Olá, Mundo!" na tela."""

#Chamando a função de colorizar
from Modulos import Formatar 

#Iremos imprimir o titulo do programa usando funções de colorizar e centralizar
print(Formatar.cabecalho(Formatar.cor("Bem vindo ao Hello Worlds da Alexa!",32)))

#Iremos imprimir cada nome inserido em uma lista
listaGarotas=["Alexa","Dakota","Candice","Tegan","Thunder Rosa"]

#Iremos imprimir cada nome na lista acima, usando diferentes cores de acordo com o index da lista (Iremos colorir a partir do valor de cor 33)
for i,g in enumerate(listaGarotas):
    print(Formatar.cor(f"Olá {g}!",i+33))
    
    
