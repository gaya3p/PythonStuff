from tkinter import *
root = Tk()

def saveNote(content):
    print(content)

content_input = Text(root)
content_input.grid(row=0, column=0)
content = content_input.get(1.0, END)

save_btn = Button(root, text='Save', command=lambda: saveNote(content_input.get(1.0, END)))
save_btn.grid(row=0, column=1)

root.mainloop()


