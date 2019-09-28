rows = 5
n = int(rows/2)
j = n-1

print(' '*n+'*')
s = ' '
c = '*' 
for i in range(1, 2*n):
    if i > n:
        print(s*(i-n) + c + s*(2*j-1)+ c)
        j -= 1
    else:
        print(s*(n-i) + c + s*(2*i-1) + c)
if n > 1:
    print(' '*n+'*')
 
n = 10
s = ' '
print(c)
for i in range(1, n):
    print(c + s*(2*i-1) + c)
for i in range(n, 0, -1):
    print(c + s*(2*i-1) + c)
print(c)
