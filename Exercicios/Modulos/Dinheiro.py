#Função que irá converter um valor em Reais para Dolares
def conversaoDolar(valorReais=0, cota=4.93):
    converterDolar = (valorReais / cota)
    return converterDolar

#Função que irá converter um valor em Dolares para Reais
def conversaoReais(valorDolar=0, cota=4.93):
    converterReais = (valorDolar * cota)
    return converterReais
    