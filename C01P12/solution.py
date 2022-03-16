def make_list(number):
    digits = []

    for x in str(number):
        digits.append(int(x))
    
    return digits

def is_credit_card_valid(number):
    result = 0
    counter = 0
    double = 0

    for n in make_list(number):
        counter += 1
        my_sum = 0
        
        if counter == 2:

            double = n*2
            counter = 0
            puti+=1

            if double >= 10:
                for x in str(double):
                    my_sum += int(x)
            else:
                my_sum += double
            

        else:
            my_sum += n
        

        result += my_sum

    return result % 10 == 0

tests = [
    # (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    # (79927398715, False),
    # (79927398710, False),
    # (79927398711, False),
    # (79927398712, False),
    # (79927398714, False),
    # (79927398715, False),
    # (79927398716, False),
    # (79927398717, False),
    # (79927398718, False),
    # (79927398719, False)
]


for number, expected in tests:
    result = is_credit_card_valid(number)

    print(result == expected)