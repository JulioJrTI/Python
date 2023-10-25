"""Desafio 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

-Abaixo de 18.5: Abaixo do Peso

-Entre 18.5 e 25: Peso Ideal

-25 até 30: Sobrepeso

-30 até 40: Obesidade

-Acima de 40: Obesidade mórbida"""

enfeite="-="*10
pessoas={"Nome":[],"Peso":[],"Altura":[],"IMC":[],"Ranking":[]}

while True:
    nome=str(input("Digite seu nome: "))
    pessoas["Nome"].append(nome)
    
    peso=float(input("Digite seu peso: "))
    pessoas["Peso"].append(peso)

    altura=float(input("Digite sua altura: "))
    pessoas["Altura"].append(altura)

    imc=peso/(altura**2)
    pessoas["IMC"].append(imc)    

    if imc <18.5:
        ranking="Abaixo do peso"        
    elif imc >=18.5 and imc <=25:
        ranking="Peso ideal"        
    elif imc >25 and imc <=30:
        ranking="Sobrepeso"        
    elif imc >30 and imc <=40:
        ranking="Obesidade"        
    else:
        ranking="Obesidade morbida"
    print(ranking) 
    pessoas["Ranking"].append(ranking)  

    c=str(input("Deseja continuar? [S/N]"))
    if c in "Nn":
        break

print()
print("Segue lista de pessoas cadastradas:")
for i in range(len(pessoas["Nome"])):
    print(enfeite)
    print(f"Nome: {pessoas['Nome'][i]}")
    print(f"Peso: {pessoas['Peso'][i]}")
    print(f"Altura: {pessoas['Altura'][i]}")
    print(f"IMC: {pessoas['IMC'][i]:.2f}")
    print(f"Ranking: {pessoas['Ranking'][i]}")
    print(enfeite)