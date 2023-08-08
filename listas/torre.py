for i in range(1, 11):
    for j in range(10-i):
        print(" ", end="")
    for j in range(2*i):
        print("*", end="")
    for j in range(10-i):
        print(" ", end="")
    print()