def ler_entrada():
    """Lê uma lista ordenada de números e um número sozinho."""
    
    lista = input().strip().split()
    numero = int(input().strip())

    return lista, numero

def busca_binaria(numero_procurado, lista, idx_inferior, idx_superior):
    """Retorna o índice de um número em uma lista;
    se o número não estiver na lista, retorna None."""
    m = (idx_inferior + idx_superior) // 2

    if int(lista[m]) == numero_procurado:
        return m
    elif idx_inferior >= idx_superior:
        if lista[idx_superior] == numero_procurado:
            return idx_superior
        else:
            return None
    elif numero_procurado > int(lista[m]):
        # m vira o novo limite inferior
        return busca_binaria(numero_procurado, lista, m + 1, idx_superior)
    elif numero_procurado < int(lista[m]):
        # m vira o novo limite superior
        return busca_binaria(numero_procurado, lista, idx_inferior, m - 1)
    
def imprimir_indice(idx_numero):
    """Imprime o índice que o número fornecido
    assume na lista; caso contrário, imprime "-1"."""
    
    if idx_numero is None:
        print(-1)
    else:
        print(idx_numero)

def main():
    lista, numero_procurado = ler_entrada()
    idx_numero = busca_binaria(numero_procurado, lista, 0, len(lista) - 1)
    imprimir_indice(idx_numero)

main()