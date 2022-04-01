def is_prime(n)
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True

def next_prime(n):
    n += 1
        while not is_prime(n)
        n += 1

    return n

def prime_factorization(n):
    result = []
    p = 2
    a = 0

    while n!= 1:
        while n % p == 0:
            a += 1
            n = n // p   # 10//5 == 2

        if a > 0: 
            result.append((p, a))

        a = 0
        p = next_prime

    return result





tests = [
    (2, [(2, 1)]),
    (4, [(2, 2)]),
    (10, [(2, 1), (5, 1)]),  # This is 2^1 * 5^1
    (14, [(2, 1), (7, 1)]),
    (356, [(2, 2), (89, 1)]),
    (89, [(89, 1)]),  # 89 is a prime number
    (1000, [(2, 3), (5, 3)])
]


for n, expected in tests:
    result = prime_factorization(n)

    print(result == expected, result)