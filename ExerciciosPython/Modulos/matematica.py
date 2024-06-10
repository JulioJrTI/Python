import math
from Modulos.formatar import cabecalho,cor
from tabulate import tabulate
from time import sleep

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

#Função que irá converter uma temperadura ºC para ºF
def conversaoF(tempC=0):
    """
    Função simples que irá converter uma temperadura ºC para ºF
    Como parametro, iremos inserir um valor de temperatura ºC (padrão = 0)
    
    """
    
    convF=(tempC*9/5+32)
    return convF

#Função que irá identificar se um novo é PAR ou IMPAR
def par_impar(num=0):
    """
    Função simples que irá retornar uma mensagem ao identificar se o valor inserido com parametro é PAR ou IMPAR
    Paramentro 'num' = valor integer, como padrão é 0.
    """
    
    if num%2==0:
        return "Par"
    else:
        return "Impar"
    
#Função que irá imprimir numeros pares usando parametros como pontos de inicio e final
def print_num_pares(n=0,f=0):
    """
    Calculando os numeros pares seguindo valores de inicio e fim (parametros)
    Parametros: n=(numero inicial), f=(numero final)
    
    """
    
    #Calculando os numeros pares e os imprimindo
    if f==0:
        print(cor("Erro! Insire um valor final no segundo parametro!",31))
    else:
        #Imprimindo os numeros pares
        print(cor(f"Numeros pares de {n} a {f}:",35).center(65))
        for num in range(n,f+1):
            if num%2==0:
                print(num,end=" > ")
        print("\b\b ")
        
#Criando uma função que irá somar e exibir numeros impares que são multiplos de 3
def somar_numerosImpares(i=0,f=0,m=3):
    
    """
    Iremos somar os numeros impares que são multiplos por 3
    Parametros: i=(Numero inicial),f=(Numeros final),m=(Multiplos, por padrão será multiplos de 3)
    
    """
    
    if f==0:
        print(cor("Erro! Digite um valor numerico final no segundo parametro!",31))
    else:
        #Variavel irá receber a soma de todos os numeros impares que são multiplos de tres
        somaNumeros=0

        print(cor(f"Numeros impares de {i} a {f} que são multiplos de {m} e seu resultado de soma: ",34,),end="")
        
        #Usando loop FOR para calcularmos os numeros impares multiplos de tres
        for num in range(i,f+1):
            if num%2==1 and num%m==0:
                print(num,end=" > ")
                somaNumeros+=num

        #Imprimindo resultado da soma        
        print(f"\b\b= {cor(somaNumeros)}") 
    
#Criando uma função que irá imprimir se o ano (inserido como parametro) é ou não bissexto
def ano_bissexto(ano=0): 
    """
    Função simples que irá calcular se o ano (parametro) é divisivel por 4, caso não seja, o ano não é bissexto, caso seja iremos efetuar uma nova verificação se o ano divisivel por 4 tbm é divisivel por 400 e NÃO é divisivel por 100, caso verdadeiro, o ano é bissexto, caso contrario não é bissexto.
    
    ano = ano (4 valores numericos integer)
    """
    
    if ano%4==0:
        if ano%100!=0 or ano%400==0:
            print(cor("\nO ano é bissexto",36))
        else:
            print(cor("\nO ano não é bissexto",31))
    else:
        print(cor("\nO ano não é bissexto",31))
        
#Função que irá converter um valor inserido como parametro para bi, octa e hex tbm inserido como parametro
def conversor_numero(num,base):
    """
    Função simples que irá converter um valor numerico (inserido como primeiro parametro) para a base escolhida (bi, oct, hex) no segundo parametro.
    
    num = Numero que será convertido
    conv = Base para a conversao: bin, oct, hex    
    """
    
    if base=='bin':
        return bin(num)[2:]
    elif base=='oct':
        return oct(num)[2:]
    elif base == 'hex':
        return hex(num)[:2]
    else:
        return None
    
#Criando uma função que irá comparar numeros de acordo com a quantidade inserida como parametro
def maior_menor(quant=2):
    """
    Função que irá comparar numeros (quantidade de numeros inserida como parametro) e no final irá dizer qual foi o maior e menor numero digitado
    
    quant = Quantidade de numeros a serem comparados    
    
    """    
    
    #Armazenando o maior e menor numero em variaveis
    maior=float('inf')
    menor=float('-inf')

    #Solicitando numeros (de acordo com o valor em parametro) ao usuario
    for n in range(quant):        
        #Tratamento de erros
        while True:
            try:
                num=int(input(f"Digite o {n+1}º numero: "))
                break
            except ValueError:
                print(cor("Erro! Digite somente valores numericos!",31))
            except KeyboardInterrupt:
                print("\nO usuario cancelou o programa...")
        
        #Efetuando a comparação dos numeros digitados acima
        if n==0:
            maior=num
            menor=num
        else:
            if num > maior:
                maior=num
            if num < menor:
                menor=num

    #Imprimindo os resultados
    if maior==menor:
        print(cor(f"\nNão existe valor maior, os {quant} numeros são iguais",35))
    else:
        print(cor(f"\nMaior: {maior}",31))
        print(cor(f"Menor: {menor}",34))        
        
#Função que irá calcular as retas de um triangulo e informar se podemos ou não formar um triangulo
def retas_triangulo(r1,r2,r3):
    """
    Iremos calcular se as retas inseridas como parametros podem ou não formar um triangulo
    Paramentros: r1,r2 e r3 (valores numericos float)
    
    """   
    
    #Calculando se as retas acima podem ou não formar um triangulo
    if (r1+r2) > r3 and (r2+r3) > r1 and (r3+r1) > r2:
        print(cor("\nPode formar um triangulo "),end="")
        return True        
    else:
        print(cor("\nNão pode formar um triangulo!",31))
        return False
    
#Função que irá conter um contador reverso
def contador_reverso(n1=0,n2=0,delay=0.5):
    
    """
    Contador reverso do segundo valor em parametro até o primeiro valor em parametro
    Parametros: n1 (valor final), n2 (valor inicial), delay (efeito de pausa entre os numeros)
    
    """    
    
    #Loop FOR para o contador reverso
    for i in range(n2,n1,-1):        
        print(i)        
        sleep(delay)
        
#Criando uma função que irá efetuar o calculo de PA
def calcular_pa(num=0, razao=0, quant=0):
    """
    Iremos calcular e imprimir a progressão aritimetica seguindo os parametros abaixo:
    num (Numero inicial), razao (De quanto em quanto iremos pular), quant (Quantidade de numeros a serem impressos) 
    
    """        

    if quant <=0:
        print(cor("Insira no 3º parametro a quantidade de numeros a serem impressos!",31))
    else:
        print(f"\nSegue {quant} termos de uma Progressão Aritmetica:")
        for n in range(quant):
            pa = num + n * razao
            print(f"{pa} > ",end="")
        print(cor("FIM"))       
        
#Função que irá identificar se um numero é ou não um numero PRIMO
def indetificar_numPrimo(num=0):
    """
    Função que irá identificar se um numero (parametro) é ou não um numero PRIMO
    
    """
    
    msg_true = cor(f"O numero {num} é um numero PRIMO!",34)
    msg_false = cor(f"O numero {num} não é um numero PRIMO!",31)
    
    if num < 2:
        return msg_false
    if num == 2:
        return msg_true
    if num%2==0:
        return msg_false

    raiz = int(math.sqrt(num))

    for i in range(3,raiz+1,2):
        if num%i==0:
            return msg_false
    
    return msg_true