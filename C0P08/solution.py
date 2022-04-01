from itertools import count


def group(items):

    length = len(items)
    result = []
    counter = 1

    for x in range(length - 1):

        if items[x] == items[x+1]:
            counter += 1
            
        else:
            result.append([for i in range(counter)])
            counter = 0

    return result


tests = [
    ([1, 1, 1, 2, 3, 1, 1], [[1, 1, 1], [2], [3], [1, 1]]),
    ([1, 2, 1, 2, 3, 3], [[1], [2], [1], [2], [3, 3]]),
    ([], []),
    ([1], [[1]]),
    ([1, 1, 1, 1], [[1, 1, 1, 1]]),
    ([1, 2, 3, 4], [[1], [2], [3], [4]])
]

for items, expected in tests:
    result = group(items)
    print(result)
    print(result == expected)
