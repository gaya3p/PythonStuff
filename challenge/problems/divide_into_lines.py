'''
write s in k lines with min a and max b letters
in each line
'''
k = 4
a = 5
b = 11
s = 'wisemensayfoolsarerushing'

l = len(s)
lst = [a for x in range(k)]
g = l - sum(lst)
# print(lst,g)

while g > 0:
    for i in range(k):
        if lst[i] == b:
            break
        lst[i] += 1
        # print(lst)
        g = l - sum(lst)
        if g <= 0:
            break
    else:
        continue
    break

if g:
    print('No solution')
else:
    h = 0
    for i in range(k):
        print(s[h:h + lst[i]])
        h += lst[i]