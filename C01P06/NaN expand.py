def nan_expand(times):
    result = 0
    nan = "NaN"
    expanded = "Not a "
    if times == 0:
        return ""
    else:
        result = expanded*times+nan
    return result

tests = [
    (0, ""),
    (1, "Not a NaN"),
    (2, "Not a Not a NaN"),
    (3, "Not a Not a Not a NaN")
]

for times, expected in tests:
    result = nan_expand(times)
    # print(f"'{expected}', '{result}'")
    # print(expected, result)
    print(result == expected)