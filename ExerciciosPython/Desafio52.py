"""Desafio 52: Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo."""

color1="\033[1;32m"
color2="\033[1;31m"
colorEnd="\033[m"

numeros={"Numeros divisiveis":[],"Numeros não divisiveis":[]} #Iremos armazenar os numeros divisiveis e não divisiveis em duas listas no dicionario

print(f"{color1}Bem vindo ao calculador de numeros primos da Alexa!{colorEnd}")
while True:
    div=0 #Iremos saber se um numero é primo se a quantidade de numeros divisiveis por ele for exatamente 2.
    while True: #Mecanica de erro, se qualquer valor alem de integer for digitado, iremos exibir uma mensagem de erro.
        try:
            numero=int(input("Digite um numero: "))
            break
        except:
            print(f"{color2}Erro! Digite um numero.{colorEnd}")        


    for n in range(1,numero+1): #Um loop FOR de 1 ao numero digitado pelo input+1
        if numero%n==0: #Se o input for um valor divisivel pelos numeros do loop
            print(f"{color1}{n}{colorEnd}",end=" > ")
            numeros["Numeros divisiveis"].append(n) #Iremos armazenar somente os numeros divisiveis
            div+=1 #E iremos aumentar em 1, todos os numeros que forem divisiveis
        else:
            print(f"{color2}{n}{colorEnd}",end=" > ") 
            numeros["Numeros não divisiveis"].append(n) #Iremos armazenar somente os numeros não divisiveis  
    print(f"{color1}Fim{colorEnd}")

    print("-="*10)
    if div==2:
        print(f"{color1}O numero {numero} é primo.{colorEnd}") #Se a quantidade de numeros divisiveis pelo input for exatamente 2.
    else:
        print(f"{color2}O numero {numero} não é primo.{colorEnd}") #Se a quantidade de numeros divisiveis for inferior ou superior a 2, então o numero em input não é primo.

    print("-="*10)
    print(f"{color1}Numeros divisiveis por {numero}: {numeros['Numeros divisiveis']}{colorEnd}") #Exibindo a lista de numeros divisiveis
    print(f"{color2}Numeros não divisiveis por {numero}: {numeros['Numeros não divisiveis']}{colorEnd}") #Exibindo a lista de numeros não divisiveis
    print("-="*10)

    while True: #Mecanica de erro, se qualquer valor alem de S ou N for digitado, iremos exibir uma mensagem de erro
        try:
            c=str(input("Deseja efetuar nova verificação? [S/N]")).upper()[0]
            break
        except:
            print("Erro! Escolha S ou N")
    if c in "S":
        div==0 #Limpando a quantidade de numeros divisiveis
        numeros["Numeros divisiveis"].clear() #Limpando as listas do dicionario
        numeros["Numeros não divisiveis"].clear() #Limpando as listas do dicionario
    if c in "N":
        print(f"{color1}Obrigado e volte sempre!{colorEnd}")
        break




