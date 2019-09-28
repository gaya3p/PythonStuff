rows = 9
n = int(rows/2)
j = n - 1
s = ' '
c = '*'

print(s*n + c)
for i in range(1, 2*n):
    if i > n:
        print(s*(i-n) + c + s*(2*j-1) + c)
        j -= 1
    else:
        print(s*(n-i) + c + s*(2*i-1) + c)
print(s*n + c)

#for i in range(n):
#    for j in range(i, n):
#        print(s, end='')
#    if i == 0:
#        print('*', end='')
#    else:
#        print('*'+s*(2*i-1)+'*', end='')
#    print()
#
#for i in range(n):
#    for j in range(i):
#        print(s, end='')
#    if i == n-1:
#        print('*', end='')
#    else:
#        print('*'+s*(2*(n-i-1))+'*', end='')
# 
#        
#    print()
