import timeit, functools
    
s1 = 'tommarvoloriddle'
s2 = 'iamlordvoldemortasd'

def isAnagram1(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return True
    return False
    
def isAnagram2(s1, s2):
    f1, f2 = {}, {}
    for x in s1:
        f1[x] = f1[x]+1 if x in f1 else 1
    for x in s2:
        f2[x] = f2[x]+1 if x in f2 else 1
    return f1 == f2

def isAnagram3(s1, s2):
    f1, f2 = {}, {}
    if len(s1) == len(s1):
        for x in s1:
            f1[x] = f1[x]+1 if x in f1 else 1
        for x in s2:
            f2[x] = f2[x]+1 if x in f2 else 1
        return f1 == f2
    else:
        return False
    
t1 = (timeit.Timer(functools.partial(isAnagram1, s1, s2))).timeit(1000)
t2 = (timeit.Timer(functools.partial(isAnagram2, s1, s2))).timeit(1000)
t3 = (timeit.Timer(functools.partial(isAnagram3, s1, s2))).timeit(1000)
print(t1*1000)
print(t2*1000)
print(t3*1000)
