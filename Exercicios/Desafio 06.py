"""Desafio 06: Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada."""

from Modulos.Formatar import cor,cabecalho
from Modulos.Matematica import dobro,triplo,raizQuadrada

#Limpando o terminal a cada execução do programa
import os
os.system("cls")

#Chave para controlarmos o input do primeiro e de novos numeros
chave=True

#Programa principal
cabecalho(cor("Bem vindo a aula de matematica da Prof(a) Alexa!",35))
while True:
    if chave: #Se a chave de controle for True, poderemos inserir um novo numero para verificação
        while True: #Tratamento de erros       
            try:
                num=int(input(cor("Digite um numero: ")))
                chave=False
                break
            except KeyboardInterrupt: #Caso o usuario tenha cancelado o programa (CTRL+C)
                print(cor("Usuario cancelou a execução do programa!",31))
                quit()
            except ValueError: #Caso o usuario tenha digitado letras
                print(cor("Erro! Digite somente numeros!",31))
    
    #Menu de escolha
    while True: #Tratamento de erros
        try:
            c=int((input(f"[1] Verificar o dobro do numero {cor(num)}\n"
                        f"[2] Verificar o triplo do numero {cor(num)}\n"
                        f"[3] Verificar a raiz quadrada do numero {cor(num)}\n"
                        "[4] Verificar outro numero\n"
                        "[5] Sair do programa\n"
                        "Escolha: ")))
            if c in [1,2,3,4,5]: #Se o usuario escolher uma das opções acima, o programa irá continuar
                break
            else: #Caso seja inserido qualquer valor acima de 5, iremos exibir um erro
                print(cor("Erro! Digite somente as escolhas abaixo! 1-5",31))                
        except ValueError: #Caso seja inserido qualquer valor alem de numeros
            print(cor("Erro! Digite numeros!",31)) 
    
    #Respostas das escolhas
    if c == 1: #Dobro        
        numDobro=dobro(num) #Armazenando resultado de uma função (dobro) em uma variavel       
        cabecalho(f"O dobro do numero {cor(num)} é {cor(numDobro)}.")
    elif c == 2: #Triplo
        numTriplo=triplo(num) #Armazenando resultado de uma função (triplo) em uma variavel
        cabecalho(f"O triplo do numero {cor(num)} é {cor(numTriplo)}.")
    elif c == 3: #Raiz Quadrada
        numRaizQuadrada=raizQuadrada(num) #Armazenando resultado de uma função (raiz quadrada) em uma variavel
        cabecalho(f"A raiz quadrada do numero {cor(num)} é {cor(numRaizQuadrada)}.")
    elif c == 4: #Verificar novo numero
        chave=True 
    elif c == 5: #Sair do programa
        print(cor("Obrigado e volte sempre!",35))
        break 
    
           