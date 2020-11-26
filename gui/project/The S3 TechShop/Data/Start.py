from tkinter import *

import os
v=os.getcwd()

import importlib.util as iu

#Tkinter Window Creation
window=Tk()
window.resizable(width=False, height=False)
window.title("(S)3 Geeky TechShop Cum Benchmark")
window.geometry("520x293+350+140")

#Background Image
img=PhotoImage(file=r""+v+"\Data\Start.png")
w=Label(window,image=img).pack()


#Button1's Function
def fun():
    window.destroy()
    
    spec = iu.spec_from_file_location('NewBs.py', ""+v+"\\Data\\NewBs.py")
    foo = iu.module_from_spec(spec)
    spec.loader.exec_module(foo)
    
#Button2's Function    
def fun2():
    window.destroy()
    spec = iu.spec_from_file_location('Verify.py', ""+v+"\\Data\\Verify.py")
    foo = iu.module_from_spec(spec)
    spec.loader.exec_module(foo)
    
       
#Buttons    
b1=Button(window,text="Login",command=fun2,bd=3,bg="orange",activeforeground="orange").place(x=200,y=250)
b2=Button(window,text="Register",command=fun,bd=3,bg="orange",activeforeground="orange").place(x=290,y=250)

window.mainloop()
