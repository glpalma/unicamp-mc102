def ler_lista_numeros():
    """Lê uma lista de numeros do teclado."""
    lista = input().strip().split()

    return lista

def intercalar(lista, inicio, meio, fim):
    """Ordena a lista separada em duas listas ordenadas."""
    i = inicio
    j = meio + 1
    lista_ordenada = []

    while i <= meio and j <= fim:
        if int(lista[i]) >= int(lista[j]):
            lista_ordenada.append(lista[j])
            j += 1
        elif int(lista[i]) < int(lista[j]):
            lista_ordenada.append(lista[i])
            i += 1
        elif int(lista[i]) == int(lista[j]):
            lista_ordenada.append(lista[j])
            j += 1
            lista_ordenada.append(lista[i])
            i += 1
    
    while i <= meio:
        lista_ordenada.append(lista[i])
        i += 1
        
    while j <= fim:
        lista_ordenada.append(lista[j])
        j += 1

    i = 0
    for j in range(inicio, fim + 1):
        lista[j] = lista_ordenada[i]
        i += 1

def merge_sort(lista, inicio, fim):
    """Ordena a lista do inicio ao fim."""

    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio + 1, fim)
        intercalar(lista, inicio, meio, fim)

def main():
    lista_numeros = ler_lista_numeros()
    merge_sort(lista_numeros, 0, len(lista_numeros) - 1)
    print(' '.join(lista_numeros))

main()