def calcular_transposta(matriz):
    """Devolve a transposta da matriz fornecida
    como argumento."""
    m = len(matriz) #número de linhas
    n = len(matriz[0]) #número de colunas
    transposta = []
    for i in range(m):
        linha = []
        for j in range(n):
            celula = matriz[j][i]
            linha.append(celula)
        transposta.append(linha)
    return transposta

def main():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transposta = calcular_transposta(a)
    print(transposta)
    
main()