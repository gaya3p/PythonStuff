def popupmsg(msg):
    import tkinter as tk
    popup = tk.Tk()
    popup.resizable(width=False, height=False)
    popup.title("Terms And Conditions")
    popup.geometry("1300x430+30+150")
    
    l = tk.Label(popup, text='Terms And Conditions',fg='black', font='Harrington 18 bold')
    l.pack()

    c = tk.Canvas(popup,bg = "white",width="1000",height = "400")
    canvas_id = c.create_text(10, 10, anchor="nw")
    c.pack(fill="both")

    c.itemconfig(canvas_id, text=msg,font=(0,0,'bold'))
    c.insert(canvas_id, 100, " ")

    def do():
        popup.destroy()
        import os
        v=os.getcwd()
        
        import importlib.util as iu
        spec = iu.spec_from_file_location('sql.py', ""+v+"\\Data\\sql.py")
        foo = iu.module_from_spec(spec)
        spec.loader.exec_module(foo)

    b = tk.Button(popup, text="Yes",font='times 0 bold',bd=3,width=4,bg="orange",command = do).place(x=590,y=380)
    b1 = tk.Button(popup, text="No",font='times 0 bold',bd=3,width=4,bg="orange",command = popup.destroy).place(x=655,y=380)
    popup.mainloop()

import os
p=os.getcwd()
fl=open(''+p+'\\Data\\Readme.txt','r')
popupmsg(fl.read())
