'''
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''
chap = 'CHAPTER'

with open('hp2.txt', 'r+') as f:
    contents = f.readlines()
    
for line in contents:
    first = line.strip()[0:7]
    if line.isupper() and first == chap:
        print(' '.join(line.strip().split()[2:]))
    else:
        line.replace('\n\n', '\n')

while '\n' in contents:
    contents.remove('\n')
        
with open('hpnew.txt.tmp', 'w') as f:
    for line in contents:
        f.write(line)
    
#f = open('hp.txt', 'r', encoding='utf-8')
#f.close()