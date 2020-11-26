from tkinter import *
from tkinter import messagebox
import importlib.util as iu

import os
v=os.getcwd()

#Tkinter Window Creation
window=Tk()
window.resizable(width=False, height=False)
window.title("Order")
window.geometry("520x290+350+140")

import mysql.connector
m=mysql.connector.connect(host="localhost",user="root",passwd=pas,database="TechShop")
mc=m.cursor()

mc.execute("select * from products")
t=mc.fetchall()

#Frame
f= Frame(window)
f.pack()

# Display Table
from Table import *
table = Table(window, ["ID", "Product Name","Stock ","₹"], column_minwidths=[None, None, None,None])
table.set_data(t)
table.place(x=245,y=75)

#Background Image
img=PhotoImage(file= r""+v+"\Data\OldB.png")
w=Label(f,image=img).pack()

#Labels
to_buy=Label(window,text="Product Code").place(x=15,y=90)
quantity=Label(window,text="Quantity ").place(x=15,y=140)
advance=Label(window,text="Payment ").place(x=15,y=180)

tot=StringVar()
tot.set('0')

#Entries
e1=Entry(window,bd=4)
e1.place(x=115,y=90)
e2=Entry(window,bd=4)
e2.place(x=115,y=140)
e3=Entry(window,bd=4)
e3.place(x=115,y=180)
e4=Entry(window,bd=4,state='disabled',textvariable=tot)
e4.place(x=290,y=38)

#Button1's Command
def do():
    val1=e1.get()
    val2=e2.get()
    val3=e3.get()

    if val2=='':
        val2='0'

    if val3=='':
        val3='0'

    try:
        mc.execute("select Price_Per_Unit from products where ID=('"+val1+"')")
        multiplier=mc.fetchall()
        val4=str(int(multiplier[0][0]) * int(val2))

        if __name__ == '__main__':
            import Verify
            mc.execute("select Due from buyers where Email=('"+em+"')")
            d=mc.fetchall()
        if len(val1)!=0:
            mc.execute("select Stock from products where ID=('"+val1+"') ")
            curr_stock=mc.fetchall()
            new_stock=str(int(curr_stock[0][0]-int(val2)))

            mc.execute("select Due from buyers where Email=('"+em+"')")
            d=mc.fetchall()
            if int(d[0][0])==0:
                if 0<= int(val2) <= int(curr_stock[0][0]):
                    new_stock=str(int(curr_stock[0][0]-int(val2)))
                    mc.execute("update buyers set Product_ID=('"+val1+"'),Units_Purchased=('"+val2+"'),Total=('"+val4+"'),Advance=('"+val3+"') where Email=('"+em+"')")
                    mc.execute("update products set Stock='"+new_stock+"' where ID=('"+val1+"')")
                    m.commit()
                
                    messagebox.showinfo("Hey There !","Congratulations For Your Purchase")
                    window.destroy()
                
                    spec = iu.spec_from_file_location('Start.py', ""+v+"\\Data\\Start.py")
                    foo = iu.module_from_spec(spec)
                    spec.loader.exec_module(foo)
                else:
                    messagebox.showinfo("Oops !","Product Selected Is Out Of Stock")
            else:
                messagebox.showinfo("Due","You have dues to pay")

        else:
            messagebox.showinfo("Error","Check If every Detail is Filled Or Not")
            
    except:
        messagebox.showinfo("Error","Invalid Producut Code Used")

#Button2's Command
def back():
    window.destroy()
    spec = iu.spec_from_file_location('Start.py', ""+v+"\\Data\\Start.py")
    foo = iu.module_from_spec(spec)
    spec.loader.exec_module(foo)

#Button3's Command
def his():
    mc.execute("select Name,Product_ID,Units_Purchased,Total,Advance,Due from buyers where Email=('"+em+"')")
    h = mc.fetchall()

    winh=Toplevel()
    winh.resizable(width=False, height=False)
    winh.title("History")
    winh.geometry("395x120+420+230")
    
    tab = Table(winh, ["Name","Product ID","Quantity","Total","Payment","Due"], column_minwidths=[None, None, None,None,None,None])
    tab.set_data(h)
    tab.place(x=1,y=1)

    def close():
        winh.destroy()

    b=Button(winh,text="Okay",command=close,bd=3,bg="orange",activeforeground="orange").place(x=180,y=90)
    
    winh.mainloop()

#Button4's Command
def total():
    val1=e1.get()
    val2=e2.get()

    if val2=='':
        val2='0'

    if val1=='':
        messagebox.showinfo("Hey Dumbo!","No Product Is Selected")
    else:
        mc.execute("select Price_Per_Unit from products where ID=('"+val1+"') ")
        multiplier=mc.fetchall()
        val=str(int(multiplier[0][0]) * int(val2))
        tot.set(val)
    
#Buttons
b1=Button(window,text="Submit",command=do,bd=3,bg="orange",activeforeground="orange").place(x=225,y=230)
b2=Button(window,text="Back",command=back,bd=3,bg="orange",activeforeground="orange").place(x=170,y=230)
b3=Button(window,text="History",command=his,bd=3,bg="orange",activeforeground="orange").place(x=290,y=230)
b4=Button(window,text='Total',command=total,bd=3,bg="orange",activeforeground="orange").place(x=430,y=35)
window.bind('<Return>',lambda x:do())
window.mainloop()

