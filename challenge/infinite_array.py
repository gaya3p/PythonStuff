'''
You are given an array A of size N. 
You have also defined an array B as the concatenation of 
array A for infinite number of times. 
Eg:
A = [1, 3, 5]
B = [1, 3, 5, 1, 3, 5, 3, 5, ...]

given range x to y in B, print sum of that range in B
L = initial value of ranges
R = final value of ranges
'''

def solve (a, r, l):
    sums = []
    n = len(a)

    for x, y in zip(l, r):
        s = 0
        f = y-x+1
        i = (x-1)%n

        while f > 0:
            s += a[i]
            i += 1
            f -= 1
            if i == n:
                i = 0
                
        sums.append(s)

    return sums 

A = [4, 1, 5]
L = [1, 3, 9, 2]
R = [4, 7, 10, 10]

out_ = solve(A, R, L)
print(out_)