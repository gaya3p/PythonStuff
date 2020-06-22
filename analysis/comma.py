import csv
from tkinter import *

root = Tk()

with open('magic.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        if row['Type'] == 'Curse':
            print(f"{row['Incantation']}:\t\t{row['Purpose']}")
   
