def triangulo(n):
    m = 2*n + 1
    for i in range(n):
        e = m//2 - i
        j = 2*i + 1
        print(e*" ", end="")
        print(j*"*", end="")
        print()
        
def main():
    n = int(input("Altura: "))
    triangulo(n)

main()