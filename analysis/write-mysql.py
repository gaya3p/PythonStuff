import csv
import mysql.connector as sq

db = sq.connect(host='localhost', user='root', password='alohomora')
cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS hogwarts')
cursor.execute('USE hogwarts')

def createTable(header):
    table = f'''magic({header[0]} varchar(25), 
                        {header[1]} varchar(15),
                        {header[2]} varchar(100),
                        {header[3]} varchar(5))
                        '''
    print(table)
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table}')

file_name = 'magic2'#input('Enter file name: ')

#db = cs50.SQL('sqlite:///students.db')
with open(file_name + '.csv') as file:
    reader = csv.reader(file)
    header = next(reader)
    createTable(header)
    for row in list(reader)[1:]:
        # name = row['name'].split()
        # if len(name) == 3:
        #     n1, n2, n3 = name
        # else:
        #     n1, n3, n2 = *name, None
        # house = row['house']
        # year = row['birth']
        
        values = (row[0], row[1], row[2], row[3])
        print(values)
        cursor.execute('INSERT INTO magic VALUES(%s, %s, %s, %s)', values)
        
db.commit()