def sum_of_digits(n):
    n_list = []
    for digit in str(abs(n)):
        n_list.append(int(digit))

    result = sum(n_list)
    return result




tests = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1)
]

for n, expected in tests:
    result = sum_of_digits(n)
    # print(f"'{expected}', '{result}'")
    # print(expected, result)
    print(result == expected)