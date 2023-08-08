"""
RASCUNHO
ler notas das provas #split
ler notas dos exercícios

normalizar_lista(lista): #função
    achar o maior valor da lista: x
    para todos os itens da lista:
        divida por x multiplique por 10
        atualize o valor na lista 

calcular média final
    para cada valor com o mesmo índice nas duas listas
        faça média GEOMÉTRICA
        adicione essa média em outra lista
        (já com as médias calculadas)

"""
import math

def obter_maximo(lista):
    """Devolve o valor máximo da lista fornecida."""
    assert lista, "A lista não pode ser vazia."
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero 
    return maximo

def converter_str_float(lista):
    """Converte os itens de uma lista fornecida 
    de string para float."""
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    return lista

def normalizar_lista(lista):
    """Normaliza cada item da lista fornecida 
    de acordo com o valor máximo dela."""
    for i in range(len(lista)):
        lista[i] = (lista[i]/obter_maximo(lista))*10
    return lista

def calcular_media_geometrica(provas, exercicios):
    """Calcula a média geométrica das notas com o 
    mesmo índice de duas listas diferentes."""
    exercicios = converter_str_float(exercicios)
    medias = []
    for i in range(len(provas)):
        media = math.sqrt(provas[i]*exercicios[i])
        medias.append(media)
    return medias

def main():
    provas = input().split()
    exercicios = input().split()

    assert len(provas) == len(exercicios), \
        "As listas de notas devem ter o mesmo tamanho."

    provas = converter_str_float(provas)
    exercicios = converter_str_float(exercicios)

    provas = normalizar_lista(provas)
    exercicios = normalizar_lista(exercicios)
    
    print(calcular_media_geometrica(provas, exercicios))
    
main()