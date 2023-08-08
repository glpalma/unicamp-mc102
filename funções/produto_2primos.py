def eh_primo(n):
    """Verifica se n é primo."""
    
    eh_primo = True
    for d in range(2, n):
        if n % d == 0:
            eh_primo = False
            break
    return eh_primo

def eh_produto_dois_primos(n):
    """Devolve True se o argumento n puder
    ser escrito como um produto de dois primos"""

    produto_primos = False
    for q in range(1, n + 1):
        if n % q == 0:
            r = n // q
            if r == q:
                break
            elif eh_primo(r) and eh_primo(q):
                produto_primos = True
                break

    return produto_primos

def main():
    n = int(input("Digite um número inteiro: "))
    if eh_produto_dois_primos(n): #implica que a função devolve um valor booleano
        print(f"O número {n} é produto de dois primos.")
    else: 
        print(f"O número {n} não é produto de dois primos.")

main()