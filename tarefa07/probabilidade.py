def ler_sequencia_numeros_entrada():
    """Lê uma sequência de números separados
    por espaço e a transforma em uma lista."""
    sequencia = input().split()
    return sequencia

def fornecer_idx_menor(lista):
    """Devolve o índice do menor valor de uma lista
    fornecida como argumento."""
    idx_menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[idx_menor]:
            idx_menor = i
    return idx_menor

def fornecer_menor_valor(lista):
    """Devolve o menor valor de uma lista
    fornecida como argumento."""
    menor = lista[0]
    for valor in lista:
        valor = float(valor)
        if valor < menor:
            menor = valor
    return menor

def calcular_probabilidades(lista):
    """Devolve duas listas: uma com os números da lista
    fornecida sem repetição e outra com as respectivas
    probabilidades de esses números serem encontrados na
    lista fornecida (mesmos índices)."""
    itens_lista = []
    probabilidade = []
    for valor in lista:
        contador = 0
        if valor not in itens_lista:
            itens_lista.append(valor)
            for j in range(len(lista)):
                if valor == lista[j]:
                    contador += 1
            probabilidade.append(contador/len(lista))
    return itens_lista, probabilidade

def ordenar_lista(lista, probabilidades): 
    """Recebe uma lista de números como argumento
    junto às respectivas probabilidades e devolve
    uma lista ordenada."""
    n = len(probabilidades)
    for _ in range(n-1):
        for i in range(n-1):
            if probabilidades[i] > probabilidades[i+1]:
                aux_p = probabilidades[i]
                probabilidades[i] = probabilidades[i+1]
                probabilidades[i+1] = aux_p

                aux_n = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux_n

    for _ in range(n-1): 
        for j in range(n-1):
            if probabilidades[j] == probabilidades[j+1]:
                if lista[j] > lista[j+1]:
                    aux_f = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux_f

    return lista

def main():
    sequencia = ler_sequencia_numeros_entrada()
    lista, probabilidades = calcular_probabilidades(sequencia)
    lista_ordenada = ordenar_lista(lista, probabilidades)
    print(" ".join(lista_ordenada))

main()