#Função que irá colorizar um texto
def cor(texto,num=32):
    """
    \033[1;33m
    Bem vindo ao colorizador da Alexa!
    Para usarmos essa função, siga o exemplo de um codigo:
    
    "print(cor("A Alexa soltou um pum! Ew!")31)"
    
    No codigo acima, chamamos a função e como metodos usamos uma frase 
    e a direita selecionamos a cor, neste caso 32=vermelho
    
    Não se preocupe enquando a resetar a cor, tudo que estive fora da 
    frase escrita na função não será colorido.
    
    A cor padrão é 32 (Verde).
    
    Opções de Cores:
    31: Vermelho
    32: Verde
    33: Amarelo
    34: Azul
    35: Magenta
    36: Ciano
    37: Branco
    
    \033[m
    """   
    return f"\033[1;{num}m{texto}\033[m" 


#Função que irá adicionar linhas
def linhas(quant=30):
    """
    Para imprimir caracteres, insira o mesmo deseja como o primeiro modulo e em seguinda digite a quantidade de caracteres que iremos imprimir.
    
    O caracteres padrão é "*".
    A quantidade padrão é 30.
    
    """    
    return "*" *quant

#Função que irá centralizar um texto e inserir caracteres cosmeticos acima e abaixo do mesmo
def cabecalho(texto,c="*",quantC=60,cent=65):
    """
    Para centralizar um texto usando esta função, não será preciso usar o 'print()'!
    
    1º Parametro: O Texto a ser centralizado.
    2º Parametro: Caractere especial a ser posicionado acima e abaixo do texto (padrão = '*')
    3º Parametro: A quantidade de caracteres especiais a ser posicionado (padrão = 60)
    4º Parametro: Em quanto o texto será centralizado (padrão = 65)
    
    """
    
    resultado = f"{c*quantC}\n {texto.center(cent, ' ')} \n{c*quantC}"    
    print(resultado)

#Função que irá exibir os tipos primitivos de um valor inserido como parametro
def tipoPrimitivo(v):
    cabecalho(cor(f"Tipo primitivo da palavra '{v}'"),58)
    
    #Se o valor inserido como parametro for um numero, a variavel que este valor está armazenada será uma variavel int
    if v.isnumeric():
        tipo=int(v)
    
    #Se o valor inserido como parametro for uma string, a variavel que este valor está armazenada será uma variavel str
    elif v.isalpha():
        tipo=str(v)
        
    #Se o valor inserido com parametro for somente espaços, iremos considera-lo como str
    elif v.isspace():
        tipo=str(v)
        
    print(cor(f"Tipo: {type(tipo)}",36)) #Tipo primitivo
    print(cor(f"Contem somente espaços em branco: {v.isspace()}",31)) #Somente espaços?
    print(cor(f"É um valor numerico: {v.isnumeric()}",32)) #Valor numerico?
    print(cor(f"São palavras: {v.isalpha()}",33)) #String?
    print(cor(f"SOMENTE MAIUSCULO: {v.isupper()}",34)) #SOMENTE MAIUSCULO?
    print(cor(f"somente minusculo: {v.islower()}",35)) #somente minusculo?
    print(cor(f"Primeira letra é maiusculo: {v.istitle()}",36)) #Primeira letra maiusculo?
    print(cor(f"Contem letras e/ou numeros: {v.isalnum()}",37)) #Contem letras e ou numeros?
    print()
    
