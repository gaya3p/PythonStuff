'''import math
x = int(input(''))
a = 0
for i in range(10):
    if i%2==0:
        a += (x**(i+1))/math.factorial(i+1)
        print(a)
    else:
        a -= (x**(i+1))/math.factorial(i+1)
        print(a)
print(a)

n = 5#int(input('rows: '))

for i in range(0, n):
    for j in range(0, n-i-1):
        print(end=' ')
    for j in range(0, i+1):
##        if j == 0 or j == i:
        print('*', end=' ')
##        print(end=' ')
    print()

for i in range(n, 0, -1):
    for j in range(0, n-i):
        print(end=' ')
    for j in range(0, i):
        print('*', end=' ')
    print()'''

romanKeys = {
    'M':1000,
    'CM':900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}

def toRoman(n):
    roman = ''
    for key in romanKeys:
        print('val:', romanKeys[key])
        while n >= romanKeys[key]:
            roman += key
            n -= romanKeys[key]
            print('no is decreased', n)
    return roman

print(toRoman(1998))
