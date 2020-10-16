from itertools import permutations
s = 'ABDCD'

def isPal(s):
    if s == s[::-1]:
        return True
    else: 
        return False
    
perms = []
for i in range(3, len(s) + 1):
    perms.extend(list(permutations(s, i)))

l = 0
a = ''
b = ()
for perm in perms:
    if len(perm) > l:
        if isPal(perm):
            b = perm
            l = len(perm)
            
for c in b:
    a += c
    
print(f'Longest palindromic permutation is {a} with length {l}.')
