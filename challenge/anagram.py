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

''' BEST WAY '''    
def isAnagram2(s1, s2):
    f1, f2 = {}, {}
    if len(s1) == len(s1):
        for x in s1:
            f1[x] = f1[x]+1 if x in f1 else 1
        for x in s2:
            f2[x] = f2[x]+1 if x in f2 else 1
        return f1 == f2
    else:
        return False

    
print(isAnagram1(s1, s2))
print(isAnagram2(s1, s2))

