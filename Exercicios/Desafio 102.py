"""Desafio 102: Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que será um valor logico (opcional) indicando se será mostrado ou não na tela o processo de calculo de fatorial, e tambem crie uma descrição para o help() da função."""

#Definindo a função com um parametro opcional que incialmente irá receber False
def fatorial(num,show=False):
    #Descrição para o help() da função
    """
    A função irá receber 2 Parametro, um será para o fatorial e outro será um valor boolean para que seja ou não mostrado o processo de calculo do fatorial:

    1º Parametro (num): Valor para o fatorial
    2º Parametro (show): Boolean, se True, irá mostrar o processo de multiplicação em ordem decrescente da fatorial, caso False irá mostrar somente o resultado final.    
    
    """

    #Função
    cont=num
    fatorial=1

    if show==True:
        print(f"{num}! = ",end="")

    while cont > 0:
        fatorial*=cont

        if show==True:
            if cont!=1:
                print(f"{cont} x",end=" ")
            else:
                print(f"{cont}",end=" = ")
        cont-=1
    print(fatorial)

#Chamando a função criada acima para o fatorial de 5 como o parametro em True
fatorial(5,show=True)

#Chamando o help da função acima
help(fatorial)