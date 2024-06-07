"""Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse modulo e use algumas dessas funções."""

from Modulos import moeda

p=float(input("Digite o preço: R$"))
print(f"A metade de R${p} é R${moeda.metade(p)}.")
print(f"O dobro de R${p} é R${moeda.dobro(p)}.")
print(f"Aumentando 10%, temos R${moeda.aumentar(p,10)}.")
print(f"Diminuindo 10%, temos R${moeda.diminuir(p,10)}.")
    
