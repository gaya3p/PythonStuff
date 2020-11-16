'''matrix Operations'''
M1 = [
    [4, 5, 18],
    [2, 5, 13],
    [1, 18, 20],
    [4, 2, 10],
    [12, 10, 13]
]

M2 = [
    [8, 8, 18],
    [7, 12, 14],
    [19, 22, 4],
    [2, 4, 10],
    [10, 2, 10]
]

S = [[] for i in range(len(M1))]

for i, j in enumerate(zip(M1, M2)):
    x, y = j
    '''zip(x, y) != j'''
    for a, b in zip(x, y):
        S[i].append(a+b)

for row in S:
    print(row)
