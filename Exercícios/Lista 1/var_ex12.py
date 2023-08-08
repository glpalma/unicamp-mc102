"""
Entrada: número inteiro de segundos 
Saída: A duração do evento foi de {} horas, {} minutos e {} segundos.
"""
t = int(input("Segundos: "))
minutos = 0
horas = 0
segundos = 0

if t < 60: # menor que um minuto
    print(f"A duração do evento foi de {t} segundos.")
elif t >= 60:
    for _ in range(t // 60):
        minutos += 1 # contagem de minutos
    if minutos < 60:
        segundos = t % 60 # atribui o resto que não entrou nos minutos aos segundos
        print(f"A duração do evento foi de {minutos} minutos e {segundos} segundos.")
    elif minutos >= 60: #contagem de horas
        for i in range(minutos // 60):
            horas += 1
        minutos = minutos - (horas * 60)
        segundos = (t - (horas * 3600) - (minutos * 60))
        print(f"A duração do evento foi de {horas} hora(s), {minutos} minutos e {segundos} segundos.")