"""Desafio 20: O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

import random

enfeite="=-"*3
color1="\033[1;32m"
color2="\033[1;34m"
colorEnd="\033[m"

alunos=[]
cont=0
pergunta=True

print(enfeite,f"{color1}Bem vindo ao sorteador de listas de alunas da Alexa 2.0!{colorEnd}",enfeite)
while cont < 4:    
    if pergunta:
        aluno=str(input(f"{color1}Digite o nome da {cont+1}º aluna: {colorEnd}"))
        alunos.append(aluno)
        cont+=1
        random.shuffle(alunos)        

    if cont==4:
        pergunta=False
        c=int(input(f"Deseja efetuar alguma alteração?\n1)Mudar alunas\n2)Sair do programa e mostra lista\n"))
        if c==1:            
            alunos.clear()
            cont=0
            pergunta=True            
        elif c==2:
            break

print(enfeite)
print(f"Segue ordem de alunas sorteadas: ")
for ordem,nome in enumerate(alunos):
    print(f"{color1}{ordem+1}º:{colorEnd} {color2}{nome}{colorEnd}")