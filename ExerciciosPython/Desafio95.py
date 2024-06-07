"""Desafio 95: Aprimore o DESAFIO 93 para que ele funcione com varios jogadores, incluido um sistema de vizualização de detalhes do aproveitamento de cada jogador."""

time = []

while True:
    jogador = {'Nome': input("Digite o nome do jogador: "), 'Gols': [], 'Total': 0}
    tot = int(input(f"Quantas partidas o jogador {jogador['Nome']} jogou: "))

    for c in range(tot):
        jogador['Gols'].append(int(input(f"     Quantos gols na partida {c+1}? ")))

    jogador['Total'] = sum(jogador['Gols'])
    time.append(jogador)

    resp = input("Deseja continuar? [S/N]").upper()
    if resp != 'S':
        break

print("-=" * 20)
print(f"{'Cod':<5}{'Nome':<15}{'Gols':<30}{'Total':<10}")
print("-" * 70)

for k, jogador in enumerate(time):
    print(f"{k:<5}{jogador['Nome']:<15}{str(jogador['Gols']):<30}{jogador['Total']:<10}")

print("-" * 70)

while True:
    busca = int(input("Mostrar dados de qual jogador? [999 para sair]"))
    if busca == 999:
        break
    if 0 <= busca < len(time):
        print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['Gols']):
            print(f"     No jogo {i+1} fez {g} gols.")
    else:
        print(f"Erro não existe jogador com o código {busca}!")
    print("=-" * 20)

print("Volte sempre!")
