"""Desafio 113: Reescreva a função leiaInt() que fizemos no Desafio 104, incluindo agora a possibilidade da digitação de um número de tipo invalido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

"""Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do Python, só que fazendo a validação para aceitar apenas um valor numero.

Ex: n=leiaInt('Digite um n')"""

color1="\033[1;31m"
color0="\033[m"

def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print(f"{color1}Por favor, digite somente numeros!{color0}")
            continue
        except KeyboardInterrupt:
            print(f"{color1}\nUsuario preferiu não digitar esse numero!{color0}")
            return 0
        else:
            return n
            
def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError,TypeError):
            print(f"{color1}Por favor, digite somente numeros!{color0}") 
            continue
        except KeyboardInterrupt:
            print(f"{color1}\nUsuario preferiu não digitar esse numero!{color0}")
            return 0            
        else:
            return n     
    

numeroInt = leiaInt("Digite um numero inteiro: ")
numeroFloat = leiaFloat("Digite um numero float: ")
print(f"O numero inteiro digitado foi {numeroInt} e o numero float foi {numeroFloat}.")