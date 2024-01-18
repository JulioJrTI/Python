"""Desafio 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

#Funções de formatação
from Modulos.Formatar import cor,cabecalho

#Função cosmetica
from time import sleep

#Iremos limpar o terminal a cada execução do programa
from os import system
system("cls")

#Função contendo o catalogo do dicionario abaixo
def exibir_produtos(produtos):    
    cabecalho(cor("Bem vindo a loja de eletronicos da Alexa!",35))
    sleep(2)
    print("Segue lista de produtos cadastrados:")
    sleep(1)
    for index, nome_produto in enumerate(produtos["Nome"]):
        preco_produto = produtos['Preço'][index]
        print(f"Id: {index} | Nome: {nome_produto}".ljust(40),end=" | ")
        print(f"Preço: R${preco_produto:.2f}")
        
#Chave de controle para que a função acima não seja chamada fora do controle
chave=True

#Dicionario contendo nome e preço de produtos de uma loja de eletronicos
produtos={"Nome":["PS5","Xbox Series X","TV OLED LG","Gamepad Dualsense Edge","Teclado Corsair RGB"],
            "Preço":[5000.00,3000.00,6500.00,1100.00,350.00]}

#Programa principal
while True:

    #Caso a chave seja True, iremos exibir o catalogo de produtos
    if chave:    
        exibir_produtos(produtos)
        chave=False    
        
    print()
    
    #Tratamento de erros
    while True:
        try:
            #Menu de escolhas
            sleep(1)
            c = int(input("[1] Adicionar desconto a algum produto\n"
                        "[2] Adicionar aumento a algum produto\n"
                        "[3] Alterar o preço de algum produto\n"
                        "[4] Adicionar novo produto a lista\n"
                        "[5] Sair do programa\n"
                        "Digite a escolha: "))
            if c in [1,2,3,4,5]:
                break
            else:
                system("cls")
                print(cor("Erro! Por favor insira um valor de escolha de 1 a 5!",31))
        except ValueError:
            system("cls")
            print(cor("Erro! Por favor insira um valor de escolha de 1 a 5!",31))

    #Desconto de preços
    if c == 1:
        #Limpando o terminal
        system("cls")
        
        #Exibindo catalogo de produtos
        exibir_produtos(produtos)
        
        #Tratamento de erro
        while True:
            try:
                #Escolhendo o produto pela index do dicionario
                produtoId=int(input("\nSeguindo a tabela acima, qual produto deseja adicionar desconto?\n"
                            "Digite a ID do produto: "))
                
                #Armazenando nome e preço original do produto escolhido em variaveis
                nomeProduto = produtos["Nome"][produtoId]
                precoOriginal = produtos["Preço"][produtoId]
                break
            except IndexError:
                print(cor("Erro! Escolha o Id correspondente ao produto que deseja tratar!",31))
        
        #Mostrando ao usuario o produto escolhido pelo Id digitado acima
        print("\nProduto Escolhido:")
        print(f"Nome do produto: {nomeProduto}")
        print(f"Preço do produto: {precoOriginal:.2f}")
        
        #Tratamento de erro
        while True:
            try:
                #Perguntando ao usuario qual será o % de desconto
                desconto = int(input("\nQuanto será o desconto: "))
                break
            except ValueError:
                print(cor("Erro! Por favor digite um valor de desconto corretamente! (Exemplo: 5 para 5 por cento de desconto)",31))
        
        #Calculando o desconto e armazenando em uma variavel
        precoNovo = precoOriginal-(precoOriginal*desconto/100)
        
        #Imprimindo preço antigo, nome do produto e novo preço
        cabecalho(f"Com {desconto}% de desconto, o produto '{nomeProduto}' que antes custava R${precoOriginal:.2f}, agora irá custar R${precoNovo:.2f}!",quantC=100)
        
    #Aumento de preços
    if c == 2:
        system("cls")
        exibir_produtos(produtos)
        
        #Tratamento de erro
        while True:
            try:
                #Escolhendo o produto pela index do dicionario
                produtoId=int(input("\nSeguindo a tabela acima, qual produto deseja adicionar aumento?\n"
                        "Digite a ID do produto: "))
        
                #Armazenando nome e preço original do produto escolhido em variaveis
                nomeProduto = produtos["Nome"][produtoId]
                precoOriginal = produtos["Preço"][produtoId]
                break
            except IndexError:                
                print(cor("Erro! Escolha o Id correspondente ao produto que deseja tratar!",31))
                
        #Mostrando ao usuario o produto escolhido pelo Id digitado acima
        print("\nProduto Escolhido:")
        print(f"Nome do produto: {nomeProduto}")
        print(f"Preço do produto: {precoOriginal:.2f}")
        
        #Tratamento de erro
        while True:
            try:
                aumento = int(input("\nQuanto será o aumento: "))
                break
            except ValueError:
                print(cor("Erro! Por favor digite um valor de aumento corretamente! (Exemplo: 5 para 5 por cento de aumento)",31))
        
        precoNovo = precoOriginal+(precoOriginal*aumento/100)
        cabecalho(f"Com {aumento}% de aumento, o produto '{nomeProduto}' que antes custava R${precoOriginal:.2f}, agora irá custar R${precoNovo:.2f}!",quantC=100)
        
    #Alteração de preço de produtos
    if c == 3:
        system("cls")
        exibir_produtos(produtos)
        
        #Tratamento de erro
        while True:
            try:
                #Escolhendo o produto pela index do dicionario
                produtoId=int(input("\nSeguindo a tabela acima, qual produto deseja alterar o preço?\n"
                                "Digite a ID do produto: "))
                
                #Armazenando nome e preço original do produto escolhido em variaveis
                nomeProduto = produtos["Nome"][produtoId]
                precoOriginal = produtos["Preço"][produtoId]
                break
            except IndexError:
                print(cor("Erro! Escolha o Id correspondente ao produto que deseja tratar!",31))         
        
        #Tratamento de erro
        while True:
            try:
                precoAlterado = float(input("Digite o novo preço: R$"))
                break
            except ValueError:
                print(cor("Erro! Por favor digite um valor monetario valido! (Exemplo: 123.00)",31))
        
        #Iremos trocar o valor de um item na lista por um valor digitado pelo usuario acima
        produtos["Preço"][produtoId] = precoAlterado
        
        #Imprimindo a alteração
        cabecalho(f"O produto '{nomeProduto}' que tinha seu preço original 'R${precoOriginal:.2f}', foi alterado para R${precoAlterado:.2f}",quantC=100)
        
    #Cadastrado de novos produtos
    if c == 4:
        while True:
            nome=str(input("Digite o nome do produto: "))
            
            #Tratamento de erro
            while True:
                try:
                    preco=float(input("Digite o preço do produto: R$"))
                    break
                except ValueError:
                    print(cor("Erro! Por favor digite um valor monetario valido! (Exemplo: 123.00)",31))
            
            #Adicionando nome e valor as listas do dicionario
            produtos["Nome"].append(nome)
            produtos["Preço"].append(preco)            
            print(cor("Produto adicionado ao catalogo com sucesso!",35))
            sleep(2)
            
            #Tratamento de erro
            while True:                
                #Escolha para o usuario se o mesma desejar continuar cadastrando novos produtos
                c=str(input("Continuar cadastrando? [S/N]")).upper()[0]                
                if c in ["S","N"]:
                    break
                else:
                    print(cor("Erro! Digite S ou N",31))            
            if c in "Nn":
                break
        
        system("cls")
        exibir_produtos(produtos) 
        
    #Sair do programa
    if c == 5:
        print(cor("\nObrigado e volte sempre!",35))
        break