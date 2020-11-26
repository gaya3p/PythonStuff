from tkinter import *
from tkinter import messagebox
import importlib.util as iu

import os
c=os.getcwd()

#Tkinter Window Creation
window=Tk()
window.resizable(width=False, height=False)
window.title("Sign Up And Order")
window.geometry("520x290+350+140")


import mysql.connector
m=mysql.connector.connect(host="localhost",user="root",passwd='alohomora',database="TechShop")
mc=m.cursor()
mc.execute("select * from products")
t=mc.fetchall()

#Frame For Image 
f= Frame(window)
f.pack()

# Display Table
from Table import *
table = Table(window, ["ID", "Product Name","Stock","₹"], column_minwidths=[None, None, None, None])
table.set_data(t)
table.place(x=246,y=72)

#Background Image
img=PhotoImage(file= r""+c+"\Data\OldB.png")
Label(f,image=img).pack()

# Entry Labels
name=Label(window,text="Create Username").place(x=22,y=42)
email=Label(window,text="Your Email ").place(x=30,y=70)
product_id=Label(window,text="Product Code ").place(x=28,y=145)
quantity=Label(window,text="Quantity ").place(x=30,y=180)
advance=Label(window,text="Payment ").place(x=30,y=215)
Paswd=Label(window,text="Password ").place(x=30,y=110)

tot=StringVar()
tot.set('0')

# Entries
e1=Entry(window,bd=4)
e1.place(x=115,y=42)
e2=Entry(window,bd=4)
e2.place(x=115,y=72)
e3=Entry(window,bd=4)
e3.place(x=115,y=144)
e4=Entry(window,bd=4)
e4.place(x=115,y=180)
e5=Entry(window,bd=4)
e5.place(x=115,y=215)
e6=Entry(window,bd=4,show='*')
e6.place(x=115,y=110)
e7=Entry(window,bd=4,state='disabled',textvariable=tot)
e7.place(x=290,y=38)

# Button1's Command
def fun():
    val1=e1.get()
    val2=e2.get()
    val3=e3.get()
    val4=e4.get()
    val5=e5.get()
    paswd=e6.get()

    if val3=='':
        val3='0'
    if val4=='':
        val4='0'
    if val5=='':
        val5='0'

    mc.execute("select Price_Per_Unit from products where ID=('"+val3+"') ")
    multiplier=mc.fetchall()
    val6=str(int(multiplier[0][0]) * int(val4))
                    
    mc.execute("select Stock from products where ID=('"+val3+"') ")
    curr_stock=mc.fetchall()
        
    try:
        if len(val1)!=0 and len(val2)!=0:
            
            if 0 <= int(val4) <= int(curr_stock[0][0]):
                new_stock=str(int(curr_stock[0][0]-int(val4)))

                mc.execute("insert into buyers(Name,Email,Password,Product_ID,Units_Purchased,Total,Advance) values('"+val1+"','"+val2+"','"+paswd+"','"+val3+"','"+val4+"','"+val6+"','"+val5+"')")
                mc.execute("update products set Stock='"+new_stock+"' where ID=('"+val3+"')")
                m.commit()
                messagebox.showinfo("Hey There !","Congratulations For Your Purchase")
                window.destroy()
                spec = iu.spec_from_file_location('Start.py', ""+c+"\\Data\\Start.py")
                foo = iu.module_from_spec(spec)
                spec.loader.exec_module(foo)
            else:
                messagebox.showinfo("Oops !","Product Selected Is Out Of Stock")
        else:
            messagebox.showinfo("Error","Email And Name must be Filled")
        
    except:
        messagebox.showinfo("Error","Account Already Exists")

# Button2's Command
def back():
    window.destroy()
    spec = iu.spec_from_file_location('Start.py', ""+c+"\\Data\\Start.py")
    foo = iu.module_from_spec(spec)
    spec.loader.exec_module(foo)

# Button3's Command
def total():
    val1=e3.get()
    val2=e4.get()

    if val2=='':
        val2='0'
    
    if val1=='':
        messagebox.showinfo("Hey Dumbo!","No Product Is Selected")
    else: 
        mc.execute("select Price_Per_Unit from products where ID=('"+val1+"') ")
        multiplier=mc.fetchall()
        val=str(int(multiplier[0][0]) * int(val2))
        tot.set(val)
                    
# Buttons       
b1=Button(window,text="Submit",command=fun,bd=3,bg="orange",activeforeground="orange").place(x=280,y=250)
b2=Button(window,text="Back",command=back,bd=3,bg="orange",activeforeground="orange").place(x=190,y=250)
b3=Button(window,text='Total',command=total,bd=3,bg="orange",activeforeground="orange").place(x=430,y=35)
window.bind('<Return>',lambda x:fun())
window.mainloop()
 
