"""Desafio 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas():
    print("-="*10)

def Termos():
    while True:
        try:
            termos=int(input("Digite a quantidade de termos que iremos exibir: "))
            return termos
            break
        except:
            print(f"{c2}Erro! Digite somente numeros.{c0}")

print(f"{c1}Bem vindo ao calculador de PAs 3.0 da Alexa!{c0}")

while True:
    try:
        n1=int(input("Digite o numero inicial: "))
        n2=int(input("Digite de quanto em quantos numeros iremos pular: "))
        break
    except:
        print(f"{c2}Erro! Digite somente numeros.{c0}")

while True:    
    num_Termos=Termos()
    Linhas()
    for n in range(1,num_Termos+1):
        pa=n1+(n-1)*n2
        if n==num_Termos:
            print(f"{pa}",end=" > FIM")
        else:
            print(f"{pa}",end=" > ")  
    print()
    Linhas()
    

    while True:    
        c=str(input("Deseja mostrar mais alguns termos? [S/N]")).upper()[0]
        if c.isalpha():
            break
        else:
            print(f"{c2}Erro! Digite somente S ou N.{c0}")
    
    if c in "N":
        print(f"{c1}Obrigado e volte sempre!{c0}")
        break
    


