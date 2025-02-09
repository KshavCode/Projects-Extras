import tkinter as tk
import tkinter.messagebox as tmb
from improvedmain import Hangman
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("500x500")
root.title("Hangman")
# root.resizable(False, False)

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

def checkalpha(num) :
    global obj, lab, img, imageNum
    global alphabetList, blankListLabel, alphaButtonList
    WholeList = obj.verify(alphabetList[num])[0]
    currentLives = obj.returnlives()
    img = ImageTk.PhotoImage(Image.open(f"images/{currentLives}.png").resize((220, 220)))
    lab.config(image=img)
    for x in range(len(blankListLabel)):
        blankListLabel[x].config(text=WholeList[x])
    if obj.GameOver() != "00": 
        for but in alphaButtonList:
            try:
                but.config(state="disabled")
            except:
                continue
        if obj.GameOver()=="10":
            string = f"You failed to guess the word and lost all your lives! The word was '{obj.reveal()}'"
        else : 
            string = f"You finished the game and guessed the word correctly! You had {obj.returnlives()} remaining lives!"
        res = tmb.askokcancel(title="GAME OVER", message=string)
        if res or not res:
            quit()
    alphaButtonList[num].destroy()

    
    
obj = Hangman()
blankListLabel = []
WholeList = obj.view()
for blankIndex in range(len(WholeList[0])):
    blankLabel = tk.Label(root, text=WholeList[0][blankIndex], font="arial 25")
    blankLabel.place(x=170+(blankIndex*30), y=230)
    blankListLabel.append(blankLabel)
    
alphaButtonList = []
for i in range(len(alphabetList)//2) :
    alphabutton = tk.Button(root, text=alphabetList[i], font="Garamond 14", width=2, command=lambda x=i: checkalpha(x)) 
    alphabutton.place(x=10+(i*37), y=350)
    alphaButtonList.append(alphabutton)

for i in range(len(alphabetList)//2, len(alphabetList)) :
    alphabutton = tk.Button(root, text=alphabetList[i], font="Garamond 14", width=2, command=lambda x=i: checkalpha(x)) 
    alphabutton.place(x=10+((i-len(alphabetList)//2)*37), y=400)
    alphaButtonList.append(alphabutton)
    
img = ImageTk.PhotoImage(Image.open(f"images/6.png").resize((220, 220)))
lab = tk.Label(root, image=img)
lab.place(x=160, y=10)

root.mainloop()