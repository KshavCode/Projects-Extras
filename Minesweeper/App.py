import tkinter as tk, time, os
from MapMaker import MapGenerator
import tkinter.messagebox as tmb

def revealBombs():
    global obj, buttonList
    for x, y in obj.mineLocation:
        buttonList[x][y].config(text="💣", bg="#F08080")

def verifyScore(totalTime, hiscoreTime):
    tmb.showerror("FINISHED", f"YAYY, YOU FINISHED THE GAME :D\nIt took you {totalTime} seconds to complete!")
    if hiscoreTime=="N/A" or int(hiscoreTime) > totalTime:
        with open("highscore.txt", "w") as f:
            f.write(str(totalTime))
    
def recursiveOpen(x, y):
    global obj, buttonList, grids_active, gameOver, start, hiscoreTime
    if not gameOver:
        if buttonList[x][y].cget("text") != "":
            return
        if obj.map[x][y] != 0 : 
            if obj.map[x][y] == -1 :
                buttonList[x][y].config(text="💣")
                tmb.showerror("BOMB!", "You opened a tile containing mine! Game over :(")
                gameOver = True
                revealBombs()
                return
            buttonList[x][y].config(text=obj.map[x][y], bg="lightgreen")
            grids_active += 1
            if obj.safetiles == grids_active :
                totalTime = int(time.time()-start)
                verifyScore(totalTime, hiscoreTime)
            return
        buttonList[x][y].config(text=obj.map[x][y], bg="lightgreen")
        grids_active += 1
        if obj.safetiles == grids_active :
            totalTime = int(time.time()-start)
            verifyScore(totalTime, hiscoreTime)
            return
        if x!=obj.row-1: 
            recursiveOpen(x+1, y)
        if x!=0:
            recursiveOpen(x-1, y)
        if y!=obj.column-1: 
            recursiveOpen(x, y+1)
        if y!=0:
            recursiveOpen(x, y-1)
            
# MAIN PROGRAM STARTS HERE
root = tk.Tk()
root.geometry("600x600")
root.title("Minesweeper")
root.resizable(True, True)

obj = MapGenerator(10, 10)
buttonList = []

distancex = 45
distancey = 45
grids_active = 0
for i in range(obj.row) :
    subButtonList = []
    for j in range(obj.column) :
        but = tk.Button(root, text="", font=f"arial 18", width=3, command=lambda x=i, y=j: recursiveOpen(x, y), bg="#EEDC82", border=2, relief="solid")
        but.place(x=80+(distancex*i), y=110+(distancey*j))
        subButtonList.append(but)
    buttonList.append(subButtonList)

if not os.path.exists("highscore.txt"):
    with open("highscore.txt","w") as f:
        f.write("")
with open("highscore.txt") as f :
    hiscoreTime = f.read()
    if not hiscoreTime :
        hiscoreTime = "N/A"

gameOver = False
start = time.time()

hiscoreLabel = tk.Label(root, text=f"HighScore: {hiscoreTime} seconds", font="Verdana 20")
hiscoreLabel.place(x=150, y=40)
root.mainloop()