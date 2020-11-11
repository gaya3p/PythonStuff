n = int(input())
l = list(map(int, input().split()))

stack = [l[0]]

for i in range(1, n):
    stack.append(l[i])
    stack.sort()
    
    if len(stack) >= 2:
        if stack[-1] == stack[-2]:
            stack.pop()
            a = stack.pop()
            stack.append(a*2)
            
stack.sort()
print(' '.join(map(str, stack)))
