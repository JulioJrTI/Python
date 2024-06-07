"""Desafio 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

from Modulos.Formatar import cor,cabecalho
from Modulos.Matematica import aumento

#Limpando o terminal a cada execução do programa
from os import system
system("cls")

#Greetings!
cabecalho(cor("Bem vindo ao calculador de salarios da diretora Alexa!",35),cent=68)

#Tratamento de erro
while True:
    try:
        #Solicitando o nome do funcionario
        nomeFuncionario=str(input("Qual é o nome do(a) funcionario(a): "))
        if nomeFuncionario.isalpha():
            break
        else:
            print(cor("ERRO! Por favor digite o nome do funcionario!",31))
    except KeyboardInterrupt:
        print(cor("\nUsuario encerrou o programa",31))
        quit()
    
#Tratamento de erro
while True:
    try:
        #Solicitando o salario atual do funcionario
        salarioAtual=float(input("Digite o salario atual do funcionario: R$"))
        break
    except ValueError:
        print(cor("Erro! Por favor digite um valor monetario valido para o salario (Exemplo 1500.00), lembre-se de usar ponto como separador!",31))
    except KeyboardInterrupt:
        print(cor("\nUsuario encerrou o programa",31))
        quit()

#O valor abaixo será o % de aumento, ou seja, em quantos % iremos aumentar o salario do funcionario
aumentoPercent=15

#Usando função para calcularmos o novo salario
novoSalario = aumento(salarioAtual,aumentoPercent)

#Imprimindo resultado
cabecalho(cor(f"O salario do funcionario {nomeFuncionario} que antes era R${salarioAtual:.2f}, agora com 15% de aumento irá ficar R${novoSalario:.2f}",35),cent=0,quantC=100)

