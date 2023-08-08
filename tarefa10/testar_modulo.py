# -*- coding:UTF-8 -*- 
def carregar_imagem_decodificada(nome_do_arquivo): #FUNÇÃO PRONTA
    """Lê o arquivo que corresponde à imagem no formato PBM
    com o nome nome_do_arquivo e devolve a largura, a altura
    e a imagem como uma matriz."""
    with open(nome_do_arquivo, "r") as arquivo: #"r" = leitura do arquivo
        altura = 0 
        largura = 0
        imagem = []
        for linha in arquivo:
            altura += 1
            largura = len(linha.strip())
            imagem.append(list(linha.strip()))
    assert altura % 2 == 0, "Altura da imagem deve ser par."

    return largura, altura, imagem

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo): #FUNÇÃO PRONTA
    """Escreve a imagem decodificada em um arquivo
    com nome nome_arquivo."""
    with open(nome_do_arquivo, "w") as arquivo:
        for i in range(altura):
            linha = ("".join(imagem[i]) + "\n")
            arquivo.write(linha)

def carregar_imagem_codificada(nome_do_arquivo):
    """Lê o arquivo que corresponde à imagem codificada
    com o nome nome_do_arquivo e devolve a largura, a altura
    e a lista de tuplas codificacao."""
    with open(nome_do_arquivo, "r") as imagem:
        imagem.readline()
        largura, altura = imagem.readline().strip().split()
        termos = imagem.readline().strip().split()
    codificacao = []
    for i in range(0, len(termos), 2):
        tupla = termos[i], termos[i+1]
        codificacao.append(tupla)

    return largura, altura, codificacao

def codificar(largura, altura, imagem):
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

def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    """Escreve a imagem codificada em um arquivo
    com nome nome_arquivo."""
    codificacao_str = ""
    for frequencia, bloco in codificacao:
        codificacao_str += "{frequencia} {bloco} ".format(frequencia, bloco)
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write("P1C\n" + f"{largura} {altura}\n")
        arquivo.write(codificacao_str)

def decodificar(largura, altura, codificacao): #FUNÇÃO PRONTA
    """Decodifica a imagem em formato run-length para o
    formato PBM."""
    imagem = [[0 for i in range(largura)] for i in range(altura)]
    contador = 0
    linha = 0
    largura = int(largura)
    for tupla in codificacao:
        frequencia = tupla[0]
        numero1 = tupla[1][0]
        numero2 = tupla[1][1] 
        for _ in range(frequencia):
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

def main():
    largura, altura, imagem = carregar_imagem_decodificada("arquivo.pbm")
    codificacao = codificar(largura, altura, imagem)
    print(largura)
    print(altura)
    print(codificacao)
    # escrever_imagem_codificada(largura, altura, codificacao, "codificadah.txt")
    decodificada = decodificar(largura, altura, codificacao)
    for linha in decodificada:
        print(linha)
    
main()