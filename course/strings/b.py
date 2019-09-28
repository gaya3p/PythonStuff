l = 'so you think you can jk gttr stop me and spit in my eye ?'
la = 'gaya3p13@gmail.com'

dom = la.split('@')[1]
if dom == 'gmail.com':
    print(dom)


'''7
i = 0
maxlen = 0
for word in l.split(' '):
    #print(word)
    if len(word) > maxlen:
        for ch in word:
            if ch in 'aeiou':
                print(word)
                continue
        
        s = word
    else:
        continue

print(s)
'''


'''5
s = 'you'
a = ''
i = 0
for word in l.split(' '):
    a += word.capitalize() + ' '
while i < len(l):
    
    if i == 0:
        a += l[0].upper()
    elif l[i-1] == ' ':
        a += l[i].upper()
    else:
        a += l[i]
    i += 1
    
print(a)'''