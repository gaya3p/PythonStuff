files = ['hp1.txt','hp2.txt','hp3.txt','hp4.txt','hp5.txt','hp6.txt','hp7.txt']
chap = 'CHAPTER'
for file in files:
    with open(file, 'r') as f:
        con = f.readlines()
    
    print('Harry Potter ', file[2], '\n')
    
    for line in con:
        if line.isupper() and line.strip()[0:7] == chap:
            print(line)
            #print(' '.join(line.strip().split()[2:]))
    
    print()