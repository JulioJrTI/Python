"""Desafio 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

c1="\033[1;32m"
c2="\033[1;31m"
c0="\033[m"

while True:
    texto=str(input("Digite uma palavra ou frase: (ou digite 0 para sair)"))

    if texto=="0":
        break
    
    else:
        if "(" in texto[0] and ")" in texto[-1]:
            print(f"{c1}Temos parenteses em ambos os lados!{c0}")
        else:        
            if "(" in texto[0]:
                print(f"{c1}Temos parenteses no lado esquerdo.{c0}",end=" ")
                if ")" not in texto[-1]:
                    print(f"{c2}Porem não temos parenteses no lado direito!{c0}")            

            elif ")" in texto[-1]:
                print(f"{c1}Temos parenteses no lado direito.{c0}",end=" ")
                if "(" not in texto[0]:
                    print(f"{c2}Porem não temos pareteses no lado esquerdo!{c0}")
            
            else:
                print(f"{c2}Não temos parenteses em ambos os lados!{c0}")
        
               
            

    