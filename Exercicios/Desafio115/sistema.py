from Desafio115.lib.interface import *
from time import sleep

while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar nova pessoa","Sair do Sistema"])
    if resposta==1:
        cabecalho("Opção 1")
    elif resposta==2:
        cabecalho("Opção 2")
    elif resposta==3:
        cabecalho("Opção 3")
        cabecalho("Saindo do sistema...")
        break
    else:
        print("Erro! Digite uma opção valida!")
    sleep(2)
