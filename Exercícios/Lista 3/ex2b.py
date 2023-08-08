NUMERO_TERMOS = 20

def fibonacci(n):
    """Imprime o n-ésimo número da sequência
    de Fibonacci."""
    a = 1
    b = 1
    c = None

    for i in range(n):
        c = a + b
        if i == 0 or i == 1:
            c = 1
        a = b
        b = c
    
    return c

def main():
    for n in range(NUMERO_TERMOS):
        print(fibonacci(n))

if __name__ == "__main__":
    main()