def leiaDinheiro(msg):
    #Chave de controle para o loop abaixo
    valido = False

    #Enquanto a chave de controle acima NÃO for True
    while not valido:
        #Variavel input, iremos eliminar espaços em branco e substituir virgulas por pontos, para que não haja problemas
        entrada = str(input(msg)).replace(",",".").strip()
        
        #Caso o valor inserido em input for palavras ou esteja vazio, iremos acionar um erro
        if entrada.isalpha() or entrada == '':
            print(f"Erro: '{entrada}' é um preço invalido!")
        
        #Caso contrario, o valor inserido será aceito e iremos retornar o mesmo agora convertido para float
        else:
            valido = True
            return float(entrada)
