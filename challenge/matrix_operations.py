'''matrix Operations'''
M1 = [
    [4, 5, 18],
    [2, 5, 13],
    [1, 18, 20],
]

M2 = [
    [8, 8, 18],
    [7, 12, 14],
    [19, 22, 4],
]

# M1 = eval(input('Enter a matrix: '))
# M2 = eval(input('Enter a matrix: '))

def add(M1, M2):
    S = [[] for i in range(len(M1))]

    for i, (row1, row2) in enumerate(zip(M1, M2)):
        for a, b in zip(row1, row2):
            S[i].append(a+b)
    return S
S = add(M1, M2)
for row in S:
    print(row)
