"""Desafio 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.

B) Os ultimos 4 colocados da tabela.

C) Uma lista com os times em ordem alfabetica.

D) Em que posição na tabela está o time da Chapecoense."""

c1="\033[1;32m"
c2="\033[1;33m"
c0="\033[m"

tabela=("Botafogo", "Palmeiras", "Gremio", "Flamengo", "Bragantino", "Fluminense", "Athletico-PR", "Fortaleza", "Atletico-MG", "Cruzeiro", "Internacional", "Cuiaba", "Sao Paulo", "Corinthians", "Bahia", "Goais", "Santos", "Vasco da Gama", "America-MG", "Chapecoense");

print(f"{c1}Bem vindo ao brasileirao da Alexa!{c0}");
print(f"{c2}Segue tabela dos primeiros 20 colocados:{c0}");

for i,n in enumerate(tabela):
    print(f"{i+1}: {n}");

print(f"{c2}Primeiros 5 colocados da tabela:{c0}")
for i,n in enumerate(tabela[0:5]):
    print(f"{i+1}º: {n}");
print();

print(f"{c2}Ultimos 4 colocados da tabela:{c0}")
for i, n in enumerate(tabela[-4:]):
    print(f"{len(tabela)-3+i}º: {n}");
print();

print(f"{c2}Lista em ordem alfabetica:{c0}")
listaAlfabetica=sorted(tabela);
print(", ".join(listaAlfabetica))
print();

print(f"\n{c2}O time da Chapecoense esta na {tabela.index('Chapecoense')+1}º posicao!{c0}");
