def collatz(numero, contador):
    """Devolve o número de repetições necessárias
    da conjectura de Collatz para chegar a 1."""
    
    if numero == 1:
        return contador
    elif numero % 2 == 0:
        contador += 1
        n = numero / 2
        return collatz(n, contador)
    else:
        contador += 1
        n = (3 * numero + 1)/2
        return collatz(n, contador)

def main():
    n = int(input())
    n_repeticoes = collatz(n, 0)
    print(n_repeticoes)
    
main()