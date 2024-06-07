from Desafio115.lib.interface import *

#Função que irá verificar se um arquivo existe ou não
def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#Função que irá criar um arquivo
def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

#Função que irá ler o conteudo de um arquivo e o modificar por dentro
def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

#Função que irá adicionar conteudo a um arquivo
def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()
