from agenda import ler_dados_argumentos, listar_eventos, remover_evento

def main():
    agenda = [
    {'identificador': 1, 'nome': 'F129 - lab', 'descricao': 'Aula de física experimental', 'data': '06/07/2020', 'hora': '10:00'},
    {'identificador': 2, 'nome': 'F128', 'descricao': 'Aula de física', 'data': '06/07/2020', 'hora': '08:00'},
    {'identificador': 3, 'nome': 'MC102', 'descricao': 'Aula de algoritmos', 'data': '13/07/2020', 'hora': "12:00"}
    ]
    
    #nome, acao, info = ler_dados_argumentos()
    listar_eventos(agenda, {'data': '13/07/2020'})
    #print(nome)
    #print(acao)
    print(agenda)
    remover_evento(agenda, {'identificador': 1})
    print(agenda)

main()