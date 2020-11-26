from tkinter import *
from tkinter import messagebox
import builtins
import importlib.util as iu
import mysql.connector

import os
v=os.getcwd()

m=mysql.connector.connect(host="localhost",user="root",passwd=pas,database="TechShop")
mc=m.cursor()

def close_window():
        window.destroy()
        
#Tkinter Window Creation
window=Tk()
window.resizable(width=False, height=False)
window.title("Login")
window.geometry("300x169+450+210")

img=PhotoImage(file=r""+v+"\Data\Verify.png")
w=Label(window,image=img).pack()

#Labels
name=Label(window,text="Username").place(x=30,y=30)
email=Label(window,text="Your Email ").place(x=30,y=68)
password=Label(window,text="Password ").place(x=30,y=101)

#Entries
e1=Entry(window,bd=4)
e1.place(x=100,y=30)
e2=Entry(window,bd=4)
e2.place(x=100,y=68)
e3=Entry(window,bd=4,show='*')
e3.place(x=100,y=101)

#Record Collection
mc.execute("select Name,Email,Password from buyers")
t=mc.fetchall()

#Button1's Command
def fun(a, b,c):
        p=a,b,c        
        try:
            if p in [x for x  in t]:
                    
                builtins.em = b
                close_window()
                spec = iu.spec_from_file_location('OldBs.py', ""+v+"\\Data\\OldBs.py")
                foo = iu.module_from_spec(spec)
                spec.loader.exec_module(foo)
                    
            else:
                if not (a or b):
                    messagebox.showinfo("Error","Please Enter Your Username and Email")
                else:
                        messagebox.showinfo("Invalid Input","Username or Email or Password doesn't match any accounts")
                        
        finally:
            pass

#Button2's Command
def back():
    window.destroy()
    spec = iu.spec_from_file_location('Start.py', ""+v+"\\Data\\Start.py")
    foo = iu.module_from_spec(spec)
    spec.loader.exec_module(foo) 
#Buttons
b1=Button(window,text="Submit",command=lambda: fun(e1.get(),e2.get(),e3.get()),bd=3,bg="orange",activeforeground="orange").place(x=150,y=130)
b2=Button(window,text="Back",command=back,bd=3,bg="orange",activeforeground="orange").place(x=95,y=130)
window.bind('<Return>',lambda x:fun(e1.get(),e2.get(),e3.get()))
window.mainloop()

