def anagrams(word1, word2):
    word1_list  = word1.lower().replace(' ', '')
    word2_list  = word2.lower().replace(' ', '')

    return sorted(word2_list) == sorted(word1_list)

tests = [
    (("silent", "listen"), True),
    (("SILENT", "listen"), True),
    (("silent", "LISTEN"), True),
    (("python", "ruby"), False),
    (("a gentleman", "elegant man"), True),
    (("eleven plus two", "twelve plus one"), True),
    (("William Shakespeare", "I am a weakish speller"), True),
    (("", ""), True)
]


for args, expected in tests:

    result = anagrams(*args)

    print(result == expected)