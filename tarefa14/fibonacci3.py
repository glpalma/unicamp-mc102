def fibonacci3(numero, memoria):
    """Devolve o n-ésimo termo da sequência de Fibonacci."""

    if numero not in memoria:
        if (numero >= 0) and (numero <= 2):
            memoria[numero] = numero
            return numero
        else:
            nesimo_termo = fibonacci3(numero - 1, memoria) + fibonacci3(numero - 2, memoria) + fibonacci3(numero - 3, memoria)
            memoria[numero] = nesimo_termo
            return nesimo_termo
    else:
        return memoria[numero]

def main():
    n = int(input())
    nesimo_fibonacci3 = fibonacci3(n, dict())
    print(nesimo_fibonacci3)

main()