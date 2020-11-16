'''n = 10
a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    
    for j in range(1, i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if n != 0:
        a[i].append(1)
#align = lambda x: ('{:^%s}' % (n+1)).format(x)
for i in range(n):
    print(' ' * (n-i), end='')
    for j in range(0, i+1):
    #print('\n'.join(map(align, a[i])))
        print(a[i][j], end=' ')
    print()'''


m = 10
a = []
for i in range(m):
    a.append([])
    a[i].append(1)

    for j in range(1, i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if m != 0:
        a[i].append(1)

for i in range(m):
    print(' '*(m-i), end='')
    for j in range(0, i+1):
        print(a[i][j], end='  ')
    print()