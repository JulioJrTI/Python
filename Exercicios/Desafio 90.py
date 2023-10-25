"""Desafio 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionario. No final, mostre o conteúdo da estrutura na tela.

-Média abaixo de 5.0: Reprovado

-Média entre 5.0 e 6.9: Recuperação

-Média entre 7.0 ou superior: Aprovado"""

color_1="\033[1;32m"
color_2="\033[1;33m"
color_3="\033[1;31m"
color_Reset="\033[m"

alunos={"Nome":[],"Nota 1":[],"Nota 2":[],"Media":[],"Status":[]} #Dicionario contendo Nome, Notas, Media de notas e status dos alunos

print(f"{color_1}Bem vindo ao calculador de provas da Prof(a) Alexa!{color_Reset}")

#Programa principal
while True:
    #Inserido o nome do aluno
    while True:
        nome=str(input("Digite o nome do(a) aluno(a): "))
        if nome.isalpha():
            alunos["Nome"].append(nome) #Adicionando o nome do aluno ao dicionario
            break
        else:
            print(f"{color_3}Erro! Digite somente letras!{color_Reset}")        
    
    #Inserindo a primeira nota
    while True:
        try:
            nota1=float(input("Digite a primeira nota do(a) aluno(a): "))
            alunos["Nota 1"].append(nota1) #Adicionando a primeira nota do aluno ao dicionario
            break
        except:
            print(f"{color_3}Erro! Digite somente numeros!{color_Reset}")
    
    #Inserindo a segunda nota
    while True:
        try:
            nota2=float(input("Digite a segunda nota do(a) aluno(a): "))
            alunos["Nota 2"].append(nota2) #Adicionando a segunda nota do aluno ao dicionario
            break
        except:
            print(f"{color_3}Erro! Insira somente numeros!{color_Reset}")    
    
    #Calculando a media de notas
    media=(nota1+nota2)/2 #Calculando a media de notas do aluno
    alunos["Media"].append(media)

    #Verificando o status do aluno
    if media<5: #Se a media de notas for inferior a 5, o aluno será reprovado
        alunos["Status"].append(f"{color_3}Reprovado!{color_Reset}")    
    elif media>=5 and media<=6.9: #Se a media de notas for entre 5 e 6.9, o aluno estará de recuperação
        alunos["Status"].append(f"{color_2}Recuperação!{color_Reset}")
    else: #Se a nota for maior do que 6.9, o aluno foi aprovado
        alunos["Status"].append(f"{color_1}Aprovado!{color_Reset}")

    #Perguntando se o usuario deseja continuar cadastradando alunos
    while True:
        c=str(input("Deseja continuar? [S/N]")).upper()[0]
        if c in ["S","N"]:
            break
        else:
            print(f"{color_3}Erro! Escolha somente S ou N!{color_Reset}")
    
    if c in "Nn":
        print(f"{color_2}<<< FIM >>>{color_Reset}")
        break

#Resumo geral
print(f"{color_1}Resumo geral de alunos:{color_Reset}")
for i in range(len(alunos["Nome"])):
    print(f"Nome: {alunos['Nome'][i]}")
    print(f"Media de notas: {alunos['Media'][i]}")
    print(f"Status: {alunos['Status'][i]}")
    print("-="*10)