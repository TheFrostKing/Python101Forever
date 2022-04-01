def is_prime(n):
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return n

def goldbach(n):
    result = []
    used_num = set()  

    if n % 2 == 1 and n <= 2:
        return

    primes = [x for x in range(2, n) if is_prime(x)]

    for a in primes:
        for b in primes:
            if a + b == n:
                pair = (a, b)
                reversed_pair = (b, a)

                if pair not in used_num and reversed_pair not in used_num:
                    result.append(pair)
                    used_num.add(pair)
    return result


tests = [
    (4, [(2, 2)]),
    (6, [(3, 3)]),
    (8, [(3, 5)]),
    (10, [(3, 7), (5, 5)]),
    (100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
    (5, None)
]

for n, expected in tests:
    result = goldbach(n)

    print(result == expected, result)