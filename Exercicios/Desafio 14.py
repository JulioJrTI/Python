"""Desafio 14: Escreva um programa que converta uma temperatura digita em ºC e converta para ºF."""

color1 = "\033[1;32m"
color2 = "\033[1;33m"
color3 = "\033[1;34m"
colorEnd = "\033[m"

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
diasTempC = []
diasTempF = []
print ( f"{color3}Bem vindo ao Clima Tempo da Alexa!{colorEnd}" )
for dia in dias :  # Iremos exibir o dia na ordem seguindo a lista de dias
    print ( f"{color1}Digite a temperatura para {dia}{colorEnd}" )
    tempC = int ( input ( "Digite a temperatura em Cº: " ) )
    diasTempC.append ( tempC )
    tempF = (tempC * 9 / 5) + 32
    diasTempF.append ( tempF )
    print ( f"{tempC}ºC foi convertido para {tempF}ºF" )
    print ( "=-" * 30 )
for dia, tempC, tempF in zip ( dias, diasTempC,
                               diasTempF ) :  # Iremos exibir o dia, a temperatura em C e F na ordem usando o comando zip
    print (
        f"Na {color1}{dia}{colorEnd} teremos {color2}{tempC}ºC{colorEnd} ou {color3}{tempF}ºF{colorEnd} de temperatura." )
