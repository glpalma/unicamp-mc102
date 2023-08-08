# Conversão de idade em dias

anos, meses, dias = input().split()

anos = int(anos)
meses = int(meses)
dias = int(dias)

dias_anos = 365 * anos
dias_meses = 30 * meses
total = dias + dias_anos + dias_meses
print(total)