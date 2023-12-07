"""Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse modulo e use algumas dessas funções."""

"""Desafio 108: Adapte o código do Desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado."""

#Função que irá aumentar o valor digitado de acordo com a taxa
def aumentar(preco = 0,taxa = 0,f=True):
    res=preco+(preco*taxa/100)
    
    #Caso o parametro de formatação esteja como True, iremos retornar o resultado formatado
    if f:
        return moeda(res)
    else:
        return res
    
#Função que irá diminuir o valor digitado de acordo com a taxa
def diminuir(preco = 0,taxa = 0,f=True):
    res=preco-(preco*taxa/100)
    
    #Caso o parametro de formatação esteja como True, iremos retornar o resultado formatado
    if f:
        return moeda(res)
    else:    
        return res    

#Função que irá exibir o dobro do numero digitado
def dobro(preco = 0,f=True):
    res=preco*2
    
    #Caso o parametro de formatação esteja como True, iremos retornar o resultado formatado
    if f:
        return moeda(res)
    else:    
        return res    

#Função que irá exibir a metade de um numero digitado 
def metade(preco = 0,f=True):
    res=preco/2
    
    #Caso o parametro de formatação esteja como True, iremos retornar o resultado formatado
    if f:
        return moeda(res)
    else:    
        return res   

#Função que irá formatar o valor inserido para o formato de moeda
def moeda(preco = 0,moeda = "R$",f=True):    
    return f"{moeda}{preco:.2f}".replace(".",",")
