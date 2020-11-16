s = 'SPIDERMAN'#'TSDSDARDXCPY'
a = 'SERM'#'ARXY'

for letter in a:
    if letter not in s:
        print('no')
        break
else:
    s = s[s.find(a[0]):]
    f = []
    for i in range(1, len(a)):
        f.append(s.find(a[i]))
        
    '''To Check if they're in order'''
    if f == sorted(f):
        print('yes')
    else:
        print('no')