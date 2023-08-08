def calcular_produto_interno(A, B, i, j):
    """Devolve o item de índices i e j do produto das
    matrizes A e B."""
    assert len(A[0]) == len(B), "Matrizes devem ser compatíveis"
    l = len(B)
    soma = 0.0
    for k in range(l):
        soma += A[i][k] * B[k][j]
    return soma

def multiplicar_matrizes(A, B):
    """Devolve o produto das matrizes A e B
    fornecidas como parâmetro."""
    assert len(A[0]) == len(B), "Matrizes devem ser compatíveis"
    m = len(A)
    l = len(B)
    n = len(B[0])
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = calcular_produto_interno(A, B, i, j)
    return C

def main():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    B = [
        [1, 1, 1],
        [1, 3, 1],
        [1, 1, 2]
    ]
    produto = multiplicar_matrizes(A, B)
    print(produto)

main()