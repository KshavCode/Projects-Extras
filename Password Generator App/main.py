from tkinter import * 
from tkinter import messagebox
import pyperclip
import random

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}`~[];:'><,./?\|"
b = []

for i in a : 
    b.append(i)
print(b)

def generate() : 
    global b
    numb = int(chose.get())
    c = []
    for ii in range(1, numb+1) : 
        f = random.choice(b)
        c.append(f)
    passw = ""
    generate.passw = passw.join(c)
    a1.set(f"{generate.passw}")

    generate.but1 = Button(root, text="Copy to Clipboard!", command=copy)
    generate.but1.grid(row=4, column=0, padx=15)
    
def copy() : 
    pyperclip.copy(generate.passw)
    but2 = generate.but1
    but2.config(text="Copied!", state=DISABLED)

    
root = Tk()
root.geometry("300x200")
root.iconbitmap("photo\icon.ico")
root.resizable(False, False)

password = []

chose = StringVar()
a1 = StringVar() 
a1.set("Confirm password length first!")
chose.set("Length of Password")

choose = OptionMenu(root,  chose, "5", "6", "7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25")
resentry = Entry(root, textvariable=a1, state=DISABLED, width=30)
conf = Button(root, text="Confirm", width=7, bg="#008A39", fg="white", activebackground="#06B338", activeforeground="white", command=generate)

choose.grid(row=0, column=0, padx=70)
resentry.grid(row=1, column=0, padx=70, pady=28)
conf.grid(row=3, column=0)

root.mainloop()