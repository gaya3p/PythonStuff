import pickle
# import os

file = 'records.dat'

def read_record():
    with open(file, 'rb') as f:
        while True:    
            try:
                row = pickle.load(f)
                print(row[0], row[1], row[2])
            except EOFError:
                print('END')
                break
            
def insert_record():  
    with open(file, 'ab') as f:
        # while True:
        sno = int(input('Enter id: '))
        name = input('Enter name: ')
        marks = int(input('Enter marks: '))
        
        record = [sno, name, marks]
        pickle.dump(record, f)
        
def search_record():
    sno = int(input('Enter id to search: '))
    with open(file, 'rb') as f:
        while True:
            # try:
            row = pickle.load(f)
            if sno == row[0]:
                print(row[0], row[1], row[2])
                break
            # except EOFError:
            #     print('No record found')
            #     break
                    

def update_record():
    sno = int(input('Enter id to update'))
    records = []
    # with open(file, '')

def delete_record():
    sno = int(input('Id to delete: '))
    records = []
    with open(file, 'rb+') as f:
        while True:
            try:
                row = pickle.load(f)
                records.append(row)
            except:
                break
            
        for row in records:
            if row[0] == sno:
                records.remove(row)
                
        while True:
            for row in records:
                pickle.dump(row, f)
    print('Record deleted')
        
                
# delete_record()
search_record()