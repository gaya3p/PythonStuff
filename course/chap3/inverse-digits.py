n = int(input('Enter a number: '))
rev = 0

while n > 0:
    s = n % 10
    rev = rev * 10 + s
    n = n // 10
    
print(rev)
