rows = 7#int(input())
columns = 9#int(input())

c = '* '
s = '  '

for i in range(rows):
    mid_r = (int(rows/2) )
    ss = columns - int(columns/2) - 2
    if i == 0:
        print(c, s*ss, c*(int(columns/2) + 1), sep='')
    
    elif i == mid_r:
        print(c*columns, sep='')

    elif i == rows - 1:
        print(c*(int(columns/2) + 1), s*ss, c , sep='')

    elif i < mid_r:
        print(c, s*ss, c, sep='')
    
    else:
        print(s*(ss+1), c, s*(ss), c, sep='')
