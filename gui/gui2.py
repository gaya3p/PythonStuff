import tkinter as tk
import f as db

class MainApplication:
    def __init__(self, master):
        ''''main window labels, entries, buttons'''
        self.master = master
        master.title('Students database recorder')
        
        self.add_btn = tk.Button(master, text='+', command=self.add_window)
        self.add_btn.grid(row=0, column=1)
        
        self.title = tk.Label(master, text='Students')
        self.title.grid(row=0, column=0)
        
        self.tableFrame = tk.Frame(master)
        self.tableFrame.grid(row=1, column=0)
        
        self.update_table() 
        self.master.bind('<Button-3>', self.add_menu)
        
    def add_menu(self, event):
        menu = tk.Menu(self.master, tearoff=0)
        menu.add_command(label='Edit')
        x, y = event.x_root, event.y_root
        menu.add_command(label='Delete', command=lambda: print(tk.grid_location(x, y)) )
        menu.tk_popup(event.x_root, event.y_root)
        menu.grab_release()
        
        
    
    def update_table(self):
        print('updated')
        self.records = db.read_records()
        print('new updated: ', self.records)
        # print(self.records)
        self.rows = len(self.records)
        try:
            self.columns = len(self.records[0])
        except IndexError:
            error_msg = tk.Label(self.tableFrame, text='no records')
            error_msg.grid(row=5, column=0)
            self.columns = 0
            
        # new stuff
        for widget in self.tableFrame.winfo_children():
            widget.destroy()
            print(widget)
        
        self.add_table()    


    def add_table(self):
        values = ['Id', 'Name', 'Marks']
        
        for i in range(3):
            self.e = tk.Entry(self.tableFrame, width=20, readonlybackground='#fff')#, state='disabled')
            self.e.grid(row=1, column=i)
            self.e.insert(0, values[i])
            self.e.config(state='readonly')
        for i in range(self.rows):
            for j in range(self.columns):
                self.e = tk.Entry(self.tableFrame, width=20, readonlybackground='#fff')
                self.e.grid(row=i+2, column=j)
                self.e.insert(0, self.records[i][j])
                self.e.config(state='readonly')
                
                if j == 2:
                    print(self.records[i][1])
                    roll = int(self.records[i][0])
                    self.btn = tk.Button(self.tableFrame, text='x',
                                         command=lambda roll=roll: self.delete_record(roll))
                    self.btn.grid(row=i+2, column=3)
        # for i in range(self.rows):
        #     self.e = tk.Button(self.master, text='x', command=lambda: self.delete_record(i),
        #                        height=1, pady=0)
        #     self.e.grid(row=i+2, column=4)
            
    def delete_record(self, i):
        print(i, type(i))
        db.delete_record(int(i))
        self.update_table()

    def add_window(self):
        '''if clicked open new window'''
        self.addWindow = tk.Toplevel(self.master)
        self.app = AddWindow(self.addWindow)
        self.update_table()
        # print(type(self.master))

class AddWindow:
    def __init__(self, master):
        '''new window fixed stuff'''
        self.master = master
        
        tk.Label(master, text='Insert Record').grid(row=0, column=0)
        tk.Label(master, text='ID no. :').grid(row=1, column=0)
        tk.Label(master, text='Name: ').grid(row=2, column=0)
        tk.Label(master, text='Marks: ').grid(row=3, column=0)
        
        self.id_input = tk.Entry(master)
        self.name_input = tk.Entry(master)
        self.marks_input = tk.Entry(master)
        
        self.id_input.grid(row=1, column=1)
        self.name_input.grid(row=2, column=1)
        self.marks_input.grid(row=3, column=1)
        
        self.submit_btn = tk.Button(self.master, text = 'submit',
                                    command = self.save_record)
        self.submit_btn.grid(columnspan=2, row=4, column=0)
        self.master.bind('<Return>', self.save_record)
        
    def save_record(self, _event=None):
        '''close new window'''
        Id = self.id_input.get()
        name = self.name_input.get()
        marks = self.marks_input.get()
        
        db.insert_record(Id, name, marks)
        
        self.parent = MainApplication(root)
        self.parent.update_table()
        self.master.destroy()
        print('master: ', self.master)
        # MainApplication.update_table(self)

def main(): 
    global root
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()