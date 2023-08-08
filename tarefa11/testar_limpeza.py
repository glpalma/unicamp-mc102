from frequencia import calcular_histograma_palavras, calcular_num_maior_quartil, receber_entrada

def main():
    palavras_texto, stop_words = receber_entrada()
    #lista_teste = [("bolo", 9), ("batata", 1), ("jorge", 5), ("pão", 2), ("gustavo", 7)]
    histograma = calcular_histograma_palavras(palavras_texto, stop_words)
    print(histograma)
    
    # filtrados = filtrar_palavras_frequencia(histograma, 2)
    quantidade = calcular_num_maior_quartil(histograma)
    print(quantidade)
    #print(filtrados)
    # lista_teste.sort(key=devolver_frequencia)
    # print(lista_teste)

main()