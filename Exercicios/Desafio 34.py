"""Desafio 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

color1="\033[1;32m"
color2="\033[1;33m"
colorEnd="\033[m"

colaboradores=[]
print(f"{color1}Bem vindo ao calculador de salarios da Alexa!{colorEnd}")
while True:
    colaborador={}
    colaborador["Colaborador"]=str(input("Digite o nome do colaborador: "))
    colaborador["Salario"]=float(input("Digite o salario do colaborador: R$"))    

    if colaborador["Salario"]>1250:        
        aumento=10
        colaborador["Novo Salario"]=colaborador["Salario"]+(colaborador["Salario"]*aumento/100)
    elif colaborador["Salario"]<=1250:        
        aumento=15
        colaborador["Novo Salario"]=colaborador["Salario"]+(colaborador["Salario"]*aumento/100)

    colaboradores.append(colaborador)    
    
    c=str(input("Deseja continuar? [S/N]"))

    if c in "Nn":        
        break
print()
print("Segue lista de colaboradores e seus salarios: ")
for colaborador in colaboradores:
    print(f"Nome: {colaborador['Colaborador']}")
    print(f"Salario: {color1}R${colaborador['Salario']:.2f}{colorEnd}")    
    print(f"Novo salario: {color2}R${colaborador['Novo Salario']:.2f}{colorEnd}")
    print("-="*5)



