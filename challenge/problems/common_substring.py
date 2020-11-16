s1 = 'WeAreChilling'
s2 = 'HackComIsChill'

if len(s1) < len(s2):
    s1, s2 = s2, s1

subs = ['']
mx = 0
for i in range(len(s2)):
    for j in range(i+1, len(s2)+1):
        sub = s2[i:j]
        
        if (sub in s1) and (len(sub) > mx):
            subs.append(sub)
            mx = len(sub)
            
print(subs[-1])
