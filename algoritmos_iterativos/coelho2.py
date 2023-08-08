def tempo_coelho():
    numero_passos = 0
    distancia = 0.0
    proximo_salto = 1
    while distancia < 2:
        distancia += 1/proximo_salto
        proximo_salto *= 2
        numero_passos += 1
    return numero_passos

def tempo_tartaruga():
    numero_passos = 0
    distancia = 0.0
    contador = 1
    while distancia < 22:
        distancia += 1/contador
        contador += 1
        numero_passos += 1
        if numero_passos % 1000000 == 0:
            print(distancia)
    return numero_passos

def main():
    print(f"O coelho demora {tempo_coelho()} minutos.")
    print(f"A tartaruga demora {tempo_tartaruga()} minutos.")

main()
