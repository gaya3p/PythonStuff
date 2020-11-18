import pickle

def insert_record(Id, name, mark):
    with open('data.pickle', 'ab') as f:
        pickle.dump([Id, name, mark], f)

def read_records():
    records = []
    with open('data.pickle', 'rb') as f:
        while 1:
            try:
                records.append(pickle.load(f))
            except:
                break
    return records

print(read_records())