"""Desafio 87: Aprimore o desafio anterios, mostrando no final:

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

matriz=[[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]
somaTotal=0
somaTerceiraColuna=0
maiorSegundaLinha=0

print(f"{c1}Bem vindo ao listador de blocos numerais da Alexa!{c0}")
for l in range(0,3):
    for c in range(0,3):
        while True:
            try:
                matriz[l][c]=int(input(f"Digite um valor para [{l} e {c}]: "))
                break
            except:
                print(f"{c2}Erro! Digite somente numeros!{c0}")
        if matriz[l][c]%2==0:
            num=matriz[l][c]
            somaTotal+=num
        if c==2:
            somaTerceiraColuna+=matriz[l][c]
        if l==1 and matriz[l][c]>maiorSegundaLinha:
            maiorSegundaLinha=matriz[l][c]

print("-="*10)

print(f"{c1}Segue a lista de numeros digitados:")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]",end="")
    print()

print(f"Soma de numeros pares digitados na lista: {somaTotal}")
print(f"Soma de numeros da terceira coluna: {somaTerceiraColuna}")
print(f"Maior numero da segunda linha: {maiorSegundaLinha}{c0}")