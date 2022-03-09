import math

def fact(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result   

def fact_digits(n):
    n_list = []
    result = 0
    for digit in str(abs(n)):
        n_list.append(int(digit))

    for num in n_list:
        result += fact(num)
    return result

    # Solution with math library
    # for num in n_list:  
    #     result += (math.factorial(num))
    # return result

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