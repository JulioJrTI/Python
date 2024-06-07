" Modulo 'moeda.py' do pacote 'utilidadesCeV' "

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