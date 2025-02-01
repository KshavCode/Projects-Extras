import tkinter as tk


# Create HANGMAN using buttons 
root = tk.Tk()
root.geometry("500x500")
root.title("Hangman")

def button(n:int) :
    print(n)
    
def word_generator() : 
    return "insect", ["e", "n"]

word = word_generator()
avheight = (500/len(word)) - 220
xINC = 30
for i in range(len(word[0])) :
    if word[0][i] not in word[1] :
        but = tk.Button(root, text="_", command=lambda i=i:button(i), font="arial 13")
    else : 
        but = tk.Button(root, text=word[0][i], command=lambda i=i:button(i), font="arial 13")
    but.place(x=xINC+(avheight*i), y=50)

root.mainloop()