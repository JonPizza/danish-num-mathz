ops = {
    'plus': '+',
    'minus': '-',
    'gange': '*',
    'divideret': '/',
    'med': '', # it comes as divided "BY", so med is by
}

danish_nums = {
    'en': 1,
    'to': 2,
    'tre': 3,
    'fire': 4,
    'fem': 5,
    'seks': 6,
    'syv': 7,
    'otte': 8,
    'ni': 9,
    'ti': 10,
	'elleve': 11,
	'tolv': 12,
	'tretten': 13,
	'fjorten': 14,
	'femten': 15,
	'seksten': 16,
	'sytten': 17,
	'atten': 18,
	'nitten': 19,
	'tyve': 20,
	'énogtyve': 21,
	'toogtyve': 22,
	'treogtyve': 23,
	'fireogtyve': 24,
	'femogtyve': 25,
	'seksogtyve': 26,
	'syvogtyve': 27,
	'otteogtyve': 28,
	'niogtyve': 29,
	'tredive': 30,
	'énogtredive': 31,
	'toogtredive': 32,
	'treogtredive': 33,
	'fireogtredive': 34,
	'femogtredive': 35,
	'seksogtredive': 36,
	'syvogtredive': 37,
	'otteogtredive': 38,
	'niogtredive': 39,
	'fyrre': 40,
	'énogfyrre': 41,
	'toogfyrre': 42,
	'treogfyrre': 43,
	'fireogfyrre': 44,
	'femogfyrre': 45,
	'seksogfyrre': 46,
	'syvogfyrre': 47,
	'otteogfyrre': 48,
	'niogfyrre': 49,
	'halvtreds': 50,
	'énoghalvtreds': 51,
	'tooghalvtreds': 52,
	'treoghalvtreds': 53,
	'fireoghalvtreds': 54,
	'femoghalvtreds': 55,
	'seksoghalvtreds': 56,
	'syvoghalvtreds': 57,
	'otteoghalvtreds': 58,
	'nioghalvtreds': 59,
	'tres': 60,
	'énogtres': 61,
	'toogtres': 62,
	'treogtres': 63,
	'fireogtres': 64,
	'femogtres': 65,
	'seksogtres': 66,
	'syvogtres': 67,
	'otteogtres': 68,
	'niogtres': 69,
	'halvfjerds': 70,
	'énoghalvfjerds': 71,
	'tooghalvfjerds': 72,
	'treoghalvfjerds': 73,
	'fireoghalvfjerds': 74,
	'femoghalvfjerds': 75,
	'seksoghalvfjerds': 76,
	'syvoghalvfjerds': 77,
	'otteoghalvfjerds': 78,
	'nioghalvfjerds': 79,
	'firs': 80,
	'énogfirs': 81,
	'toogfirs': 82,
	'treogfirs': 83,
	'fireogfirs': 84,
	'femogfirs': 85,
	'seksogfirs': 86,
	'syvogfirs': 87,
	'otteogfirs': 88,
	'niogfirs': 89,
	'halvfems': 90,
	'énoghalvfems': 91,
	'tooghalvfems': 92,
	'treoghalvfems': 93,
	'fireoghalvfems': 94,
	'femoghalvfems': 95,
	'seksoghalvfems': 96,
	'syvoghalvfems': 97,
	'otteoghalvfems': 98,
	'nioghalvfems': 99,
	'hundrede': 100,
}

def num_to_word(n):
    return [key for key, value in danish_nums.items() if value == n][0]

while True:
    s = input('Evaluate me! : ')
    e = ''

    for word in s.replace('?', '').split(' '):
        if word in ops:
            e += ops[word]
        else:
            e += str(danish_nums[word])

    print(num_to_word(eval(e)))
