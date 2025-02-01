from tkinter import * 
from tkinter.messagebox import *

# INITIALIZATION
window = Tk()
window.geometry("600x450")
window.title("TicTacToe")
moves = 0
button_number = 0
buttons_list = []
game_state = list(range(9))
    
# FUNCTIONS
def check_game(x) :
    global buttons_list, game_state, moves
    if (game_state[0]==game_state[1]==game_state[2] or game_state[3]==game_state[4]==game_state[5] or game_state[6]==game_state[7]==game_state[8] or game_state[0]==game_state[3]==game_state[6] or game_state[1]==game_state[4]==game_state[7] or game_state[2]==game_state[5]==game_state[8] or game_state[0]==game_state[4]==game_state[8] or game_state[2]==game_state[4]==game_state[6]) : 
        for i in buttons_list :
            i.config(state=DISABLED)
        showinfo("Winner", f"{game_state[x]} Wins!")
    elif moves ==9 :
        showinfo("Tie", "It's a Tie!")

def change_button(x) :
    global moves, buttons_list
    if moves%2==0 :
        buttons_list[x].config(text="❌", state=DISABLED, background="white")
        game_state[x] ="❌"
    else :
        buttons_list[x].config(text="⭕", state=DISABLED, background="white")
        game_state[x] ="⭕"
    moves += 1
    check_game(x)
    

# MAIN
for i in range(3) :
    for j in range(3) :
        buttons_list.append(Button(window, text="", width=3, command=lambda x=button_number:change_button(x), font="arial 50", background="#ffa3a3"))
        buttons_list[button_number].grid(row=i, column=j, padx=5, pady=5)
        button_number += 1
label1 = Label(window, text="Press any key to restart", font="arial 15", wraplength=150)
label1.grid(row=1, column=3, padx=30)

def reset_game(e) :
    global moves
    for i in range(9) :
        buttons_list[i].config(text="", state=NORMAL, background="#ffa3a3")
        game_state[i] = i
        moves = 0

window.bind("<KeyPress>", reset_game)
window.mainloop()