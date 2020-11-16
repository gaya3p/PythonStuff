import mysql.connector as sq

db = sq.connect(host="localhost",user="root",passwd="alohomora", db='library')

cursor = db.cursor()

s = "select count(*) from books where type = 'fiction';"
cursor.execute(s)

yes = int(cursor.fetchall()[0][0])

print(yes)

db.close()