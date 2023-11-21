"""Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do Python, só que fazendo a validação para aceitar apenas um valor numero.

Ex: n=leiaInt('Digite um n')"""

#Cores
color1="\033[1;32m"
color2="\033[1;31m"
color0="\033[m"

#Criando uma função que irá receber uma mensagem como parametro
def leiaInt(msg):
    
    #Chave boolean
    ok=False

    #Iremos armazenar o valor inserido em input na variavel abaixo
    valor=0

    #Abrindo um loop que irá verificar se o valor inserido é ou não um valor integer valido
    while True:
        n=str(input(msg)) #Iremos armazenar o valor inserido no input nesta variavel
        
        if n.isnumeric(): #Se o valor inserido no input for integer
            valor=int(n) #A variavel de valor acima, irá receber o valor convertido para int
            ok=True #A chave boolean irá valer true, para podermos sair do loop
        else:
            print(f"{color2}Erro! Digite um numero inteiro valido!{color0}") #Caso contrario, iremos exibir uma mensagem de erro até que o usuario insira um valor correto

        if ok: #Saindo do loop
            break
    
    return valor #Retornando o valor da variavel          
    

#Chamando a função e armazenando o valor em input em uma variavel
n=leiaInt("Digite um numero: ")

#Imprimindo o valor inserido na variavel
print(f"{color1}Vc acabou de digitar o numero {n}{color0}")
