#Função que irá colorizar um texto
def cor(texto,num=32):
    """
    Bem vindo ao colorizador da Alexa!
    Para usarmos essa função, siga o exemplo de um codigo:
    
    "print(cor("A Alexa soltou um pum! Ew!")31)"
    
    No codigo acima, chamamos a função e como metodos usamos uma frase 
    e a direita selecionamos a cor, neste caso 32=vermelho
    
    Não se preocupe enquando a resetar a cor, tudo que estive fora da 
    frase escrita na função não será colorido.
    
    A cor padrão é 32 (Verde).
    
    """   
    return f"\033[1;{num}m{texto}\033[m" 


#Função que irá adicionar linhas
def linhas(quant=30):
    return "-"*quant


#Função que irá centralizar um texto e inserir linhas acima e abaixo do mesmo
def cabecalho(texto,center=55):
    resultado = f"{linhas(len(texto))}\n{texto.center(center)}\n{linhas(len(texto))}"    
    return resultado
