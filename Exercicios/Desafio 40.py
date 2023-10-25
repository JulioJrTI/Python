"""Desafio 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

-Média abaixo de 5.0: Reprovado

-Média entre 5.0 e 6.9: Recuperação

-Média entre 7.0 ou superior: Aprovado"""

from time import sleep

color1="\033[1;32m"
color2="\033[1;31m"
color3="\033[1;33m"
colorEnd="\033[m"

alunos={"Nome":[],"Nota 1":[],"Nota 2":[],"Media":[],"Resultado":[]}
print(f"{color1}Bem vindo a escolinha da Alexa!{colorEnd}")
while True:
    nome=str(input("Digite o nome do aluno: "))
    alunos["Nome"].append(nome)    
    
    nota1=float(input("Digite a primeira nota:"))
    alunos["Nota 1"].append(nota1)

    nota2=float(input("Digite a segunda nota: "))
    alunos["Nota 2"].append(nota2)

    media=(nota1+nota2)/2
    alunos["Media"].append(media)

    print("Calculando media do aluno...")
    sleep(2)
    print()
    print(f"Segue media do aluno: {media}")
    print()

    if media < 5.0:
        resultado=f"{color2}Reprovado!{colorEnd}"
        alunos["Resultado"].append(resultado)
        print(resultado)
    elif media >=5.0 and media<=6.9:
        resultado=f"{color3}Recuperação!{colorEnd}"
        alunos["Resultado"].append(resultado)
        print(resultado)
    else:
        resultado=f"{color1}Aprovado!{colorEnd}"
        alunos["Resultado"].append(resultado)
        print(resultado)
    print()
    c=str(input("Deseja continuar? [S/N]"))
    print()

    if c in "Nn":
        break

print(f"{color1}Segue lista de alunos cadastrados:{colorEnd}")
for i in range(len(alunos["Nome"])):
    print(f"Aluno: {alunos['Nome'][i]}")
    print(f"Nota 1: {alunos['Nota 1'][i]}")
    print(f"Nota 2: {alunos['Nota 2'][i]}")
    print(f"Media: {alunos['Media'][i]}")
    print(f"Resultado: {alunos['Resultado'][i]}")
    print("-="*10)