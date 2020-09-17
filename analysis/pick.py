import pickle, csv, bz2

dic = {'a':1, 'b': 2}

pickled_obj = pickle.dumps(dic)
'''
with open('b99.csv', 'r') as f:
    reader = csv.reader(f)
    content = []
    for row in reader:
        content.append(row)
    
    dumped = pickle.dumps(content)
    content = bz2.compress(dumped)

with open ('pickle.pickle', 'wb') as f:
    pickle.dump(content, f)
'''  
with open('pickle.pickle', 'rb') as f:
    a = pickle.load(f)
    b = bz2.decompress(a)
    
print(b)