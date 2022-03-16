def str_reverse(s):
    return ''.join(reversed(s))

def is_paledrome(x):
    x = str(x)

    return x == str_reverse(x)

def palindromes_count(n):
    result = 0
    for num in range(10, n+1):
        if is_paledrome(num):
            result += 1

    return result




tests = [
    (10, 0),
    (20, 1),
    (30, 2),
    (101, 10),
    (200, 19),
    (43539, 525),
    (4247, 132),
    (48877, 577),
    (94012, 1029),
    (62560, 715),
    (92009, 1009),
    (63176, 721),
    (67409, 763),
    (62834, 718),
    (77420, 863),
    (99999, 1089),
]


for n, expected in tests:
    result = palindromes_count(n)

    print(result == expected)