'''Min additions to make the sequence valid'''
s = list('((()))((())') #input()
stk = []

for x in s:
    if stk:
        if stk[-1] == '(' and x == ')':
            stk.pop()
        else:
            # x == '('
            stk.append(x)
    else:
        stk.append(x)
print(len(stk))
