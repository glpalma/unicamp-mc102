def receber_numeros():
    """Lê os números a e b separados por espaço."""
    a, b = input().strip().split()

    return int(a), int(b)

def potencia(a, b):
    """Devolve "a" elevado à potência "b"."""

    if b == 0:
        return 1
    else:
        return a * potencia(a, b - 1)

def main():
    a, b = receber_numeros()
    print(potencia(a, b))

main()