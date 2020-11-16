import pickle

file = 'data.pickle'

def insert_record():
    roll = int(input('Insert roll no: '))
    name = input('Insert name: ')
    marks = int(input('insert marks:'))
    
    record = [roll, name, marks]

    with open(file, 'ab') as f:
        pickle.dump(record, f)
        
# a = []
    
def read_records():
    with open(file, 'rb') as f:
        while True:
            try:
                record = pickle.load(f)
                # a.append(record)
                print(record[0], record[1], record[2])
                # print()
            except:
                # print('over')
                # raise
                break
            
# read_records()
# print(a)

def search_record():
    roll = int(input('Enter id: '))
    found = False
    with open(file, 'rb') as f:
        while True:
            try:
                record = pickle.load(f)
                if record[0] == roll:
                    print(record[0], record[1], record[2])
                    found = True
            except:
                if not(found):
                    print('No records')
                break
            
def update_record():
    roll = int(input('Enter id: '))
    records = []
    with open(file, 'rb+') as f:
        while True:
            try:
                record = pickle.load(f)
                records.append(record)
            except:
                break
            
        f.seek(0)
        
        for record in records:
            if record[0] == roll:
                record[2] = int(input('Updated mark '))
            pickle.dump(record, f)
            
# search_record()

def delete_record():
    roll = int(input('Enter id: '))
    records = []
    with open(file, 'rb+') as f:
        while True:
            try:
                record = pickle.load(f)
                records.append(record)
            except:
                break
            
        # f.seek(0)
        print(records)
        print('over')
        
    with open(file, 'wb') as f:
        for record in records:
            if int(record[0]) == roll:
                print('to delete', record)
                continue
            pickle.dump(record, f)
            print(record)
            
            
            