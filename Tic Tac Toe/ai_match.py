import random

# def display(arr:list)->None :
#     player_icon = 0
#     for i in range(3, 10, 3) :
#         print(arr[player_icon:i])
#         player_icon = i
#     print()

def game(player_icon="X") :
    moves = 0
    player1 = player_icon
    player2 = 0
    game_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random_list = list(range(9))

    player1 = player_icon
    if player1 == "X" : 
        player2 = "O"
    else : 
        player2 = "X"

    while True : 
        # display(game_state)
        player1_choice = random.choice(random_list)
        random_list.remove(player1_choice)
        game_state[player1_choice] = player1
        moves += 1
        if game_state[0]==game_state[1]==game_state[2] or game_state[3]==game_state[4]==game_state[5]   or game_state[6]==game_state[7]==game_state[8] or game_state[0]==game_state[3]==game_state[6]     or game_state[1]==game_state[4]==game_state[7] or game_state[2]==game_state[5]==game_state[8]   or game_state[0]==game_state[4]==game_state[8] or game_state[2]==game_state[4]==game_state[6] : 
            return 1
        if moves > 8 :
            return 0
        
        player2_choice = random.choice(random_list)
        random_list.remove(player2_choice)
        game_state[player2_choice] = player2
        moves += 1
        if game_state[0]==game_state[1]==game_state[2] or game_state[3]==game_state[4]==game_state[5] or game_state[6]==game_state[7]==game_state[8] or game_state[0]==game_state[3]==game_state[6] or game_state[1]==game_state[4] ==game_state[7] or game_state[2]==game_state[5]==game_state[8] or game_state[0]==game_state[4]==game_state[8]  or game_state[2]==game_state[4]==game_state[6] : 
            return 2
        if moves > 8 :
            return 0
        

result_list = [0, 0, 0]
totalmatches = 1000
for i in range(totalmatches) :
    result = game()
    result_list[result] += 1

# print("Ties :", result_list[0])
# print("Player 1 Wins :", result_list[1])
# print("Player 2 Wins :", result_list[2])
# print("Total Matches :", sum(result_list))
print("Ties Probablity:", result_list[0]/totalmatches)
print("Player 1 Probablity:", result_list[1]/totalmatches)
print("Player 2 Probablity:", result_list[2]/totalmatches)

