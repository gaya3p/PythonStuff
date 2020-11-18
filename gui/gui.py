import db
from tkinter import *

class Table:
    def __init__(self, root):
        for i in range(rows):
            for j in range(columns):
                self.e = Entry(root, width=20)
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, records[i][j])

def add_record_window():
    global add_window
    add_window = Tk()
    
    Label(add_window, text='Insert Record').grid(row=0, column=0)
    Label(add_window, text='ID no. :').grid(row=1, column=0)
    Label(add_window, text='Name: ').grid(row=2, column=0)
    Label(add_window, text='Marks: ').grid(row=3, column=0)
    
    id_input = Entry(add_window)
    name_input = Entry(add_window)
    marks_input = Entry(add_window)
    
    id_input.grid(row=1, column=1)
    name_input.grid(row=2, column=1)
    marks_input.grid(row=3, column=1)
    
    # addCommand = lambda: [, ]
    
    submit_btn = Button(add_window, text='Submit',command=lambda:add_record(id_input.get(), name_input.get(), marks_input.get()))
    submit_btn.grid(columnspan=2, row=4, column=0)
    #add_window.bind('<Return>', addCommand)
    
def add_record(id_input, name_input, marks_input):
    db.insert_record(id_input, name_input, marks_input)
    add_window.destroy()
    update_table()

def update_table():
    records = records = db.read_records()
    rows = len(records)
    t = Table(root)
    root.mainloop()

# module
records = db.read_records()
rows = len(records)
columns = len(records[0])

#tkinter
root = Tk()
root.title('Students database recorder')

add_btn = Button(root, text='+', command=add_record_window)
add_btn.grid(row=0, column=1)

title = Label(root, text='Students')
title.grid(row=0, column=0)

t = Table(root)
root.mainloop()