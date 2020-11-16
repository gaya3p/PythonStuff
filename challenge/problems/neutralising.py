'''
Charges have a property of killing each other or in other words neutralizing each other if they are of
same charge and next to each other.
aaacccbbcccd -> accd -> ad

'''
s = list('aaacccbbbcccd')
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