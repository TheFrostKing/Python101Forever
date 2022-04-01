from enum import Enum

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3
 

def increasing_or_decreasing(ns):
    length = len(ns)

    if length <= 1:
        return Monotonicity.NONE

    increasing = True
    decreasing = True

    for index in range(length - 1):

        a = ns[index]
        b = ns[index + 1]
    
        increasing = increasing and a < b
        decreasing = decreasing and a > b 


    if decreasing:

        return Monotonicity.DECREASING

    if increasing:

        return Monotonicity.INCREASING

    else:
        return Monotonicity.NONE

tests = [   
    ([1,  2, 3, 4, 5], Monotonicity.INCREASING),
    ([5,  6, -10], Monotonicity.NONE),
    ([1,  1, 1, 1], Monotonicity.NONE),
    ([9,  8, 7, 6], Monotonicity.DECREASING),
    ([],  Monotonicity.NONE),
    ([1],  Monotonicity.NONE),
    ([1,  100], Monotonicity.INCREASING),
    ([1,  100, 100], Monotonicity.NONE),
    ([100,  1], Monotonicity.DECREASING),
    ([100,  1, 1], Monotonicity.NONE),
    ([100,  1, 2], Monotonicity.NONE),
]


for ns, expected in tests:
    result = increasing_or_decreasing(ns)
    print(result == expected)
