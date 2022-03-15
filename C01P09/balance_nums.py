def is_number_balanced(number):

    number_holder = []
    sum_left = 0
    sum_right = 0

    for digit in str(number):
            number_holder.append(int(digit))
            
    if len(number_holder) == 1:
        return True
    print(len(number_holder))
    length = len(number_holder)
    if length % 2 == 0:

        for n in range(len(number_holder)):

            if n < len(number_holder)/2:

                sum_left += number_holder[n]

            else:
                sum_right += number_holder[n]

    if length % 2!= 0:
        make_even = round(length/2)
        number_holder.remove(number_holder[make_even-1])
        for n in range(len(number_holder)):
            
            if n < len(number_holder)/2:
                sum_left += number_holder[n]

            else:
                sum_right += number_holder[n]

    number_holder.clear()

    if sum_right == sum_left:
        return True

    else:
        return False
    

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