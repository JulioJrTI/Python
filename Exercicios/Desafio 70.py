"""Desafio 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.

B) Quantos produtos custam mais de R$1000.

C) Qual é o nome do produto mais barato."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

produtos={"Nome do produto":[],"Preço do produto":[]}
produtosMilReais=[]
totalGasto=0

maiorPreco=0
maiorPrecoLista=[]

menorPreco=0
menorPrecoLista=[]

print(f"{c1}Bem vindo ao super-mercados Alexa Bliss!{c0}")
while True:
    while True:
        nomeProduto=str(input("Digite o nome do produto: "))
        if nomeProduto.isalpha():
            produtos["Nome do produto"].append(nomeProduto)
            break
        else:
            print(f"{c2}Erro! Digite somente palavras!{c0}")

    while True:
        try:
            precoProduto=float(input("Digite o preço do produto: R$"))
            produtos["Preço do produto"].append(precoProduto)
            totalGasto+=precoProduto
            break
        except:
            print(f"{c2}Erro! Digite somente numeros!{c0}")

    if maiorPreco==0 or precoProduto>maiorPreco:
        maiorPreco=precoProduto
        pMais=[nomeProduto,precoProduto]
        maiorPrecoLista.append(pMais)
    
    elif menorPreco==0 or precoProduto<menorPreco:
        menorPreco=precoProduto
        pMenos=[nomeProduto,precoProduto]
        menorPrecoLista.append(pMenos)
    
    if precoProduto>1000:
        produto=[nomeProduto,precoProduto]
        produtosMilReais.append(produto)
    
    while True:
        c=str(input("Deseja continuar cadastrando? [S/N]")).upper()[0]
        if c.isalpha() and c in ["S","N"]:
            break
        else:
            print(f"{c2}Erro! Digite somente S ou N!{c0}")

    if c in "Nn":
        break

print()
print(f"{c1}Lista de produtos:{c0}")
for i in range(len(produtos["Nome do produto"])):
    print(f"Nome do produto: {produtos['Nome do produto'][i]}")
    print(f"Preço do produto: R${produtos['Preço do produto'][i]}")
    print("~"*10)

print(f"{c1}Produtos custando mais que R$1000,00:{c0}")
for produto in produtosMilReais:
    nomeProduto,precoProduto=produto
    print(f"Nome: {nomeProduto}")
    print(f"Preço: {precoProduto}")
    print("~"*10)    

print(f"{c1}Produto mais barato: {c0}",end="")
for produto in menorPrecoLista:
    nomeProduto,precoProduto=produto
    print(f"Nome: {nomeProduto}, Preço: {precoProduto}")
    print(f"~"*10)    

print(f"{c1}Total gasto: R${totalGasto}{c0}")
print("~"*10)
print(f"{c1}Obrigado e volte sempre!{c0}")