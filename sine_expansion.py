deg = int(input('Enter degree: '))
pi = 3.14159265
a = (pi/180)*deg
x = 3 # power

def factorial(n): # factorial
    pr = 1
    for i in range(n, 0, -1):
        pr *= i
    return pr

def sin(n):
    hg = a
    x = 3
    for i in range(10):
        if i%2 == 0:
            hg -= ((n**x)/factorial(x))
        else:
            hg += ((n**x)/factorial(x))
        x += 2
    return hg
        
print(f'Sine of {deg} degree = {sin(a)}')
