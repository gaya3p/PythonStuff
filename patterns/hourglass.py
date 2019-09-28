n = 5
c = '*'
s = ' '
a = '-'
for i in range(n):
    for j in range(1, i+2):
        if j == n:
            continue
        print(c, end=' ')
    for j in range(n+2-i*2):
        print(s, end=' ')
    for j in range(i+1):
        print(c, end=' ')
    print()
    
for i in range(n):
    for j in range(n, i+1, -1):
        print(c, end=' ')
    for j in range(0, i*2+1):
        print(s, end=' ')
    for j in range(n, i+1, -1):
        print(c,  end=' ')
    print()

