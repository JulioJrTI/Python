#Importando funções de formatação e cores
from Modulos.Formatar import cabecalho,cor
from time import sleep

#Limpando o terminal cada execução do programa
from os import system
system("cls")

#Dicionario contendo os dados de uma pessoa
cadastroPessoas={"Nome do cliente":[],"Quantidade de dias alugados":[],"Quantidade de KMs percorridos":[],"Valor total a pagar":[]}

#Carregando informações se existir
try:
    with open('dados_locacao.txt','r') as arquivo:
        linhas = arquivo.readlines();
        
    #Processando e formatando o dicionario
    for linha in linhas:
        chave, valor = linha.strip().split(': ')
        valor = valor.strip('[]').split(', ' )
        cadastroPessoas[chave] = valor
except FileNotFoundError:
    print("Arquivo de dado não encontrado. Será criado um novo!")

#Greetings!
cabecalho(cor("Bem vindo ao programa de locação de carros da Alexa!",35))

#Programa principal
while True:    
    #Menu principal    
    c=int(input("[1] Cadastrar cliente"
                "\n[2] Verificar cliente cadastrado"
                "\n[3] Sair do programa"
                "\nDigite sua escolha: "))        
        
    #Cadastrando novos clientes
    if c==1:
        #Tratamento de erro
        while True:
            nomePessoa=str(input("Digite o nome do cliente: "))
            
            if nomePessoa.isalpha():
                cadastroPessoas["Nome do cliente"].append(nomePessoa)
                break
            else:
                print("Erro! Valor invalido! Digite o nome de uma pessoa corretamente (Exemplo: Alexa)")

        #Tratamento de erros
        while True:
            try:
                #Solicitando ao usuario que insira a quantidade de dias alugados
                quantDias=int(input("Digite a quantidade de dias alugados: "))
                cadastroPessoas["Quantidade de dias alugados"].append(quantDias)
                break
            except ValueError:
                print(cor("Erro! Por favor digite um valor numerico valido!",31))            

        #Calculando o valor a pagar pela quantidade de dias alugados 
        diasPagar=(quantDias*60)
        print(f"Total de dias alugados: {quantDias} dias")
        print(f"Valor a pagar: R${diasPagar:.2f}")

        #Tratamento de erros
        while True:
            try:
                #Solicitando ao usuario que insira a quantidade de KMs percorridos
                quantsKm=float(input("\nDigite a quantidade de KMs percorridos: "))
                cadastroPessoas["Quantidade de KMs percorridos"].append(quantsKm)
                break
            except ValueError:
                print(cor("Erro! Por favor digite um valor numerico valido!",31))
            

        #Calculando o valor a pagar pela quantidade de KMs percorridos
        kmsPagar=(quantsKm*0.15)
        print(f"Total de KMs percorridos: {quantsKm}")
        print(f"Valor a pagar: R${kmsPagar:.2f}")

        #Calculando total a pagar e imprimindo o resultado
        print("\nCalculando valor total...")
        sleep(1)
        totalPagar=(diasPagar+kmsPagar)
        cadastroPessoas["Valor total a pagar"].append(totalPagar)
        cabecalho(cor(f"Total a pagar: R${totalPagar:.2f}",34),cent=0,quantC=25)
        
        #Salvando informações
        with open('dados_locacao.txt','w') as arquivo:
            for chave,valor in cadastroPessoas.items():
                arquivo.write(f"{chave}: {valor}\n")
        
    elif c==2:
        print("Lista de clientes cadastrados:")
        for i, n in enumerate(cadastroPessoas["Nome do cliente"]):
            print(f"{i}: {n}")
    
    #Saindo do programa
    elif c==3:
        print("Obrigado e volte sempre!")
        break