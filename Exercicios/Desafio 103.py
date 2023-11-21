"""Desafio 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

# Criando uma função que irá receber o nome de um jogador e a quantidade de gols feitas no campeonato como parametros opcionais
def ficha(nome="",gols=0):   
    print("-="*30)
    
    # O nome do jogador
    nome=str(input("Digite o nome do jogador: "))    
    
    #Mecanica de erro, caso o usuario não digite o nome do jogador, o nome do mesmo será desconhecido
    if nome=="":
        nome="<desconhecido>"            
    
    #Mecanica de erro, caso o osuario não digite a quantidade de gols, a quantidade será exibida normalmente porem será 0
    try:
        gols=int(input("Quantos gols: "))
    except:
        gols=0          
    
    #Retornando os valores digitados na função
    return f"O(a) jogador(a) {nome} fez {gols} gol(s) durante o campeonato."
    
#Imprimindo função e seus parametros      
print(ficha())