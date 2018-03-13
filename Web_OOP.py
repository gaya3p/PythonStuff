import tkinter as tk
import webbrowser

g = "Arial"
window = tk.Tk()
window.geometry("500x500")

#______________________________________________________________
# Buttons are linked over here
def doorbell(event):
    webbrowser.open_new_tab('file:///C:/Users/Gayathri/Desktop/CHASEBOOK.com/ChaseBook%20Home%20page.htm')
    for i in range(20):
        print("$800 deducted from your bank account.")

def open_KA(event):
    webbrowser.open_new_tab('https://www.khanacademy.org/profile/gay3p/')
    for i in range(20):
        print("Sal Khan is $800 richer!")

    
def open_FB(event):
    webbrowser.open_new_tab('www.facebook.com')
    for i in range(20):
        print("Mark Zukenburg is $800 richer!")

def KA(event):
    print("Sal Khan is $800 richer!")
def FB(event):
    print("Mark Zukenburg is $800 richer!")

def close_win(event):
    window.destroy()

#______________________________________________________________
#Fruits
lab = tk.Label(text="Chasebook:", font=g, foreground="red")
lab.grid(column=0, row=0)

lab_b = tk.Label(text="Khan Academy:", font=g, foreground="green")
lab_b.grid(column=0, row=1)

lab_c = tk.Label(text="Facebook:", font=g, foreground="blue")
lab_c.grid(column=0, row=2)

#______________________________________________________________
#Buttons
button = tk.Button(window, text="Give me some money...", font=g)
button.grid(column=1, row=0)

button_b = tk.Button(window, text="Give Sal Khan some money...", font=g)
button_b.grid(column=1, row=1)

button_c = tk.Button(window, text="Give Mark Zuckenburg some money...", font=g, foreground="blue")
button_c.grid(column=1, row=2)

BUTTON = tk.Button(window, text='Close', font="TimesNewRoman", relief="sunken")
BUTTON.grid(column=3, row=6)

#______________________________________________________________
#BINDING them
button.bind("<Button-1>", doorbell)
button_b.bind("<Button-1>", open_KA)
button_c.bind("<Button-1>", open_FB)
button_b.bind("<Button-3>", KA)
button_c.bind("<Button-3>", FB)
BUTTON.bind("<Button-1>", close_win)


#______________Execute Them!!!!!!!!!!!!!_______________________
window.mainloop()
