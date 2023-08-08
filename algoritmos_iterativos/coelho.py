"""
def tempo_gasto_tartaruga():
    numero_passos = 0
    distancia = 0.0
    proximo_passo = 1
    pass
"""

def tempo_gasto_coelho():
    numero_saltos = 0
    distancia_percorrida = 0.0
    proximo_salto = 1.0

    while distancia_percorrida < 2.0:
        numero_saltos += 1
        distancia_percorrida += proximo_salto
        proximo_salto = proximo_salto / 2
    
    return numero_saltos

def main():
    tempo = tempo_gasto_coelho()
    print(f"O coelho gasta {tempo} minutos.")