from datetime import date

anoAtual=date.today().year
anoNascimento=int(input("Ano de nascimento: "))

idade=anoAtual-anoNascimento

print(idade)

