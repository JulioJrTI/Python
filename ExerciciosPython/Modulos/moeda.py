"""Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse modulo e use algumas dessas funções."""

"""Desafio 108: Adapte o código do Desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado."""

"""Desafio 109: Modifique as funções que foram criadas no Desafio 107 para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no Desafio 108"""

"""Desafio 110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""

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

#Função que irá chamar de todas as funções criadas até agora de forma resumida
def resumo(preco=0,taxaAumento=0,taxaReducao=0):
    print("-"*35)
    print("Resumo do valor".center(30))
    print("-"*35)

    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco,True)}")
    print(f"Metade do preço: \t{metade(preco,True)}")
    print(f"Com {taxaAumento}% de aumento: \t{aumentar(preco,taxaAumento,True)}")
    print(f"Com {taxaReducao}% de redução: \t{diminuir(preco,taxaReducao,True)}")

    print("-"*35)
    
    

    
