import mysql.connector as m1
import time
def returnConnection():
        mycon = m1.connect(host="127.0.0.1",user="root",password='alohomora',database='company')
        return mycon


	
