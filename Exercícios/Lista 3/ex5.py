def tiktok(n):
    """Imprime "tik" se o número for divisível por 3
    e "tok" se for divisível por 5."""

    if n % 3 == 0:
        print('tik')
    elif n % 5 == 0:
        print('tok')

def main():
    n = int(input())

    for i in range(1, n + 1):
        tiktok(i)
        
main()