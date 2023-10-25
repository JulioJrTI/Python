"""Desafio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços."""

c1="\033[1;32m"
c2="\033[1;31m"
c3="\033[1;33m"
cE="\033[m"

frasesDict={"Frases digitadas":[],"Frases invertidas":[],"Resultado":[]} #Iremos armazenar a frase ou palavra digitada, sua versão reversa e seu resultado.

print(f"{c1}Bem vindo ao analisador de palindromo da Alexa!{cE}")
while True:     
    while True: #Mecanica de erro
        try:
            frase=str(input("Digite uma palavra ou frase: "))            
            break
        except:
            print(f"{c2}Erro, digite uma palavra ou frase!{cE}")
    
    frasesDict["Frases digitadas"].append(f'{c1}{frase}{cE}') #Armazenando a frase digitada no dicionario
    frasesDict["Frases invertidas"].append(f'{c3}{frase[::-1]}{cE}') #Armazenando sua versao reversa (com espaços e sem correcoes de formatacao) no dicionario
    
    fraseSemEspaco=frase.replace(" ","").upper() #Removendo os espacos e colocando todas as letras em maiu
    fraseInvertida=fraseSemEspaco[::-1] #Invertendo a frase em maiu e sem espaco

    if fraseSemEspaco==fraseInvertida: #Se a frase sem espacos e maiu for a mesma que invertida, a frase ou palavra é um palindromo
        print(f"{c1}A frase ou palavra '{frase}' é um palindromo.{cE}")
        frasesDict["Resultado"].append(f"{c1}Palindromo{cE}") #Armazendo o resultado no dicionario
    else:
        print(f"{c2}A frase ou palavra {cE}{c1}'{frase}'{cE} {c2}não é um palindromo.{cE}")
        frasesDict["Resultado"].append(f"{c2}Não é um palindromo{cE}") #Armazendo o resultado no dicionario

    while True: #Mecanica de erro
        try:
            c=str(input("Deseja continuar? [S/N]")).upper()[0]
            break
        except:
            print(f"{c2}Erro, escolha S ou N{cE}")
    if c in "N":        
        break

print("-="*10)
print("Segue frases digitadas:")
for i,v in enumerate(frasesDict["Frases digitadas"]): #Iremos exibir o index e valores das listas do dicionario na ordem em que foram digitadas
    print(f"{i+1}: {v} - {frasesDict['Frases invertidas'][i]} - {frasesDict['Resultado'][i]}")
print("-="*10)
print(f"{c1}Obrigado e volte sempre!{cE}")