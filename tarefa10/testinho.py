from modulo import decodificar, carregar_imagem_codificada, carregar_imagem_decodificada, escrever_imagem_decodificada
from bordas import destacar_bordas

def main():
    entrada = input()
    saida = input()
    largura, altura, imagem = carregar_imagem_decodificada(entrada)
    #decodificada = decodificar(largura, altura, codificada)
    bordas = destacar_bordas(largura, altura, imagem) #probelma tá aqui
    escrever_imagem_decodificada(largura, altura, bordas, saida)

main()