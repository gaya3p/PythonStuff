r = 10
n = int(r/2)+1

for i in range(n):
    for j in range(n, i, -1):
        print(end=' ')
    for j in range(0, i):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(0, i):
        print('', end=' ')
    for j in range(0, n-i):
        print('*', end=' ')
    print()

a = []
for i in range(5):
    a.append([])
    print(a[i])
    a[i].append(1)

    for j in range(1, i):
        a[i].append(a[i-1][j-1] + a[i-1][j])
    if 5 != 0:
        a[i].append(1)

for i in range(len(a)):
    print(' '*(5-i), end='')
    for j in range(0, i+1):
        print(a[i][j], end=' ')
    print()

for i in range(n):
    for j in range(n, i, -1):
        print(end=' ')
    for j in range(0, i):
        print(j, end=' ')
    print()

for i in range(n):
    for j in range(0, i):
        print(end=' ')
    for j in range(n, i, -1):
        print(j, end=' ')
    print()


