"""Desafio 95: Aprimore o DESAFIO 93 para que ele funcione com varios jogadores, incluido um sistema de vizualização de detalhes do aproveitamento de cada jogador."""

time=list()
jogador=dict()
partidas=list()

while True:
    jogador.clear()
    jogador['Nome']=str(input("Digite o nome do jogador: "))
    tot=int(input(f"Quantas partidas o jogador {jogador['Nome']} jogou: "))
    partidas.clear()

    for c in range(0,tot):
        partidas.append(int(input(f"     Quantos gols na partida {c+1}? ")))
    jogador['Gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())

    while True:
        resp=str(input("Deseja continuar? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("Erro! Responda apenas S ou N.")

    if resp=="N":
        break

print("-="*10)
print("Cod ",end="")
for i in jogador.keys():
    print(f"{i:<15}",end="")
print()
print("-"*50)
for k , v in enumerate(time):
    print(f"{k:>3} ",end="")
    for d in v.values():
        print(f"{str(d):<15}",end="")
    print()
print("-"*50)
while True:
    busca=int(input("Mostrar dados de qual jogador? [999 para sair]"))
    if busca==999:
        break
    if busca>len(time):
        print(f"Erro não existe jogador com o codigo da {busca}!")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['Gols']):
            print(f"     No jogo {i+1} fez {g} gols.")
    print("=-"*10)
print("Volte sempre!")