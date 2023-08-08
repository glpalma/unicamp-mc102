"""
Calcula os valores máximos de duas listas
e devolve o produto deles.
"""
def ler_lista_numeros():
        n = int(input())
        lista = []
        for _ in range(n): #underline é usada no lugar de uma variável para indicar que ela não importa
            numero = int(input)
            lista.append(numero)
    return lista

def obter_maximo(lista):
        maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

def obter_produto_maximos(lista1, lista2):
    maximo1 = obter_maximo(lista1)
    maximo2 = obter_maximo(lista2)
    produto = maximo1 * maximo2
    return produto

def main():
    print("Digite uma lista de números:")
    lista1 = ler_lista_numeros()
    print("Digite uma lista de números:")
    lista2 = ler_lista_numeros()
    produto = obter_produto_maximos(lista1, lista2)
    print(produto)

main()