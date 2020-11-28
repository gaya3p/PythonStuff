from tkinter import *
import dbConnection as mydb
import hashlib
from tkinter import messagebox
import os


def login():
	mycon = mydb.returnConnection()
	mycur = mycon.cursor()
	u = user.get()
	p = pwd.get()
	p = hashlib.md5(p.encode())

	p = p.hexdigest()
	query="select * from login where user='"+u+"'"# and  password=('"+p+"')"
	print(p)
	mycur.execute(query)
	mydata = mycur.fetchone()
	#print(mydata[0],mydata[1])
	if mycur.rowcount==1:
		messagebox.showinfo('..:::Login','Login Successful')
		mywin.destroy()
		os.system('python mainframe.py')
		
	else:
		messagebox.showinfo('..:::Login','Access Denied')
	
			
mywin = Tk()
mywin.title("...::::User Authentication")
mywin.geometry("300x250+400+300")
mywin.resizable(False,False)
user=StringVar()
pwd=StringVar()
Label(mywin,text="Login Information",bg='purple', fg='pink',bd=5,font=('arial',12,'bold'),width=30).grid(columnspan=2)
Label(mywin,text="User Name",bg='silver', fg='navy',bd=5,font=('arial',12,'bold')).grid(row=2,column=0,pady=20)
t1=Entry(mywin,bg='yellow', fg='navy',bd=5,font=('arial',10,'bold'),textvariable=user)
t1.grid(row=2,column=1,pady=20)
Label(mywin,text="Password",bg='silver', fg='navy',bd=5,font=('arial',12,'bold')).grid(row=3,column=0,pady=10)
t2=Entry(mywin,show="$",bg='yellow', fg='navy',bd=5,font=('arial',10,'bold'),textvariable=pwd)
t2.grid(row=3,column=1,pady=10)
t1.focus_set()

img1=PhotoImage(file='login.png')
img2=PhotoImage(file='exit.png')

Button(mywin,image=img1,height=60, width=120,command=login).grid(row=4,column=0)
Button(mywin,image=img2,height=60, width=120,command=mywin.quit).grid(row=4,column=1)

mywin.mainloop()
