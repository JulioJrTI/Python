"""Desafio 72: Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de zero até 20. Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

def Linhas(variavel):
    l="~"*len(variavel)
    print(l)

numerosExtenso=("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifhteen","Sixteen","Seventeen","Eighteen", "Nineteen","Twenty")

print(f"{c1}Bem vindo ao extensor de numeros da Alexa!{c0}")
while True: 
    try:
        num=int(input("Digite um numero:"))    
        if num>=0 and num<=20:
            Linhas(numerosExtenso[num])
            print(f"O numero escolhido foi: {numerosExtenso[num]}")
            Linhas(numerosExtenso[num])            
        else:
            print(f"{c2}Digite um numero entre 0 e 20!{c0}")
    except:
       print(f"{c2}Por favor, digite um numero valido!{c0}")

    c=str(input("Deseja continuar: [S/N]")).upper()[0]

    if c in "Nn":
        print(f"{c1}Obrigado e volte sempre!{c0}")
        break        
        

    
        
    

    