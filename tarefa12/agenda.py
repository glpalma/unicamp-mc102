import sys, argparse

def ler_dados_argumentos():
    """Devolve o nome da agenda, a ação a ser executada
    e um dicionário com osdados fornecidos na linha de comando."""
    argumentos = sys.argv
    assert argumentos[1] == "-a", "Ação básica de alteração não foi fornecida."

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', help="Indicador de mudança da agenda (obrigatório). Deve ser seguido pelo nome do arquivo da agenda.")
    parser.add_argument('acao', help="Ação a ser executada sobre a agenda.", type=str)
    parser.add_argument('--evento', help="Número identificador do evento na agenda.", type=int)
    parser.add_argument('--nome', help="Nome do evento.", type=str)
    parser.add_argument('--descricao', help="Descrição do evento.", type=str)
    parser.add_argument('--data', help="Data de acontecimento do evento.", type=str)
    parser.add_argument('--hora', help="Horário de acontecimento do evento.", type=str)
    args = parser.parse_args()

    info_evento = {"identificador": args.evento, "nome": args.nome,
              "descricao": args.descricao, "data": args.data, "hora": args.hora}
    nome_agenda = args.a

    return nome_agenda, args.acao, info_evento

def inicializar_agenda(nome_agenda):
    """Cria o arquivo CSV usado para armazenar
    os dados da agenda."""
    with open(nome_agenda, "w") as _:
        print(f"Uma agenda com o nome '{nome_agenda}' foi criada!")

def ler_agenda(nome_agenda):
    """Devolve uma lista de dicionários com as
    informações dos eventos."""
    agenda = []

    with open(nome_agenda) as arquivo_agenda:
        for linha in arquivo_agenda:
            identificador, nome, descricao, data, hora = linha.split(",")
            info_evento = {"identificador": int(identificador), "nome": nome, "descricao": descricao, "data": data, "hora": hora.strip()}
            agenda.append(info_evento)

    return agenda

def criar_evento(agenda, info_evento):
    """Cria um evento na agenda."""
    m = len(agenda)

    if not agenda:
        identificador = 1
    else:
        identificador = m + 1
    
    info_evento["identificador"] = identificador
    agenda.append(info_evento)

def devolver_identificador(evento):
    """Devolve o identificador que representa o
    evento na agenda."""
    return evento["identificador"]

def listar_eventos(agenda, info_evento):
    """Lista os eventos da agenta em ordem de
    anotação."""
    data = info_evento["data"]
    nenhum_evento = True
    agenda.sort(key=devolver_identificador)
    mostrou_eventos_dia = False

    for evento in agenda:
        identificador_evento = evento["identificador"]
        nome_evento = evento["nome"]
        descricao_evento = evento["descricao"]
        data_evento = evento["data"]
        hora_evento = evento["hora"]
        if data == data_evento:
            if not mostrou_eventos_dia:
                print(f'Eventos do dia {data_evento}')
                mostrou_eventos_dia = True
            nenhum_evento = False
            print(47*"-")
            print(f'Evento {identificador_evento} - {nome_evento}')
            print(f'Descrição: {descricao_evento}')
            print(f'Data: {data_evento}')
            print(f'Hora: {hora_evento}')
        if mostrou_eventos_dia and evento == agenda[-1]:
            print(47*"-")
    if nenhum_evento:
        print(f"Não existem eventos para o dia {data}!")


def alterar_evento(agenda, info_evento):
    """Altera os dados de um evento."""
    identificador_usuario = info_evento['identificador']
    assert identificador_usuario is not None, 'Um número de identificador deve ser fornecido.'
    achou_evento = False

    for evento in agenda:
        if evento['identificador'] == identificador_usuario:
            evento_selecionado = evento
            achou_evento = True
        
    if not achou_evento:
        print('Nenhum evento com esse identificador foi encontrado.')
        return

    for informacao in info_evento:
        if info_evento[informacao] is not None:
            evento_selecionado[informacao] = info_evento[informacao]

    print(f'O evento {identificador_usuario} foi alterado com sucesso!')

def remover_evento(agenda, info_evento):
    """Remove um evento da agenda."""
    identificador_usuario = info_evento['identificador']

    for indice, evento in enumerate(agenda):
        if evento['identificador'] == identificador_usuario:
            idx_evento = indice
        elif int(evento['identificador']) > identificador_usuario:
                evento['identificador'] -= 1
    agenda.pop(idx_evento)

def salvar_agenda(agenda, nome_agenda):
    """Armazena as mudanças
    efetuadas na agenda."""

    with open(nome_agenda, 'w') as arquivo_agenda:
        for evento in agenda:
            evento_lista = [str(evento['identificador']), evento['nome'],
            evento['descricao'], evento['data'], evento['hora']]
            print(','.join(evento_lista).strip(), file=arquivo_agenda)
            
def main():
    nome_agenda, acao, info_evento = ler_dados_argumentos()

    if acao == "inicializar":
        inicializar_agenda(nome_agenda)

    try:
        agenda = ler_agenda(nome_agenda)
    except ValueError:
        agenda = []

    if acao == "criar":
        criar_evento(agenda, info_evento)
    elif acao == "alterar":
        alterar_evento(agenda, info_evento)
    elif acao == "remover":
        remover_evento(agenda, info_evento)
    elif acao == "listar":
        listar_eventos(agenda, info_evento)

    salvar_agenda(agenda, nome_agenda)

if __name__ == "__main__":
    main()