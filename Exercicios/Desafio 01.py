"""Desafio 01: Crie um programa que escreva "Olá, Mundo!" na tela."""

garotas = ["Alexa", "Dakota", "Candice"]  # Lista inicial que com o passar da loop, pode acabar diminuindo de tamanho
agrados = []  # Iremos adicionar as garotas que receberam comprimentos nesta lista
print ( "Hello World!" )

while True :
    greeting = (
        input ( "Olá, temos algumas garotas na sala, como deseja comprimenta-las? [Bom Dia/Boa Tarde/Boa Noite] " ))
    garota = input ( "Qual garota irá recebe-lo primeiro?\n"
                     "Alexa\n"
                     "Dakota\n"
                     "Candice\n" )
    if "bom dia" in greeting.lower () and "alexa" in garota.lower () :  # Se dermos BOM DIA para a Alexa
        garotas[0] = "Bom Dia Alexa!"  # Iremos trocar o valor "Alexa" na lista por "Bom Dia Alexa!"
        agrados.append ( garotas[0] )  # Iremos adicionar a Alexa a lista de mulheres agradadas
        garotas.pop ( 0 )  # E iremos retirar ela da primeira lista
    elif "boa tarde" in greeting.lower () and "alexa" in garota.lower () :  # Se dermos BOA TARDE para a Alexa
        garotas[0] = "Boa Tarde Alexa!"  # Iremos trocar o valor "Alexa" na lista por "Boa tarde Alexa!"
        agrados.append ( garotas[0] )  # Iremos adicionar a Alexa a lista de mulheres agradadas
        garotas.pop ( 0 )  # E iremos retirar ela da primeira lista
    elif "boa noite" in greeting.lower () and "alexa" in garota.lower () :  # Se dermos BOA NOITE para a Alexa
        garotas[0] = "Boa Noite Alexa!"  # Iremos trocar o valor "Alexa" na lista por "Boa noite Alexa!"
        agrados.append ( garotas[0] )  # Iremos adicionar a Alexa a lista de mulheres agradadas
        garotas.pop ( 0 )  # E iremos retirar ela da primeira lista

    if "bom dia" in greeting.lower () and "dakota" in garota.lower () :
        garotas[1] = "Bom Dia Dakota!"
        agrados.append ( garotas[1] )
        garotas.pop ( 1 )
    elif "boa tarde" in greeting.lower () and "dakota" in garota.lower () :
        garotas[1] = "Boa Tarde Dakota!"
        agrados.append ( garotas[1] )
        garotas.pop ( 1 )
    elif "boa noite" in greeting.lower () and "dakota" in garota.lower () :
        garotas[1] = "Boa Noite Dakota!"
        agrados.append ( garotas[1] )
        garotas.pop ( 1 )

    if "bom dia" in greeting.lower () and "candice" in garota.lower () :
        garotas[2] = "Bom Dia Candice!"
        agrados.append ( garotas[2] )
        garotas.pop ( 2 )
    elif "boa tarde" in greeting.lower () and "candice" in garota.lower () :
        garotas[2] = "Boa Tarde Candice!"
        agrados.append ( garotas[2] )
        garotas.pop ( 2 )
    elif "boa noite" in greeting.lower () and "candice" in garota.lower () :
        garotas[2] = "Boa Noite Candice!"
        agrados.append ( garotas[2] )
        garotas.pop ( 2 )

    choice = input ( f"Deseja dar {greeting} a alguma outra garota? [S/N]" )

    print ( "*" * 50 )
    if choice in "Nn" :
        print ( f"Segue a lista de garotas que receberam um agrado: ", end="\n" )
        for garota_agradada in agrados :  # Iremos criar um pequeno loop para imprimirmos a lista de garotas
            print ( garota_agradada )
        print ( "*" * 50 )
        print ( "Segue a lista de garotas que não receberam um agrado: ", end="\n" )
        for garota_nao_agradada in garotas :  # Iremos criar um pequeno loop para imprimirmos a lista de garotas
            print ( garota_nao_agradada )
        break
print ( "*" * 50 )
