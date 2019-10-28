inp = input('Enter a list of numbers (sep. by space): ').strip().split(' ')

a = []
for i in inp:
    a.append(int(i))

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
            ''' can combine only 2 numbers at once '''
            b.extend([num*2 for i in range(f//2)])
            if f%2 != 0:
                b.append(num)
        else:
            b.append(num)
    
    a = list(b)
    
a = sorted(a)
print('\nFinal arrangement: ', end='')
for num in a:
    print(num, end=' ')
            