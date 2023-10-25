"""Desafio 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permite que o usuário possa mostrar as notas de cada aluno individualmente."""

color_1="\033[1;32m"
color_2="\033[1;31m"
color_reset="\033[m"

#Programa principal
alunos={"Nome":[],"Nota 1":[],"Nota 2":[],"Media":[]} #Dicionario contendo listas de nomes, notas e media de notas de alunos.

print(f"{color_1}Bem vindo ao listador de alunos e notas da Alexa!{color_reset}")
while True:
    while True:
        nome=str(input("Digite o nome do(a) aluno(a): "))
        if nome.isalpha():
            alunos["Nome"].append(nome) #Adicionando nome do aluno ao dicionario.
            break
        else:
            print(f"{color_2}Erro! Insira somente letras!{color_reset}")
    
    while True:
        try:
            n1=float(input("Digite a primeira nota: "))
            alunos["Nota 1"].append(n1) #Adicionando a primeira nota do aluno ao dicionario.
            break
        except:
            print(f"{color_2}Erro! Insira somente numeros!{color_reset}")
    
    while True:
        try:    
            n2=float(input("Digite a segunda nota: ")) 
            alunos["Nota 2"].append(n2) #Adicionando a segunda nota do aluno ao dicionario.
            break
        except:
            print(f"{color_2}Erro! Insira somente numeros!{color_reset}")

    media=(n1+n2)/2 #Somando a media de notas.   
    alunos["Media"].append(media) #Adicionando a media de notas do aluno ao dicionario.
    print(f"Media de notas: {media}")

    while True:        
        c=str(input("Deseja continuar? [S/N]")).upper()[0]

        if c in ["S","N"]:
            break
        else:
            print(f"{color_2}Erro! Digite somente S ou N!{color_reset}")

    if c in "Nn":
        break
print("<<<< FIM >>>>")

#Resumo geral
print(f"{color_1}Resumo geral dos alunos:{color_reset}") #Resumo geral de alunos, notas e media.
for i in range(len(alunos["Nome"])):
    print("-="*10)
    print(f"Nome do(a) aluno(a): {alunos['Nome'][i]}")
    print(f"Notas do(a) aluno(a): {alunos['Nota 1'][i]} e {alunos['Nota 2'][i]}")
    print(f"Media de notas: {alunos['Media'][i]}")
    print("-="*10)

#Verificação especifica
while True:
    while True:    
        c1=str(input("Deseja verificar notas de algum aluno especifico? [S/N]")).upper()[0]
        if c1 in ["S","N"]:
            break
        else:
            print(f"{color_2}Erro! Escolha somente S ou N!{color_reset}")
    
    if c1 in "Ss":
        print("-="*10)
        print("Alunos:")
        for i, n in enumerate(alunos["Nome"]): #Mostrando o indice e nomes de alunos cadastradas ao dicionario.
            print(f"{i}: {n}")
        print("-="*10)
            
        index_aluno=int(input(f"Qual aluno deseja verificar? [0 a {len(alunos['Nome'])-1}]"))
        for i in range(len(alunos["Nome"])):
            if i==index_aluno: #Se o valor inserido no input bate com o valor de index do dicionario.            
                print("-="*10)
                print(f"Aluno(a) '{alunos['Nome'][i]}'")
                print(f"Notas: {alunos['Nota 1'][i]} e {alunos['Nota 2'][i]}")
                print(f"Media: {alunos['Media'][i]}")
                print("-="*10)
    
    elif c1 in "Nn":
        print(f"{color_1}Obrigado e volte sempre!{color_reset}")
        break

    
