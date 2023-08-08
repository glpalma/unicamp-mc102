from frequencia import limpar_palavras, frequencia_tupla

def ler_entrada():
    """Lê o caminho do texto e os pares de palavras aos
    quais serão sugeridas continuações."""
    caminho_texto = input()
    pares_palavras = []

    try:
        while True:
            par = input()
            pares_palavras.append(par)
    except EOFError:
        return caminho_texto, pares_palavras

def ler_texto(nome_arquivo):
    """Devolve uma lista com as palavras do texto cujo
    caminho foi fornecido."""
    palavras_texto = []

    with open(nome_arquivo) as texto:
        for linha in texto:
            palavras_linha = linha.strip().split()
            palavras_formatadas = limpar_palavras(palavras_linha)
            for palavra in palavras_formatadas:
                palavras_texto.append(palavra)

    return palavras_texto

def encontrar_terceiras_palavras(palavras_texto, pares_palavras):
    """Devolve uma lista com os pares de palavras e as palavras
    que vêm após juntas às suas respectivas frequências."""
    pares_com_mais_frequentes = []

    for par in pares_palavras:
        par_l = par.split() # separa o par em duas strings
        par_com_mais_frequentes = [par, {}]
        achou_primeira = False
        for i, palavra_texto in enumerate(palavras_texto):
            if achou_primeira and palavra_texto == par_l[1]:
                if palavras_texto[i+1] not in par_com_mais_frequentes[1]:
                    par_com_mais_frequentes[1][palavras_texto[i+1]] = 1
                else:
                    par_com_mais_frequentes[1][palavras_texto[i+1]] += 1
            elif palavra_texto == par_l[0]:
                achou_primeira = True
            else:
                achou_primeira = False
        pares_com_mais_frequentes.append(par_com_mais_frequentes)

    return pares_com_mais_frequentes

def preparar_sugestoes(palavras_frequentes):
    """Devolve uma lista de tuplas. Cada tupla contém um par de
    palavras e a a palavra mais frequente que vem após o par."""
    sugestoes = []    

    for par, dicio in palavras_frequentes:
        dicio = list(dicio.items()) # transforma o dicionário em uma lista de tuplas
        dicio.sort(key=frequencia_tupla, reverse=True) # coloca a palavra com mais ocorrências em primeiro lugar
        n = len(dicio)
        for _ in range(n-1): 
            for j in range(n-1):
                if dicio[j][1] == dicio[j+1][1]:
                    if dicio[j][0] > dicio[j+1][0]:
                        aux = dicio[j]
                        dicio[j] = dicio[j+1]
                        dicio[j+1] = aux
        bloco = (par, dicio[0][0])
        sugestoes.append(bloco)

    return sugestoes

def exibir_saida(sugestoes):
    """Exibe cada par de palavras seguido de suas sugestões."""
    
    for par, sugestao in sugestoes:
        print(par, sugestao)

def main():
    caminho_texto, pares_palavras = ler_entrada()
    palavras_texto = ler_texto(caminho_texto)
    pares_com_mais_frequentes = encontrar_terceiras_palavras(palavras_texto, pares_palavras)
    sugestoes = preparar_sugestoes(pares_com_mais_frequentes)
    exibir_saida(sugestoes)

main()
