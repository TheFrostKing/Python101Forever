
def make_list_of_digits(n):
    result = []
    for digit in str(n):
        result.append(int(digit))

    return result

def is_number_balanced(number):
    sum_left = 0
    sum_right = 0

    list_digits = make_list_of_digits(number)
    length = len(list_digits)
    middle = length // 2

    is_length_odd = length % 2 == 1

    for index, digit in enumerate(list_digits):

        if index < middle:
            sum_left += digit

        else:
            if index == middle and is_length_odd:
                continue

            sum_right += digit

    return sum_right == sum_left




tests = [
    (9, True),
    (4518, True),
    (1111, True),
    (11111, True),
    (28471, False),
    (1238033, True),
    (123, False),
    (121, True),
]


for n, expected in tests:
    result = is_number_balanced(n)
    
    print(result == expected)