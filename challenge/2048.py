a = list(map(int, input('List of numbers: ').strip().split(' ')))

def isNotUnique(lst):
    for i in set(lst):
        if lst.count(i) > 1:
            return True
    return False

while isNotUnique(a):
    b = []
    
    for num in set(a):
        f = a.count(num) 
        
        if f > 1:
            # can combine only 2 numbers at once 
            b.extend([num*2 for _ in range(f//2)])
            if f%2 != 0: # if count is odd
                b.append(num)
        else:
            b.append(num)
    
    a = list(b)
    
a = sorted(a)
print('\nFinal arrangement: ', ' '.join(str(x) for x in a))

'''
should technically workz

s = [2, 4, 4, 8, 8, 16, 32, 32]
stack = [s[0]]

for i in range(1, len(s)):
    stack.append(s[i])
    print(stack)
    stack.sort()
    try:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.append(stack.pop()*2)
            
    except:
        pass

print(stack)
'''
