"""Desafio 109: Modifique as funções que foram criadas no Desafio 107 para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no Desafio 108."""

from Modulos import moeda

p=float(input("Digite o preço: R$"))

print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p,f=True)}.")

print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p,f=True)}.")

print(f"Aumentando 10%, temos {moeda.aumentar(p,10,f=True)}.")

print(f"Diminuindo 10%, temos {moeda.diminuir(p,10,f=True)}.")