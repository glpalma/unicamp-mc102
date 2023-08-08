def receber_sequencia_numeros():
    """Recebe como entrada uma sequência de números
    separados por espaço e a transforma em uma lista."""
    sequencia = input().split()
    return sequencia

def eh_primo(n):
    """Verifica se n é primo."""
    eh_primo = True
    if n == 1 or n == 0:
        return False
    for d in range(2, n):
        if n % d == 0:
            eh_primo = False
            break
    return eh_primo

def converter_str_int(lista):
    """Converte os itens de uma lista fornecida 
    de string para inteiro."""
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista

def filtra(lista, funcao):
    """Filtra uma lista de itens usando uma função
    fornecida como filtro."""
    filtrados = []
    for valor in lista:
        if funcao(valor):
            filtrados.append(valor)
    return filtrados

def mapeia(lista):
    """Aplica uma determinada operação sobre os itens
    de uma lista e devolve outra com tais itens."""
    mapeados = []
    for i in range(len(lista)):
        mapeados.append(lista[i]**2)
    return mapeados

def reduz(lista):
    """Acumula os valores de uma lista de forma que
    devolve apenas um valor."""
    soma = 0
    for valor in lista:
        soma += valor
    return soma

def main():
    sequencia = converter_str_int(receber_sequencia_numeros())
    primos = filtra(sequencia, eh_primo)
    quadrados_primos = mapeia(primos)
    soma = reduz(quadrados_primos)
    print(soma)

main()