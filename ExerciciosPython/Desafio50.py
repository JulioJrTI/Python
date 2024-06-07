"""Desafio 50: Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o."""

# Usando de modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Greetings
cabecalho(cor("Bem vindo ao somador de numeros pares da Prof(a) Alexa!",35))

# Lista contendo somente numeros pares
numeros_Pares=[]

# Solicitando 6 numeros inteiros
for n in range(6):
    
    while True:
        try:    
            num = int(input(f"Digite o {n+1}º numero: "))
            break
        except ValueError:
            print(cor("ERRO! DIGITE SOMENTE VALORES NUMERICOS!\n",31)) 
    
    # Se o valor inserido acima for um numero par iremos adicionar a lista, 
    # caso contrario será desconsiderado, o mesmo vale se digitarmos um numero repetido
    if (num%2==0 and num!=0) and num not in numeros_Pares:
        numeros_Pares.append(num)    

# Somando numeros pares inseridos na lista
soma=sum(numeros_Pares)

# Organizando os numeros da lista em ordem crescente
numeros_Pares.sort()

# Imprimindo numeros pares digitados e a soma dos mesmos
if len(numeros_Pares) > 0:    
    print(cor("\nNumeros pares e sua soma:",33))       
    print(" > ".join(map(str,numeros_Pares)) + f" = {soma}")
else:
    print(cor("Não foram digitados numeros pares!",35))
print()