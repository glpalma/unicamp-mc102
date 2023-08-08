from math import ceil, floor

def frequencia_tupla(tupla): # usada na ordenação do histograma
    return tupla[1] 

def limpar_palavras(lista_palavras):
    """Retorna uma lista de palavras sem letras maiúsculas ou
    sinais de pontuação."""
    sinais_pontuacao = {".", ",", "!", "?", "(", ")", "[", "]", "{", "}", ";", ":", "'"}
    lista_palavras_limpas = []

    for palavra in lista_palavras:
        palavra_limpa = ""
        for caractere in palavra:
            if caractere not in sinais_pontuacao:
                caractere = caractere.casefold() # transforma maiúsculos em minúsculos
                palavra_limpa += caractere

        lista_palavras_limpas.append(palavra_limpa)
    
    return lista_palavras_limpas

def receber_entrada():
    """Recebe a entrada de um texto e de stop-words e devolve uma
    lista com as palavras do texto e um conjunto com as stop-words."""
    nome_arquivo = input()
    stop_words = set(input().split())
    palavras_texto = []

    with open(nome_arquivo, "r") as texto:
        for linha in texto:
            palavras_linha = linha.strip().split()
            palavras_formatadas = limpar_palavras(palavras_linha)
            for palavra in palavras_formatadas:
                palavras_texto.append(palavra)
                
    return palavras_texto, stop_words

def calcular_histograma_palavras(lista_palavras, excecoes):
    """Retorna um histograma de palavras fornecidas como argumento
    sem contar palavras fornecidas em excecoes."""
    histograma = dict()

    for palavra in lista_palavras:
        if palavra not in excecoes:
            if palavra not in histograma:
                histograma[palavra] = 1
            else:
                histograma[palavra] += 1

    histograma = list(histograma.items())
    histograma.sort(key=frequencia_tupla, reverse=True) # ordenar o histograma a partir das frequências
    n = len(histograma)

    for _ in range(n-1): 
        for j in range(n-1):
            if histograma[j][1] == histograma[j+1][1]:
                if histograma[j][0] > histograma[j+1][0]:
                    aux_f = histograma[j]
                    histograma[j] = histograma[j+1]
                    histograma[j+1] = aux_f

    return histograma

def filtrar_palavras_frequencia(histograma, limite):
    """Retorna uma lista de palavras filtradas de acordo com um limite
    relacionado à frequência."""
    filtrados = []

    for palavra, frequencia in histograma:
        if frequencia > limite:
            par = (palavra, frequencia)
            filtrados.append(par)
        
    return filtrados

def encontrar_idx_quartil(lista_palavras):
    """Retorna o índice do primeiro quartil de uma lista."""
    m = len(lista_palavras)
    idx_quartil = (m + 1)/4
    auxiliar = idx_quartil - int(idx_quartil) # parte fracionária do idx
    
    if auxiliar >= 0.5:
        return ceil(idx_quartil) - 1
    elif auxiliar < 0.5:
        return floor(idx_quartil) - 1
    else:
        return idx_quartil - 1

def calcular_num_maior_quartil(lista_palavras):
    """Retorna a quantidade de números que apresentam frequência maior
    ou igual ao quartil de uma lista."""
    i = encontrar_idx_quartil(lista_palavras) # índice do quartil da lista

    contador = 0
    for _, frequencia in lista_palavras:
        if frequencia >= lista_palavras[i][1]: 
            contador += 1

    return contador

def calcular_palavras_menor_quartil(lista_palavras):
    """Retorna uma string com até três palavras com frequência menor
    à do quartil de uma lista."""
    i = encontrar_idx_quartil(lista_palavras)
    palavras_alem_quartil = ""
    contador = 0
    frequencia_quartil = lista_palavras[i][1]

    for palavra, frequencia in lista_palavras:
        if frequencia < frequencia_quartil:
            palavras_alem_quartil += palavra + " "
            contador += 1
            if contador == 3:
                break

    return palavras_alem_quartil

def separar_mais_frequentes(histograma, numero):
    """Separa um número específico das palavras mais frequentes
    de um histograma."""
    separadas = ""

    for i, tupla in enumerate(histograma):
        separadas += tupla[0] + " "
        if i == (numero - 1):
            break

    return separadas

def exibir_saida(palavras_mais_frequentes, frequencia_maior_quartil, palavras_alem_quartil):
    """Exibe as três palavras mais frequentes do texto, o número de palavras com frequência
    maior ou igual à do quartil e as palavras com frequência menor do que a do quartil."""
    
    print(palavras_mais_frequentes)
    print(frequencia_maior_quartil)
    print(palavras_alem_quartil)

def main():
    lista_palavras, stop_words = receber_entrada()
    histograma = calcular_histograma_palavras(lista_palavras, stop_words)

    palavras_filtradas_frequencia = filtrar_palavras_frequencia(histograma, 5)

    quantidade_maior_quartil = calcular_num_maior_quartil(palavras_filtradas_frequencia)

    tres_palavras_mais_frequentes = separar_mais_frequentes(histograma, 3)

    palavras_alem_quartil = calcular_palavras_menor_quartil(palavras_filtradas_frequencia)

    exibir_saida(tres_palavras_mais_frequentes, quantidade_maior_quartil, palavras_alem_quartil)

if __name__ == '__main__':
    main()
