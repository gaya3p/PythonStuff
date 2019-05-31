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
        return # exit if already prime
    if n <= 1:
        return # preventa infinity loop & ZeroDivisionError
    
    for i in range(1, n):
        x = int(n / i)

        if n % i == 0:
            # search for a factor of n
            if isPrime(x):
                factors.append(x)
                # if x is prime we've reached end of the branch
                if isPrime(i):
                    factors.append(i)
                    # if i is prime, we've reached end of the program
                break
            
        # if i is not prime, further factorise i into
        # a * b and so on until all factors are prime
        factorise(i, factors)
"""
    n
   / \
  x   i
     / \
    a   b
"""

factors = []
n = int(input('Enter the number: '))
factorise(n, factors)
factors.sort()

if len(factors) > 1:
    out = '*'.join(str(x) for x in factors)
    print(f'{out} = {n}')
else:
    print(f'{n} is already a prime number.')