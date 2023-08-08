def eh_capicuia(n):
    """Devolve True se o número n for capicuia."""
    n = str(n)
    iterador = len(n) // 2

    for i in range(iterador):
        if n[i] != n[-i - 1]:
            return False

    return True

def main():
    n = input('Digite um número: ')
    if eh_capicuia(n):
        print('O número é um capicuia.')
    else:
        print('O número não é um capicuia.')
      
main()