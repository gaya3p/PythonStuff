rows = 10

#ascending half
for i in range(0,rows):
    for j in range(0, i):
        print(j+1, end=' ')
    print()
    
#descending half
for i in range(rows, 0, -1):
    for j in range(0,i):
        print(j+1, end=' ')
    print()