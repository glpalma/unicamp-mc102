texto = input()
n = int(input())

saida = """"""

d = len(texto)//n #número de carac. em cada linha
contador = d

for i in range(len(texto)):
    if i == contador:
        saida += texto[i]
        saida += "\n"
        contador += d
    else: 
        saida += texto[i]

print(saida)