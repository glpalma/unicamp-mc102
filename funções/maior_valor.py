lista = [2, 4, 7, 10, 51, 13, 17]
maximo = lista[0]
for numero in lista:
    if numero > maximo:
        maximo = numero

print(maximo)