matrix = [
    [1, 2, 3, 4],
    [3, 7, 1, 5],
    [6, 3, 8, 6]
]

rows = len(matrix)
columns = len(matrix[0])

transposed = [[] for x in range(columns)]
flat = [matrix[i][j] for i in range(rows) for j in range(columns)]

for i in range(columns):
    for j in range(0, len(flat), columns):
        transposed[i].append(flat[i+j])

def show(m):
    for row in m:
        print(row)

print('Original matrix')
show(matrix)
print('\nTransposed matrix')
show(transposed)