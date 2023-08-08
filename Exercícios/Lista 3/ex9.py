def is_divisible(up, down):
    if up % down == 0:
        return "YES!"
    else:
        return "NO! :("

def main():
    n = int(input())
    for i in range(2, n + 1):
        print(i, is_divisible(n, i))

main()