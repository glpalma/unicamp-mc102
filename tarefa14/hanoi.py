def n_hanoi(n, origem, destino, auxiliar, contador):
    """Devolve o número mínimo de passos necessários para
    mover um número n de discos de uma origem até um destino."""

    if n == 1 or n == 0:
        return n
    else:
        soma = n_hanoi(n - 1, origem, auxiliar, destino, contador) + 1 + n_hanoi(n - 1, auxiliar, destino, origem, contador)
        return soma
        
def main():
    n = int(input())
    n_passos = n_hanoi(n, "A", "C", "B", 0)
    print(n_passos)

main()