def bubble_sort(lista):
    n = len(lista)
    for _ in range(n-1):
        for i in range(n - 1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

def main():
    lista = [0.2, 0.1, 0.1, 0.2, 0.1, 0.2, 0.1]
    bubble_sort(lista)
    print(lista)

main()