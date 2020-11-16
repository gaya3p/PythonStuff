money = int(input('Amount: '))

d = {
    2000: 0,
    500: 0,
    200: 0,
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

for a in d.keys():
    s = money % a
    j = money // a

    d[a] += j
    money = s

for x, y in d.items():
    print(f'{x} * {y}')