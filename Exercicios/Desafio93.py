"""Desafio 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade gols feitos em cada partida. No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato."""

color1="\033[1;32m"
color2="\033[1;31m"
colorReset="\033[m"

futebol={"Nome do jogador":[],"Quantidade de partidas":[],"Gols por partida":[],"Total de gols":[]}

print(f"{color1}Bem vindo ao campeonato de futebol da AlexaSports 2023!{colorReset}")
while True:
    #Nome do jogador
    while True:        
        nome=str(input("Digite o nome do jogador: "))
        if nome.isalpha():
            futebol["Nome do jogador"].append(nome)
            break
        else:
            print(f"{color2}Erro! Digite o nome do jogador!{colorReset}")    

    #Quantidade de partidas que o jogador jogou
    while True:
        try:
            quantPartidas=int(input(f"Digite a quantidade de partidas que o jogador {nome} jogou durante o campeonato: "))
            futebol["Quantidade de partidas"].append(quantPartidas)
            break
        except:
            print(f"{color2}Erro! Digite em numeros a quantidade de partidas jogadas!{colorReset}")

    #Quantidade de gols para cada partida
    gols=[]
    golsTotal=0
    for g in range(quantPartidas):        
        while True:
            try:
                golsPartida=int(input(f"{g+1}º partida: "))
                gols.append(golsPartida)
                golsTotal+=golsPartida
                break
            except:
                print(f"{color2}Erro! Digite a quantidade de gols em numeros!{colorReset}")    
    futebol["Gols por partida"].append(gols)
    futebol["Total de gols"].append(golsTotal)

    while True:        
        c=str(input("Deseja continuar cadastrando: [S/N]")).upper()[0]
        if c in ["S","N"]:
            break
        else:
            print(f"{color2}Erro! Digite somente S ou N!{colorReset}")

    if c in "Nn":
        break 

#Resumo Geral
print(f"{color1}Leaderboard:{colorReset}")
for i in range(len(futebol["Nome do jogador"])):
    #Exibindo o nome do jogador e quantidade de partidas
    print(f"Jogador: {futebol['Nome do jogador'][i]}")
    print(f"Quantidade de partidas: {futebol['Quantidade de partidas'][i]}")
    
    #Exibindo cada gol por partida
    for j,g in enumerate(futebol["Gols por partida"][i]):
        print(f"{j+1}º partida: {g} gols.")

    #Exibindo quantidade total de gols
    print(f"Quantidade total de gols: {futebol['Total de gols'][i]}")

    print("-="*10)



