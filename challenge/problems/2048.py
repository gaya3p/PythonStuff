# s = list(map(int, input().split()))
s = [2, 4, 4, 8, 8, 16, 32, 32]
stack = [s[0]]

for i in range(1, len(s)):
    stack.append(s[i])
    stack.sort()

    if len(stack) >= 2:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.append(stack.pop()*2)

print(' '.join(map(str, stack)))