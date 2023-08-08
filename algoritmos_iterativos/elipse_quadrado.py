LADO = 10

def desenhar_quadrado():
    for i in range(LADO):
        for _ in range(LADO):
            print("*", end="")
            print(" ", end="")
        print()

def esta_elipse(a, b, i, j):
    if ((i/a)**2) + ((j/b)**2) <= 1:
        return True
    else:
        return False

def desenhar_elipse():
    tamanho_a = 25
    tamanho_b = 50
    for i in range(-tamanho_a, tamanho_a+1):
        for j in range(-tamanho_b, tamanho_b+1):
            if esta_elipse(tamanho_a, tamanho_b, i, j):
                print("* ", end="")
            else:
                print("  ", end="")
        print()

desenhar_elipse()