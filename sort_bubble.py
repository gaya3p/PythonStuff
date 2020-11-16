from random import randint
l = [randint(1, 100) for i in range(10)]
print('Original: ', l)
n = len(l)

for i in range(n):
    for j in range(n-i-1):
        if l[j+1] < l[j]:
            l[j+1], l[j] = l[j], l[j+1]

print('Sorted: ', l)
