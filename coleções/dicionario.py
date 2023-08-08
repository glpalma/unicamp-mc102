def procurar_indice(dicionario, palavra):
    """devolve o índice correspondente à palavra
    ou None se ela não existir no dicionário"""

    for i, verbete in enumerate(dicionario):
        if verbete[0] == palavra:
            return i
    return None

def atualizar_definicao(dicionario, palavra, nova_definicao):
    """atualiza a definição de uma palavra"""

    i = procurar_indice(dicionario, palavra)
    verbete_antigo = dicionario[i]
    verbete_novo = (verbete_antigo[0], nova_definicao, verbete_antigo[2])
    dicionario[i] = verbete_novo

def adicionar_verbete(dicionario, verbete):
    """adiciona um novo verbete ao dicionário"""

    i = procurar_indice(dicionario, verbete[0])
    if i is None:
        dicionario.append(verbete)
    else:
        raise Exception(f"Palavra {verbete[0]} já existe.")

def criar_dicionario():
    """cria um dicionário vazio"""

    return []

def procurar_verbete(dicionario, palavra):
    """devolve o verbete correspondente à palavra;
    se palavra não for encontrada, devolve None"""

    for verbete in dicionario:
        if verbete[0] == palavra:
            return verbete
    return None

def remover_verbete(dicionario, palavra):
    """Remove a palavra fornecida como argumento do dicionário."""
    i = procurar_indice(dicionario, palavra)

    if i is None:
        raise Exception(f"A palavra {palavra} não existe no dicionário fornecido.")
    else:
        dicionario.pop(i)
        

def main():
    dicionario = criar_dicionario()

    verbete = ("amor", "fogo que arde sem se ver", 1595)
    adicionar_verbete(dicionario, verbete)

    remover_verbete(dicionario, "amor")

    outro = ("amor", "é sofrer amargamente", 2020)
    adicionar_verbete(dicionario, outro)

    palavra, definicao, _ = procurar_verbete(dicionario, "amor")
    print(f"{palavra} significa {definicao}")

main()
