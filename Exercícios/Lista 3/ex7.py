def potencia(a, b):
    produto = 1
    for _ in range(b):
        produto *= a

    return produto

def main():
    a, b = input("Digite a e b: ").strip().split()
    print(potencia(int(a), int(b)))

main()