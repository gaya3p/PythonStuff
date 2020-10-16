'''
Charges have a property of killing each other or in other words neutralizing each other if they are of
same charge and next to each other.
aaacccbbcccd -> accd -> ad

'''
n = 12
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
n = 12
s = list('aaacccbbcccd')
stack = [s[0]]

for i in range(1, len(s)):
    stack.append(s[i])
    try:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    except:
        pass

print(''.join(stack))
'''
