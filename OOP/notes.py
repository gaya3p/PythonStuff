import mysql.connector as sq
from tkinter import *

fontHead = ('CircularStd', '15')
fontBody = ('Circular Std Book', '12')

root = Tk()
root.title('Remembrall')
root.geometry('250x150')

db = sq.connect(host='localhost', user='root', passwd='alohomora')
cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS notesdb')
db.commit()
cursor.execute('USE notesdb')
db.commit()

table = 'notes(id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255),contents TEXT)'
cursor.execute(f'CREATE TABLE IF NOT EXISTS {table}')

sql = "INSERT INTO notes (title, contents) VALUES (%s, %s)"
val = ('a', 'content')
cursor.execute(sql, val)
db.commit()

# Add existing notes
cursor.execute('SELECT * FROM notes')
notes = cursor.fetchall()
total_notes = len(notes)
print(total_notes)

for note in notes:
    i, title_txt, content_txt = note
    
    title = Button(root, text=title_txt, font=fontBody, command=lambda i=i: openNote(i))
    title.grid(row=i, column=0)
    
def openNote(i):
    note = notes[i-1]
    note_window = Toplevel()
    note_window.wm_title('Remembrall')
    
    i, title_txt, content_txt = note
    
    title_label = Label(note_window, text = title_txt, font=fontHead)
    content_label = Label(note_window, text = content_txt, font=fontBody)
    
    title_label.grid(row=0,column=0)
    content_label.grid(row=1, column=0)

# name
name = Label(root, text='Remembrall', font=fontHead)
name.grid(row=0, column=0)

# Add new note
def saveNote(title, content):
    sql = "INSERT INTO notes (title, contents) VALUES (%s, %s)"
    val = (title, content)
    cursor.execute(sql, val)
    db.commit()

def newNote():
    i = total_notes+1
    new_window = Toplevel()
    new_window.wm_title('Remembrall')
    
    title_input = Entry(new_window)
    content_input = Text(new_window)
    
    title_input.grid(row=0, column=0)
    content_input.grid(row=1, column=0)
    
    title = title_input.get()
    content = content_input.get(1.0, END)
    
    save_btn = Button(new_window, text='Save', command=lambda: saveNote(title_input.get(), content_input.get(1.0, END)))
    save_btn.grid(row=0, column=1)
    
    
addBtn = Button(root, text='Add', font=fontBody, command=newNote)
addBtn.grid(row=0, column=1)


db.close()
root.mainloop()