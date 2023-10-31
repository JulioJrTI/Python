pessoa={} #Dicionario
galera=[] #Lista

soma=0 #Iremos somar todos os valores de idade digitadas pelo input
media=0 #Iremos armazenar o valor de media nesta variavel

while True:    
    pessoa.clear()
    pessoa["Nome"]=str(input("Digite seu nome: "))

    while True: #Sistema de erro
        pessoa["Sexo"]=str(input("Digite seu sexo [M/F]: ")).upper()[0] 
        if pessoa["Sexo"] in "MF":
            break
        print("Erro! Por favor digite apenar M ou F.")
    
    pessoa["Idade"]=int(input("Digite sua idade: "))
    soma+=pessoa["Idade"] #Iremos efetuar a soma, com os valores inseridos no input de idade

    galera.append(pessoa.copy()) #Iremos os dados inseridos no dicionario para com uma lista   
    
    while True: #Sistema de erro
        c=str(input("Deseja continuar? [S/N]")).upper()[0]    
        if c in "SN":
            break
        print("ERRO! Por favor digite S ou N.")
    if c=="N":
        break   

media=soma/len(galera) #A Media será os valores de idade somados na variavel soma dividido pela quantidade de pessoas cadastradas

print("-="*10)
print(f"Foram cadastradas {len(pessoa)} pessoas.") #Quantidade de pessoas cadastradas
print(f"A media de idade das pessoas cadastradas é {media:5.2f} anos.") #A media de idade das pessoas cadastradas
print(f"As mulheres cadastradas foram: ",end="")
for p in galera: #Iremos saber os nomes das mulheres cadastradas
    if p['Sexo'] in 'Ff':
        print(f"{p['Nome']}, ",end="")
print()
print(f"Lista das pessoas que estão acima da media: ")
for p in galera: #Iremos saber as pessoas com idades acima da media
    if p['Idade'] >=media:
        print("   ",end="")
        for k, v in p.items():
            print(f"{k}={v}; ",end="")
        print()
print("<<< Encerrado >>>")