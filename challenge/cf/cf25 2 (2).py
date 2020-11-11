n, h = list(map(int, input().split()))
stacks = list(map(int, input().split()))
commands = list(map(int, input().split()))

pos = 0
curr = []
for c in commands:
    if c == 0:
        break
    elif c == 1:
        pos = pos - 1 if pos > 0 else 0
    elif c == 2:
        pos = pos + 1 if pos < n-1 else n-1
    elif c == 3:
        if len(curr) == 0 and stacks[pos] > 0:
            curr.append(stacks[pos])
            stacks[pos] -= 1
    elif c == 4:
        if len(curr) == 1 and stacks[pos] < h:
            curr.pop()
            stacks[pos] += 1
    else:
        continue

print(' '.join(map(str, stacks)))
