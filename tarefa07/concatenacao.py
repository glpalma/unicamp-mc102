lista_A = input().split()
lista_B = input().split()
lista_C = []

for i in range(len(lista_A)):
    elemento = lista_A[i] + lista_B[i]
    lista_C.append(elemento)

print(" ".join(lista_C))