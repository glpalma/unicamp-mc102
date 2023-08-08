lista_A = input().split()
lista_B = input().split()

lista_C = []
for i in lista_A:
    if i in lista_B:
        if i not in lista_C: # sem essa condição, a lista_C fica com itens repetidos
            lista_C.append(i)

print(" ".join(lista_C))