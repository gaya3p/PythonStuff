#Main code's Author: Soham Pramanik
from tkinter import *
import mysql.connector
from tkinter import messagebox
import builtins
import importlib.util as iu

import os
v=os.getcwd()

c=(v+"\\Data")
sys.path.insert(0,c)

window=Tk()
window.resizable(width=False, height=False)
window.title("Password Required")
window.geometry("300x100+450+240")

name=Label(window,text="Enter Your MySql Password",font=('Helvetica',10,'bold')).place(x=65,y=5)
e=Entry(window,bd=4,show='*')
e.place(x=89,y=30)

spec = iu.spec_from_file_location('Msg.py', ""+v+"\Data\Msg.py")
foo = iu.module_from_spec(spec)

def check():
    try:
        m=mysql.connector.connect(host="localhost",user="root",passwd=e.get())
        window.destroy()
        spec.loader.exec_module(foo)
        
    except:
        messagebox.showinfo("It's Neccessary","Please Enter The Correct Password.")
        
def fun(a):
    if not a:
        messagebox.showinfo("It's Neccessary","Please Enter Your MySql Password. We Work On Localhost.")
        messagebox.showinfo("Tip",'Enter "(NULL)" If You Have No Password')
    else:
        if a=="(NULL)":
            builtins.pas = ''
            check()      
        else:
            builtins.pas = a
            check()

b=Button(window,text="Submit",command=lambda:fun(e.get()),bd=3,bg="orange",activeforeground="orange").place(x=125,y=60)
window.bind('<Return>',lambda x:fun(e.get()))
window.mainloop()
