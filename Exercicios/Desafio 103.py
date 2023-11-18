"""Desafio 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def ficha(nome="",gols=0):   
    print("-="*30)
    nome=str(input("Digite o nome do jogador: "))    
    try:
        gols=int(input("Quantos gols: "))
    except:
        gols=0     

    if nome=="":
        nome="<desconhecido>"      
    
    return f"O(a) jogador(a) {nome} fez {gols} gol(s) durante o campeonato."
    
      
print(ficha())


"""nomeJogador=str(input("Digite o nome do jogador: "))
quantGols=int(input("Quantos gols foram feitos: "))
print(ficha(nomeJogador,quantGols))"""