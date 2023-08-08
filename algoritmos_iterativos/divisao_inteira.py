def divisao_inteira(dividendo, divisor):
    residuo = dividendo
    contador = 0
    while residuo >= divisor:
        residuo = residuo - divisor
        contador += 1
    return contador

print(divisao_inteira(11, 2))