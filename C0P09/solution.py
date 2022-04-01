def make_list(num):
    result = []

    for x in str(num):

        result.append(int(x))

    return result

def is_credit_card_valid(number):
    result = []
    digits = make_list(number)
    length = len(make_list(number))

    isDouble = False

    for index in range(length - 1, -1, -1):
        multiplier = 1 

        if isDouble:
            multiplier = 2

        my_sum = sum(make_list(digits[index]) * multiplier)

        result.append(my_sum)

        isDouble = not isDouble

    return sum(result) % 10 == 0


tests = [
    (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    (79927398715, False),
    (79927398710, False),
    (79927398711, False),
    (79927398712, False),
    (79927398714, False),
    (79927398715, False),
    (79927398716, False),
    (79927398717, False),
    (79927398718, False),
    (79927398719, False)
]


for number, expected in tests:
    result = is_credit_card_valid(number)

    print(result == expected)