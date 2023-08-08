def ler_entrada():
    """Lê um valor de ponto flutuante N."""
    n = float(input())

    return n

def calcular_min_notas_moedas(valor):
    """Devolve um dict() com o número de notas
    e moedas necessário para compor o valor
    de dinheiro fornecido."""
    num_notas = {'100.00': 0, '50.00': 0, '20.00': 0, '5.00': 0, '2.00': 0}
    num_moedas = {'1.00': 0, '0.50': 0, '0.25': 0, '0.10': 0, '0.05': 0, '0.01': 0}

    while valor > 10e-3:
        if valor >= 100:
            num_notas['100.00'] += 1
            valor -= 100
        elif valor >= 50:
            num_notas['50.00'] += 1
            valor -= 50
        elif valor >= 20:
            num_notas['20.00'] += 1
            valor -= 20
        elif valor >= 5:
            num_notas['5.00'] += 1
            valor -= 5
        elif valor >= 2:
            num_notas['2.00'] += 1
            valor -= 2
        elif valor >= 1:
            num_moedas['1.00'] += 1
            valor -= 1
        elif valor >= 0.5:
            num_moedas['0.50'] += 1
            valor -= 0.5
        elif valor >= 0.25:
            num_moedas['0.25'] += 1
            valor -= 0.25
        elif valor >= 0.10:
            num_moedas['0.10'] += 1
            valor -= 0.10
        elif valor >= 0.05:
            num_moedas['0.05'] += 1
            valor -= 0.05
        elif valor >= 0.01:
            num_moedas['0.01'] += 1
            valor -= 0.01

    return num_notas, num_moedas

def mostrar_num_notas_moedas(num_notas, num_moedas):
    """Exibe o número de notas e moedas necessário
    para compor um valor N de dinheiro."""

    existem_notas = False
    for valor_nota in num_notas:
        if num_notas[valor_nota] > 0:
            existem_notas = True
            break

    if existem_notas:
        print("NOTAS:")
        for valor_nota in num_notas:
            if num_notas[valor_nota] > 0:
                print(f"{num_notas[valor_nota]} nota(s) de R$ {valor_nota}")

    existem_moedas = False
    for valor_moeda in num_moedas:
        if num_moedas[valor_moeda] > 0:
            existem_moedas = True
            break

    if existem_moedas:
        print("MOEDAS:")
        for valor_moeda in num_moedas:
            if num_moedas[valor_moeda] > 0:
                print(f"{num_moedas[valor_moeda]} moeda(s) de R$ {valor_moeda}")
   

def main():
    valor_N = ler_entrada()
    num_notas, num_moedas = calcular_min_notas_moedas(valor_N) #dict
    mostrar_num_notas_moedas(num_notas, num_moedas)

if __name__ == "__main__":
    main()