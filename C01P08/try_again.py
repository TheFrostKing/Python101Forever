def group(items):

    index = 0 
    length = len(items)
    result = []

    while index < length: 
        item = items[index]
        group_current = [item]

        next_item_index = index + 1

        while next_item_index < length and items[index] == items[next_item_index]:
            group_current.append(items[next_item_index])
            next_item_index += 1

        result.append(group_current)
        index = next_item_index

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
