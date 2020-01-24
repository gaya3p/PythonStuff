import timeit, functools
    
s1 = 'tommarvoloriddle'
s2 = 'iamlordvoldemort'

def isAnagram1(s1, s2):
    if len(s2) == len(s2):
        for l1, l2 in zip(s1, s2):
            if (l1 not in s2) or (l2 not in s1):
                return False
        else:
            for letter in s1:
                if s1.count(letter) != s2.count(letter):
                    return False
            else:
                return True
    else:
        return False
    
def isAnagram2(s1, s2):
    d1, d2 = {}, {}
    if len(s1) == len(s2):
        for l in set(s1):
            d1[l] = s1.count(l)
        for l in set(s2):
            d2[l] = s1.count(l)
        return d1 == d2
    else:
        return False
    
#print(isAnagram1(s1, s2))
#print(isAnagram2(s1, s2))

t1 = (timeit.Timer(functools.partial(isAnagram1, s1, s2))).timeit(1000)
t2 = (timeit.Timer(functools.partial(isAnagram2, s1, s2))).timeit(1000)
print(t1*1000)
print(t2*1000)
print(t1/t2)