"""Desafio 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido."""

import random

alunos=[[],[]] #Iremos colocar os nomes das alunas na primeira sublista e a aluna sorteada irá para a segunda

for a in range(4):
    aluno=str(input(f"Digite o nome do {a+1} aluno: "))
    alunos[0].append(aluno)
sorteio=random.choice(alunos[0])
alunos[1].append(sorteio) #Aluna sorteada irá para a segunda sublista
    
print(f"Temos 4 alunas na classe e seus nomes são: ",end="")
for aluna in alunos[0]:    
    print(f"{aluna}, ",end="")
print(f"\nA aluna escolhida para apagar o quadro foi: {alunos[1][-1]}")
