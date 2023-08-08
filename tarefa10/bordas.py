from modulo import *

def verificar_arredores(imagem, i, j, numero, condicao):
    """Verifica se o número localizado na posição (i, j)
    de uma imagem fornecida possui um número especificado
    em volta de si de acordo com uma condição."""
    if condicao == 'pelo_menos':
        try:
            if (imagem[i+1][j] == numero) or (imagem[i][j+1] == numero) or (imagem[i-1][j] == numero) or (imagem[i][j-1] == numero):
                # checa a presença do número na vertical e horizontal
                return True
            elif (imagem[i-1][j-1] == numero) or (imagem[i+1][j+1] == numero) or (imagem[i-1][j+1] == numero) or (imagem[i+1][j-1] == numero):
                # checa a presença do número na diagonal
                return True
            else:
                return False
        except IndexError:
            if (imagem[i-1][j] == numero) or (imagem[i][j-1] == numero):
                return True
            elif i == (len(imagem) - 1) or i == 0 or j == (len(imagem[i]) - 1) or j == 0:
                # contorno do objeto nos limites da imagem
                return True 
            else:
                return False
    elif condicao == 'todos':
        if (imagem[i-1][j] == numero) and (imagem[i+1][j] == numero) and (imagem[i][j-1] == numero) and (imagem[i][j+1] == numero):
            return True
        else:
            return False

def destacar_bordas(largura, altura, imagem):
    """Delimita as bordas do objeto da imagem
    fornecida."""
    nova_imagem = [['0' for i in range(largura)] for i in range(altura)]
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] == '1' or imagem[i][j] == 1:
                if verificar_arredores(imagem, i, j, "0", "pelo_menos"): #pelo menos um 0
                    # verifica se faz parte da borda
                    nova_imagem[i][j] = '1'
                elif j == 0:
                    nova_imagem[i][j] = '1'
                
    return nova_imagem


def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
