"""
Programa que recebe um número
inteiro e decide se ele é um 
produto de dois primos.

Entrada: número n
para cada núm q = 2, 3, ..., n-1:
    se n é divisível por q:
        r <-- n / q
        verifique se q é primo 
        verifique se r é primo 
        se ambos forem, responda SIM
se não encontrei, responda NÃO 
"""
# FIXME: o código ainda não está funcionando 
def eh_primo(numero):
    encontrei_divisor = False
    for i in range(2, numero):
        if numero % i == 0:
            encontrei_divisor = True
            break

    if not encontrei_divisor and numero > 1:
        numero_eh_primo: True
    else:
        numero_eh_primo: False
    return numero_eh_primo

def eh_composto_especial(n):
    composto_especial = False
    for q in range(2, n):
        if n % q == 0:
            r = n  // q
            if eh_primo(r) and eh_primo(q):
                composto_especial = True
                break
    return composto_especial
    
def main():
    n = int(input())
    if eh_composto_especial(n):
        print(f"{n} é produto de dois primos.")
    else: 
        print(f"{n} não é produto de dois primos.")

main()

"""

composto_especial = False

for q in range(2, n):
    if n % q == 0:
        r = n  // q

        # verificando se q é primo
        encontrei_divisor = False
        for i in range(2, q):
            if q % i == 0:
                encontrei_divisor = True
                break

        if not encontrei_divisor and q > 1:
            q_eh_primo: True
        else:
            q_eh_primo: False


        # verificando se r é primo
        encontrei_divisor = False
        for i in range(2, r):
            if r % i == 0:
                encontrei_divisor = True
                break

        if not encontrei_divisor and r > 1:
            r_eh_primo = True
        else:
            r_eh_primo = False

        if r_eh_primo and q_eh_primo:
            composto_especial = True
            break

        if eh_primo(r) and eh_primo(q):
            composto_especial = True
            break



if composto_especial:
    print(f"{n} é produto de dois primos.")
else: 
    print(f"{n} não é produto de dois primos.")

"""