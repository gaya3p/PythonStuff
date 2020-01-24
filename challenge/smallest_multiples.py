n = 100
ans = 0
def isPrime(n):
    if n >= 2:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                return False
    else:
        return False
    return True

if isPrime(n):
    print('Not possible')
else:
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            a = int(str(int(n/i)) + str(i))
            if i == 2:
                ans = a
            elif a < ans:
                ans = a
print(ans)