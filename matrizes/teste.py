def ler_aquivo_palavras(nome_arquivo):
    """
    Lê um arquivo e devolve a lista de palavras,
    uma por linha
    """

    with open(nome_arquivo) as arquivo:
        palavras = []
        for linha in arquivo:
            palavra = linha.strip()
            palavras.append(palavra)

    return palavras

def separar_plurais(palavras):
    """
    Devolve a lista das palavras que terminam em s
    """
    plurais = []
    for palavra in palavras:
        if palavra[-1] == "s":
            plurais.append(palavra)
    return plurais

def calcular_diferenca(lista1, lista2):
    """
    Devolve uma lista com os elementos
    de lista1 que não estão em lista2
    """
    diferenca = []
    for valor in lista1:
        if valor not in lista2:
            diferenca.append(valor)
    return diferenca

def criar_arquivo_palavras(nome_arquivo, palavras):
    """
    Cria um arquivo nome_arquivo com as palavras,
    uma por linha
    """

    with open(nome_arquivo, "w") as arquivo:
        for palavra in palavras:
            linha = palavra + "\n"
            arquivo.write(linha)

def main():
    palavras = ler_aquivo_palavras("palavras.txt")
    plurais = separar_plurais(palavras)
    singulares = calcular_diferenca(palavras, plurais)

    print(plurais)
    print(singulares)

    criar_arquivo_palavras("plural.txt", plurais)
    criar_arquivo_palavras("singular.txt", singulares)

main()