def ler_informacoes_entrada():
    """Lê as informações de nota e de frequência
    a partir do teclado."""
    tarefas = input().strip().split()
    frequencia = []
    while True:
        try:
            aula = input().strip()
            frequencia.append(aula)
        except EOFError:
            break

    return tarefas, frequencia
        
def verificar_notas(tarefas):
    """Devolve True se o aluno cumpriu os requisitos
    mínimos de nota na matéria; caso contrário,
    devolve False."""
    cumpriu_requisitos = True
    for nota_tarefa in range(1, len(tarefas), 2):
        if tarefas[nota_tarefa] == "D":
            cumpriu_requisitos = False

    return cumpriu_requisitos

def verificar_frequencia(frequencia):
    """Devolve True se o aluno cumpriu os requisitos
    mínimos de frequência na matéria; caso contrário,
    devolve False."""
    numero_aulas = len(frequencia)
    numero_presencas = 0.0

    for aula in frequencia:
        if aula == "presente":
            numero_presencas += 1
    taxa = numero_presencas/numero_aulas
    cumpriu_requisitos = False
    if taxa >= 0.75:
        cumpriu_requisitos = True

    return cumpriu_requisitos
        
def mostrar_resultado(notas, frequencia):
    """Mostra "Aprovadx" se x alunx tiver cumprido
    os requisitios mínimos de nota e de frequência;
    caso contrário, mostra "Reprovadx"."""
    if notas and frequencia:
        print("Aprovadx")
    else:
        print("Reprovadx")

def main():
    tarefas, frequencia = ler_informacoes_entrada()
    notas = verificar_notas(tarefas)
    frequencia = verificar_frequencia(frequencia)
    mostrar_resultado(notas, frequencia)
    
main()