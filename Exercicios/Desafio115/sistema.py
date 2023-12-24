from Desafio115.lib.interface import *
from Desafio115.lib.arquivo import *
from time import sleep

arq = "CursoEmVideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
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

