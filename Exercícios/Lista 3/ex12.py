def is_prime(n):
    """Returns True if n is prime."""
    is_prime = True
    if n == 1 or n == 0:
        return False
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    return is_prime

def before_after_primes(n):
    """Returns the prime numbers that come after and
    before n (n included if prime)."""
    last_prime = 2
    next_prime = 3

    for number in range(2*n):
        if is_prime(number) and number <= n:
            last_prime = number
        elif is_prime(number) and number >= n:
            next_prime = number
            break

    return last_prime, next_prime

def main():
    n = int(input())
    last_prime, next_prime = before_after_primes(n)
    print(last_prime, next_prime)

main()