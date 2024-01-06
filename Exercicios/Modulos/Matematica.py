import math

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
    