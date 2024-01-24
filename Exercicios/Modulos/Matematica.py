import math
from Modulos.Formatar import cabecalho,cor
from tabulate import tabulate

#Função que irá somar dois numeros e imprimir o resultado final
def somarNumeros(n1=0,n2=0):
    """
    \033[1;32m
    
    Iremos somar dois numeros int inseridos como parametros.
    Os valores padrões são 0 para os dois parametros.
    
    \033[m
        
    """    
    soma = (n1+n2)
    print(f"A soma entre os numeros {n1} e {n2} é igual a {soma}.")

def dobro(n=0):
    """
    Função que irá retornar o dobro de um numero (inserido como parametro)
    Por padrão o parametro é 0.
    
    """  
    dobro=n*2
    return dobro

def triplo(n=0):
    """
    Função que irá retornar o triplo de um numero (inserido como parametro)
    Por padrão o parametro é 0.
    
    """
    triplo=n*3
    return triplo

def raizQuadrada(n=0):
    """
    Função que irá retornar a raiz quadrada de um numero (inserido como parametro)
    Por padrão o parametro é 0.
    
    """
    raizQuadrada=math.sqrt(n)
    return raizQuadrada
    
def mediaNumeros(n1,n2):
    media=(n1+n2)/2
    return media

def conversaoMetros(metros=0):
        pCentimetros=metros*100
        pMilimetros=metros*1000
        cabecalho(f"{metros}(m) é igual a {pCentimetros}(cm) e {pMilimetros}(mm).","-",50,0)
        
def tabuada(num=0):
    tabela = []
    for n in range(1, 11):
        t = num * n
        tabela.append([num, "x", n, "=", t])

    headers = ["Número", "", "Multiplicador", "", "Resultado"]
    print(tabulate(tabela, headers=headers, tablefmt="pretty"))
    
#Função de aumento de valor
def aumento(valor=0,aumento=0):
    """
    Essa função irá retornar um novo valor que será calculado junto a um percentual anexado com o parametro!
    1º parametro (valor) = Valor que irá ser calculado, padrão = 0
    2º parametro (aumento) = Percentual de aumento, padrão = 0
    
    """
    
    aumentoValor=(valor+(valor*aumento/100))
    return aumentoValor