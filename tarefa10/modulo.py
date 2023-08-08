def codificar(largura, altura, imagem): #FUNÇÃO PRONTA
    """Codifica a imagem de formato PBM para run-length
    (modificado)."""
    contador = 0
    codificacao = []
    bloco_anterior = str(imagem[0][0]) + str(imagem[1][0])
    for i in range(0, altura, 2):
        for j in range(largura):
            bloco = str(imagem[i][j]) + str(imagem[i + 1][j])
            if bloco != bloco_anterior:
                tupla = contador, bloco_anterior
                codificacao.append(tupla)
                contador = 0
            bloco_anterior = bloco
            contador += 1
            if i == (len(imagem) - 2) and j == (len(imagem[-2]) - 1):
                tupla = contador, bloco_anterior
                codificacao.append(tupla)

    return codificacao

def decodificar(largura, altura, codificacao): #FUNÇÃO PRONTA
    """Decodifica a imagem em formato run-length para o
    formato PBM."""
    largura = int(largura)
    imagem = [[0 for i in range(largura)] for i in range(int(altura))]
    contador = 0
    linha = 0
    for tupla in codificacao:
        frequencia = tupla[0]
        numero1 = tupla[1][0]
        numero2 = tupla[1][1] 
        for _ in range(int(frequencia)):
            if linha == 0:
                coluna = contador
            else:
                coluna = int(contador - (largura * (linha/2)))
            imagem[linha][coluna] = numero1
            imagem[linha + 1][coluna] = numero2
            contador += 1
            if contador % largura == 0: 
                linha += 2

    return imagem

def carregar_imagem_codificada(nome_do_arquivo): #FUNÇÃO PRONTA
    """Lê o arquivo que corresponde à imagem codificada
    com o nome nome_do_arquivo e devolve a largura, a altura
    e a lista de tuplas codificacao."""
    with open(nome_do_arquivo, "r") as imagem:
        imagem.readline()
        largura, altura = imagem.readline().strip().split()
        termos = imagem.readline().strip().split()
    altura = int(altura)
    largura = int(largura)
    codificacao = []
    for i in range(0, len(termos), 2):
        tupla = termos[i], termos[i+1]
        codificacao.append(tupla)

    return largura, altura, codificacao

def carregar_imagem_decodificada(nome_do_arquivo): #FUNÇÃO PRONTA
    """Lê o arquivo que corresponde à imagem no formato PBM
    com o nome nome_do_arquivo e devolve a largura, a altura
    e a imagem como uma matriz."""
    with open(nome_do_arquivo, "r") as arquivo: #"r" = leitura do arquivo
        arquivo.readline()
        largura, altura = arquivo.readline().split()
        imagem = []
        for linha in arquivo:
            imagem.append(list(linha.strip()))
    altura = int(altura)
    largura = int(largura)
    assert altura % 2 == 0, "Altura da imagem deve ser par."

    return largura, altura, imagem

def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo): #FUNÇÃO PRONTA
    """Escreve a imagem codificada em um arquivo
    com nome nome_arquivo."""
    codificacao_str = ""
    for frequencia, bloco in codificacao:
        codificacao_str += f"{frequencia} {bloco} "
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write("P1C\n" + f"{largura} {altura}\n")
        arquivo.write(codificacao_str)

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo): #FUNÇÃO PRONTA
    """Escreve a imagem decodificada em um arquivo
    com nome nome_arquivo."""
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write(f"P1\n{largura} {altura}\n")
        for i in range(altura):
            for indice_lista in range(len(imagem[i])):
                imagem[i][indice_lista] = str(imagem[i][indice_lista])
            linha = imagem[i]
            horizontal = ("".join(linha) + "\n")
            arquivo.write(horizontal)
