def isPrime(n):
    if n >=2 :
        for i in range(2,int((n/2)+1)):
            print(f'{n} % {i} = {n%i}')
            if not(n%i):
                return False
    else:
        return False
    return True

n = int(input('Enter a number: '))

print('Its is prime.') if isPrime(n) else print('Its is not prime.')
