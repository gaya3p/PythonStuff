from math import sqrt
a = (3, 5,6,8,2,6,34,54,2,0,1)

n = len(a)
xbar = sum(a)/n
s = 0

for xi in a:
    s += (xi-xbar)**2
    
sd = sqrt(s/(n-1))

print(sd)