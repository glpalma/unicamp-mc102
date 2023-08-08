def ler_num_trabalhos_e_pesos():
    """Lê os números de trabalhos a serem feitos e os
    pesos de cada um."""
    pesos_trabalhos = []
    
    while True:
        try:
            num_trabalhos = int(input().strip())
            lista_pesos = input().strip().split()
            assert num_trabalhos == len(lista_pesos)

            pesos_trabalhos.append(lista_pesos)
        except EOFError:
            break

    return pesos_trabalhos

def soma_pesos(pesos):
    """Devolve a soma de todos os pesos de uma lista."""
    soma = 0

    for peso in pesos:
        soma += int(peso)
    
    return soma

def menor_valor(lista):
    """Devolve o menor valor de uma lista fornecida."""
    menor_valor = lista[0]

    for valor in lista:
        if valor < menor_valor:
            menor_valor = valor

    return menor_valor

def calcular_diferencas_pesos(pesos):
    """Devolve uma lista com as diferenças do grau de
    dificuldade de várias tarefas divididas entre 2 alunos."""
    diferencas = []
    
    for lista_pesos in pesos:
        gugu = soma_pesos(lista_pesos)
        rangel = 0
        lista_diferencas = []
        for peso in lista_pesos:
            diferenca = abs(gugu - rangel)
            lista_diferencas.append(diferenca)
            rangel += int(peso)
            gugu -= int(peso)

        menor_diferenca = menor_valor(lista_diferencas)
        diferencas.append(menor_diferenca)

    return diferencas

def mostrar_diferencas_pesos(diferencas):
    """Mostra as diferenças entre os graus de dificuldade
    atrelados para cada aluno."""

    for diferenca in diferencas:
        print(diferenca)

def main():
    pesos_trabalhos = ler_num_trabalhos_e_pesos()
    diferencas = calcular_diferencas_pesos(pesos_trabalhos)
    mostrar_diferencas_pesos(diferencas)

if __name__ == "__main__":
    main()