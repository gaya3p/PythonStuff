import os
import mysql.connector
import importlib.util as iu

v=os.getcwd()
t = [('buyers',),('products',)]

m = mysql.connector.connect(host='localhost',user='root',password=pas)
mc =m.cursor()
mc.execute('create database if not exists TechShop')
mc.close()

m1 = mysql.connector.connect(host='localhost',user='root',password=pas,database='TechShop')
mc = m1.cursor()
fd = open(''+v+'/Data/soham.sql', 'r')
f=fd.read()
fd.close()

spec = iu.spec_from_file_location('Start.py', ""+v+"\\Data\\Start.py")
foo = iu.module_from_spec(spec)


mc.execute("show tables")
table = mc.fetchall()

if table!=t:
        try:
                mc.execute(f)
                spec.loader.exec_module(foo)
        except:
                for x in mc.execute(f,multi=True):
                        pass
                        break
                spec.loader.exec_module(foo)
else:
    spec.loader.exec_module(foo)

