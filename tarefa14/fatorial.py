def fatorial(numero):
    """Devolve o fatorial de um número."""

    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

def main():
    numero = int(input())
    fat = fatorial(numero)
    print(fat)

