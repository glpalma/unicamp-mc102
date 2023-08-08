def triangulo_floyd(n):
    """Imprime um triângulo de Floyd
    com n linhas."""
    numero_atual = 1
    linha = 1

    while linha <= n:
        for _ in range(linha):
            print(numero_atual, end=' ')
            numero_atual += 1
        linha += 1
        print()

def main():
    n = int(input())
    triangulo_floyd(n)

main()