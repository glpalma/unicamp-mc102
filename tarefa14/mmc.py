def maior_menor2(a, b):
    """Devolve o maior e menor entre
    dois valores."""

    if a > b:
        maior = a
        menor = b
    elif a < b:
        maior = b
        menor = a

    return maior, menor

def mdc(a, b):
    """Devolve o MDC dos números a e b."""
    maior, menor = maior_menor2(a, b)
    resto = maior % menor
        
    if resto == 0:
        return menor
    else:
        return mdc(menor, resto)

def mmc(a, b):
    """Devolve o MMC dos números a e b."""

    return (a * b)//mdc(a, b)

def main():
    a, b = input().split()
    a, b = int(a), int(b)
    mmc_ab = mmc(a, b)
    print(mmc_ab)

main()