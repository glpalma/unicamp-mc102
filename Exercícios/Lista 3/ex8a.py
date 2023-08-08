def somatorio_numeros(numero):
    soma = 0
    for n in range(1, numero + 1):
        soma += n

    return soma

def soma_PA(a1, an, n):
    return int((a1 + an) * n/2)

def main():
    n = int(input())
    soma = somatorio_numeros(n)
    soma = soma_PA(1, n, n) # <-- bem mais rápido
    print(soma)

main()