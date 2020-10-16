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
