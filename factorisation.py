def isPrime(n):
    if n >=2:
        for i in range(2, int((n/2)+1)):
            # int((n/2)+1) to reduce computing time
            if not(n%i):
                return False
    else:
        return False
    return True

def factorise(n, factors):
    if isPrime(n):
        factors.append(n) # add the last factor
        return # exit if already prime
    if n <= 1:
        return # prevents infinity loop & ZeroDivisionError
    
    for i in range(2, int(n/2) +1):

        if isPrime(i) and n % i == 0:
            
            factors.append(i)

            # now factorise  n / i
            x = int(n/i)
            return factorise(x, factors)

'''
i | n
  |---
  | x
'''
factors = []
n = int(input('Enter the number: '))
factorise(n, factors)
factors.sort()

if len(factors) > 1:
    out = '*'.join(map(str, factors))
    print(f'{out} = {n}')
else:
    print(f'{n} is already a prime number.')