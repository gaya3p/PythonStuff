from tkinter import *

root = Tk()

l = Label(root, text='hey now')
m = Label(root, text='youre an all star')
b = Button(root, text='bomb', command=print('3'))

l.grid(row=0, column=0)
m.grid(row=1, column=0)
b.grid(row=2, column=0)

root.mainloop()