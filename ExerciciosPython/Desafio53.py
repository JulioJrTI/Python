"""Desafio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços."""

# Usando de Modulos para a formatação do programa
from Modulos.formatar import cabecalho,cor,limpar_terminal

# Limpando o terminal a cada execução do programa
limpar_terminal()

# Usando JSON para o carregamento a armazenamento de informações
import json

# Carregando ou criando novo arquivo JSON
try:
    with open('dados_ex53.json', 'r') as arquivo:
        palindromo = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado, criando um novo!")
    # Lista contendo palindromos digitados
    palindromo = []

# Greetings!
cabecalho(cor("Bem vindo ao analizador de palindromos da Prof(a) Alexa!",35))

# Programa principal
while True:
    # Solicitando uma palavra ou frase ao usuario
    frase=str(input("Digite uma frase ou palavra: "))
    
    # Removendo espaços e substituindo todas as letras por letras minusculas
    frase_formatada = frase.lower().replace(" ","")

    # Armazenando a frase/palavra digitada acima em uma variavel que irá inverter o sentido armazenado
    frase_inv = frase_formatada[::-1]

    # Verificando se a frase/palavra digitamente inicialmente tem o mesmo significado ao contrario
    if frase_formatada==frase_inv:
        print(cor(f"\nA frase ou palavra digitada é um palindromo!\n",32))        
        if frase not in palindromo:        
            palindromo.append(frase)
            
            # Salvado palavras/frases no arquivo JSON
            with open('dados_ex53.json','w') as arquivo:
                json.dump(palindromo,arquivo) 
                   
    else:
        print(cor(f"\nA frase ou palavra digitada não é um palindromo!\n",31))
        
    # Continuar ou não o programa
    c = str(input("Deseja continuar? [S/N]")).upper()
    
    # Saindo do programa
    if c in "Nn":        
        break

# Imprimindo lista completa de palindromos digitados
print(cor("\nSegue lista de palindromos digitados:",34))
for i, v in enumerate(palindromo):
    print(f"{i+1}: {v}")
print(cor("\nOBRIGADO E VOLTE SEMPRE!",35))