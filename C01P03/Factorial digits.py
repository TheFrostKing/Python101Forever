import math
def fact_digits(n):
    n_list = []
    result = 0
    for digit in str(abs(n)):
        n_list.append(int(digit))

    for num in n_list:
        result += (math.factorial(num))

    return result




tests = [
    (101, 3),
    (111, 3),
    (145, 145),
    (999, 1088640)
]

for n, expected in tests:
    result = fact_digits(n)
    # print(f"'{expected}', '{result}'")
    # print(expected, result)
    print(result == expected)