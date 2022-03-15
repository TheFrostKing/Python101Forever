def group(items):

    index = 0
    length = len(items)
    result = []

    while index < length:

        item = items[index] # suzdavame promenliva da pazi razmera na spisuka
        current_group = [item] # suzdava spisuk ot suotvetniq element

        lookup_index = index + 1 #sledvashtiq index

        while lookup_index < length and items[lookup_index] == item: # proverqva dali spisuka ot suotvetniq element suvpada s tozi s index + 1 (items[lookup_index] )

                current_group.append(items[lookup_index]) #vkarvame index + 1 == index v spisuk
                lookup_index += 1

        result.append(current_group) # vkarvame spisuk s elementite v result

        index = lookup_index # uvelichavame index + 1 

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

    print(result == expected) 
