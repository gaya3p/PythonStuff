import csv
#import cs50
import mysql.connector as sq

db = sq.connect(host='localhost', user='root', passwd='alohomora')
cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS hogwarts')
cursor.execute('USE hogwarts')

table = '''students(first_name varchar(15), 
                    middle_name varchar(15),
                    last_name varchar(15),
                    house varchar(10),
                    birth_year int)
                    '''
cursor.execute(f'CREATE TABLE IF NOT EXISTS {table}')

file_name = 'characters'#input('Enter file name: ')

#db = cs50.SQL('sqlite:///students.db')
with open(file_name + '.csv') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        name = row['name'].split()
        if len(name) == 3:
            n1, n2, n3 = name
        else:
            n1, n3, n2 = *name, None
        
        house = row['house']
        year = row['birth']
        values = (n1, n2, n3, house, year)
        print(values)
        cursor.execute('INSERT INTO students VALUES(%s, %s, %s, %s, %s)', values)
        
db.commit()