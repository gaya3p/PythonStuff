s1 = 'WeAreChilling'
s2 = 'HackComIsChill'

if len(s1) < len(s2):
    s1, s2 = s2, s1

max_sub = ''
mx = 0
for i in range(len(s2)):
    for j in range(i+1, len(s2)+1):
        sub = s2[i:j]
        
        if (sub in s1) and (len(sub) > mx):
            max_sub = sub
            mx = len(sub)
            
print(max_sub)