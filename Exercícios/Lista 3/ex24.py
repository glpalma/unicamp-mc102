def tabela_impares(n_linhas, n_colunas):
    """Imprime uma tabela de números ímpares
    com n_linhas e n_colunas."""
    numero = 1

    for linha in range(n_linhas):
        for coluna in range(n_colunas):
            print(numero, end=' ')
            numero += 2
        print()


def main():
    m = int(input("m: "))
    n = int(input("n: "))
    tabela_impares(m, n)

main()