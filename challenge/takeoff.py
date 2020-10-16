'''
3 planes: take off at every nth day
A: p, 2p, 3p
b: q, 2q, 3q..
C: ...

if one flight per day, then take off
else, no fights

print total no. if flight in N days
'''

N = int(input()) #test cases

def count(a):
    l = {}
    for x in a:
        l[x] = l[x]+1 if x in l else 1
    return l

def factor(k):
    e = w//k
    for i in range(1, e+1):
        a.append(i*k)


for _ in range(N):
    w, x, y, z = list(map(int, input().split()))  
    # w: no of days
    # x, y, z = p, q, r
    a=[]
    factor(x)
    factor(y)
    factor(z)
    c=list(count(a).values())
    d=0
    for i in c:
        if(i==1):
            d+=1
    print(d)
