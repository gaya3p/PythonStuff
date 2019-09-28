s = 'that arizona sky burning in your eyes'
a =''
for i in range(1, len(s), 2):
    a += s[i-1] + s[i].capitalize()
    
print(a)