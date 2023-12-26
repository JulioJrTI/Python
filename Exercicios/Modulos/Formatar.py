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


#Função que irá centralizar um texto e inserir linhas acima e abaixo do mesmo
def cabecalho(texto,cent=0):
    resultado = f"{linhas(len(texto))}\n{texto.center(cent)}\n{linhas(len(texto))}"    
    return resultado
