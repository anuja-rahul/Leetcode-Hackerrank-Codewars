import math


def is_prime(n):
    if n % 10000 == 0:
        print(n)
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


primes = [p for p in range(2, 2000000) if is_prime(p)]
print(primes[0])
print(sum(primes))
