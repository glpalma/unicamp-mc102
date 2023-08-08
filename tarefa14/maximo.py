def ler_entrada():
    """Lê uma sequência de números separados por vírgula."""
    lista = input().strip().split()

    return lista

def maximo_lista(lista, inicio, fim):
    """Devolve o valor máximo de 
    um recorte de uma lista."""

    if inicio == fim:
        return lista[inicio]
    else:
        m = (inicio + fim) // 2
        maximo_up = int(maximo_lista(lista, m + 1, fim))
        maximo_down = int(maximo_lista(lista, inicio, m))
        if maximo_up > maximo_down:
            return maximo_up
        else:
            return maximo_down

def main():
    lista = ler_entrada()
    maximo = maximo_lista(lista, 0, len(lista) - 1)
    print(maximo)

main()