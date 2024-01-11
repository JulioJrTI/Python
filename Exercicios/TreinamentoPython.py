valorFloat=input("Digite um valor (sem virgula): ")

if "," in valorFloat:
    valorFloat = valorFloat.replace(",",".")
valorFloat = float(valorFloat)    

print(valorFloat)