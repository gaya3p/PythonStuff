'''
# The diamond size
l = 20
rows = ['*']

# Add half of the rows; we loop over the odd numbers from
# 1 to l, and then append a star followed by `i` spaces and a star
for i in range(1, l, 2):
    rows.append('*' + ' ' * i + '*')

# Mirror the rows and append; we get all but the last row
# (the middle row) from the list, and inverse it (using
# `[::-1]`) and add that to the original list. 
rows += rows[:-1][::-1]

# center-align each row, and join them
align = lambda x: ('{:^%s}' % (l+1)).format(x)
diamond = '\n'.join(map(align, rows))

print(diamond)
'''

n = 6
j = n-1

c, s = '*', ' '

print(n*s + c)
for i in range(1, n*2):
    if i > n:
        print(s*(i-n) + c + s*(2*j-1) + c)
        j -= 1
    else:
        print(s*(n-i) + c + s*(2*i-1) + c)
print(n*s + c)