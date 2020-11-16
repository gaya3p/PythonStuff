s1 = 'tommarvoloriddle'
s2 = 'iamlordvoldemort'

def isAnagram2(s1, s2):
    f1, f2 = {}, {}
    if len(s1) == len(s1):
        for x in s1:
            f1[x] = f1[x]+1 if x in f1 else 1
        for x in s2:
            f2[x] = f2[x]+1 if x in f2 else 1
        return f1 == f2
    return False

print(isAnagram2(s1, s2))

