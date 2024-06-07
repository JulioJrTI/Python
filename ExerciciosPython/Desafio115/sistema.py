from Desafio115.lib.interface import * #O arquivo modular irá customizar a "interface"
from Desafio115.lib.arquivo import * #O arquivo modular irá contrar a logica de read e write de um arquivo txt
from time import sleep

#Nome do arquivo em texto que iremos armazenar nomes e idade de pessoas
arq = "CursoEmVideo.txt"

#Se o arquivo acima não existe, iremos chamar uma função que irá criar este arquivo
if not arquivoExiste(arq):
    criarArquivo(arq)

#Criando um menu que irá nos permitir exibir ou cadastrar pessoas
while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo atraves de uma função
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastrar uma pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho("Opção 3")
        cabecalho("Saindo do sistema...")
        break
    else:
        print("Erro! Digite uma opção valida!")
    sleep(2)

