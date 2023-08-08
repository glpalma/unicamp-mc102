entrada = input()
saida = ""

for i in range(len(entrada)):
    if entrada[i].islower(): 
        aux = entrada[i].capitalize()
        saida += aux
    elif not entrada[i].islower():
        aux = entrada[i].casefold()
        saida += aux

print(saida)