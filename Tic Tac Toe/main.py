from tabulate import tabulate 

play1 = []
play2 = []
choice = ["X", "O"]
guesslis = [0, 1, 2, 3, 4, 5, 6, 7, 8]

while True : 
        print("Choose your symbol player 1 : ")
        sym = (input()).upper()
        if sym not in choice : 
            print("Choose either X or O!")
            continue
        else : 
            play1.append(sym)
            if play1[0] == "X" : 
                play2.append("O")
            else : 
                play2.append("X")
            break

flag = True
while True : 
    if flag == False : 
        break
    data = [[guesslis[0], guesslis[1], guesslis[2]], [guesslis[3],guesslis[4],guesslis[5]], [guesslis[6],guesslis[7],guesslis[8]]]
       
    if guesslis[0]==guesslis[1]==guesslis[2] or guesslis[3]==guesslis[4]==guesslis[5] or guesslis[6]==guesslis[7]==guesslis[8] or guesslis[0]==guesslis[3]==guesslis[6] or guesslis[1]==guesslis[4]==guesslis[7] or guesslis[2]==guesslis[5]==guesslis[8] or guesslis[0]==guesslis[4]==guesslis[8] or guesslis[2]==guesslis[4]==guesslis[6] : 
        print("Game finished!")
        print("Player 2 Wins!")
        break

    
    print(f"Player 1 chose {play1[0]}\nPlayer 2 chose {play2[0]}\n")
    print(tabulate(data, tablefmt="grid"))
    while True : 
        player1 = int(input("Player 1 turn : "))
        if player1 > 8 or player1 < 0: 
            print("Out of range position")
            continue
        else : 
            if guesslis[player1] == "X" or guesslis[player1] == "O" : 
                print("The position is already taken!")
            else : 
                guesslis[player1] = play1[0]
                data = [[guesslis[0], guesslis[1], guesslis[2]], [guesslis[3],guesslis[4],guesslis[5]], [guesslis[6],guesslis[7],guesslis[8]]]
                print(tabulate(data, tablefmt="grid"))
                if guesslis[0]==guesslis[1]==guesslis[2] or guesslis[3]==guesslis[4]==guesslis[5] or guesslis[6]==guesslis[7]==guesslis[8] or guesslis[0]==guesslis[3]==guesslis[6] or guesslis[1]==guesslis[4]==guesslis[7] or guesslis[2]==guesslis[5]==guesslis[8] or guesslis[0]==guesslis[4]==guesslis[8] or guesslis[2]==guesslis[4]==guesslis[6] : 
                    print("Game finished!")
                    print("Player 1 Wins!")
                    flag = False
                break
    if flag == False : 
        break
    
    while True : 
        player2 = int(input("Player 2 turn : "))
        if player2 > 8 or player2 < 0 : 
            print("Out of range position")
        else :
            if guesslis[player2] == "X" or guesslis[player2] == "O" : 
                print("The position is already taken!")
                continue
            else : 
                guesslis[player2] = play2[0]
                break
             
             
            
            
        