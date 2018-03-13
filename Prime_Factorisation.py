def main():
    try:
        while True:
            # simple function to test if a number, n, is a prime number
            def isPrime(n):
                if n >= 2:
                    for i in range(2, n):
                        if not (n % i):
                            return False
                else:
                    return False
                return True

            def factorise(n, li):
                if isPrime(n):
                    return
                # exit if n is already prime
                if n <= 1:
                    return
                # prevents infinite loop and divide by zero errors

                for i in range(1, n):
                    x = int(n / i)
                # x is a child node
                    if n % i == 0:
                        # search for a factor of n

                        if isPrime(x):
                            li.append(x)
                # if x is prime, we've reached the end of a branch, add it to the list
                            if isPrime(i):
                                li.append(i)
                # if i is prime, we've reached the end of the program
                            break
                factorise(i, li)
                # move to the next branch

            # examples:
            #     20             45
            #    /  \            /  \
            #   10   2       9    5
            #  /  \           / \
            # 5    2        3   3

            primes = []
            n = int(input("Enter the number:  "))
            factorise(n, primes)
            if len(primes) > 1:
                out = '*'.join(str(x) for x in primes)
                print(out + " = " + str(n))
            else:
                print("{} is already a prime number.".format(n))

            # This prevents infinity loop of the whole program.

    except:
        print("Your input is not valid. Please try again. :( ")


main()
