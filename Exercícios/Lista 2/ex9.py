entrada = input().split()
n = len(entrada)

if entrada[0] == entrada[-1] or entrada[0] == entrada[1]:
    print("Os números têm que ser distintos entre si.")

for i in range(n-1):
    for j in range(n-1):
        if entrada[j] > entrada[j+1]:
            aux = entrada[j]
            entrada[j] = entrada[j+1]
            entrada[j+1] = aux

print(" ".join(entrada))