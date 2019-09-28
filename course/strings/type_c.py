'''1
p = '102-234-1234'
if p[3] == p[7] == '-':
    d = ''.join(p.split('-'))
    if d.isdigit():
        print('valid')'''
        
'''3
l = 'so you think you can asj45 stop me and spit in my eye ?'
w = len(l.split(' '))
c = len(l)
an = 0
for ch in l.split(' '):
    if ch.isalnum():
        print(ch)
        an += 1
print(w, c, (an/w)*100)'''

'''4
l = 'So when Im all Chocked up and I cant find the Words'
s = ''
for ch in l:
    #if ch.isalpha():
    s += ch.swapcase()
    #else:
      #  sw += ch
print(l.swapcase())'''

'''6'''
l = 'supermegafoxyawesomehot'
n = int(len(l) / 2)
j = n-1
for i in range(1, n+1):
    print(' '*(i-1) + l[i-1] + ' '*(2*j+1) + l[-i])
    j -= 1
if len(l) % 2 == 1:
    print(' '*(n) + l[n])
'''l = '23429sdhfgsjdh834kdf8'
s = 0
for a in l:
    if a.isdigit():
        s += int(a)'''