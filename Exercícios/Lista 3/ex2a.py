from ex2b import fibonacci

def main():
    n = int(input('Digite o número de meses: '))
    n_parelhas = fibonacci(n)
    if n == 1:
        print(f'No {n}º mês, os coelhos terão {n_parelhas} parelha de filhotes.')
    else:
        print(f'No {n}º mês, os coelhos terão {n_parelhas} parelhas de filhotes.')

main()