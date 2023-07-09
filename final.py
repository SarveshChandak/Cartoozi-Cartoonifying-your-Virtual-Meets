import sys
import os
from tkinter import *

window=Tk()

window.title("Cartozi")
window.iconbitmap('Cartozi.ico')
window.geometry('600x300')
backg=PhotoImage(file='bg.png')
label1= Label (window, image =backg)
label1.place(x=0,y=0)

def run1():
    os.system('python "emojifier-python-project.py"')
def run2():
    os.system('python "cartoonifier-python-project.py"')
btn1= Button(window, text="Face to Emotes",bg="blue", fg="white",command=run1)
btn1.configure(background='#364156',font=('calibri',20,'bold'), width=30)
btn1.place(x=90,y=95)
btn2= Button(window, text="Cartoonify!", bg="blue", fg="white",command=run2)
btn2.configure(background='#364156',font=('calibri',20,'bold'), width=30)
btn2.place(x=90, y=195)

window.mainloop()