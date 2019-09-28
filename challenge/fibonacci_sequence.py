#Fibonacci Sequence
# Enter "till" or "the" first.
# Then enter the number of that number.

UserMood = input("Enter \"till\"or \"the\" nth term. ")

if UserMood == "till":
    '''If he/she wants till the nth number'''
    fib_cache = {}

    #If there
    def fibonacci(n):
        if n in fib_cache:
            return fib_cache[n]

        if n == 1:
            val =  1
        if n == 2:
            val =  1
        elif n > 2:
            val =  fibonacci(n-1) + fibonacci(n-2)

        fib_cache[n] = val
        return val

    n = int(input("Enter the number: "))
    for n in range(1, n+1):
       
        if n == 1:
             print(n, "st term is", fibonacci(n), '.')
        if n == 2:
             print(n, "nd term is", fibonacci(n), '.')
        if n == 3:
             print(n, "rd term is", fibonacci(n), '.')
        if n > 3:
             print(n, "th term is", fibonacci(n), '.')
#**********************************************************************
#**********************************************************************


'''If he/she wants the nth number'''
if UserMood == "the":
    fib_cache = {}

    #If there
    def fibonacci(n):
        if n in fib_cache:
            return fib_cache[n]

        if n == 1:
            val =  1
        if n == 2:
            val =  1
        elif n > 2:
            val =  fibonacci(n-1) + fibonacci(n-2)

        fib_cache[n] = val
        return val

    n = int(input("Enter the number : "))
    if n == 1:
        print( "The" ,n, 'st term is', fibonacci(n), '.')
    if n == 2:
        print( "The" ,n, 'nd term is', fibonacci(n), '.')
    if n == 3:
        print( "The" ,n, 'rd term is', fibonacci(n), '.')
    if n > 3:
        print( "The" ,n, 'th term is', fibonacci(n), '.')

else:
    print("Print Enter \"till\" or \"the\" first. Then enter the number of that number.")
