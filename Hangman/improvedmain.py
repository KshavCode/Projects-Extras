import random
from time import sleep

class Hangman :
    def __init__(self):
        # Getting all the words stored in the txt file
        with open("words.txt") as f:
            wordList = f.read().strip().split()
            self.word = list(random.choice(wordList))
            
        self.lives = 6
        self.blankList = ["_" for _ in range(len(self.word))]
        self.guessedWordList = []
        
    def view(self):
        return (self.blankList, self.guessedWordList)
    
    def verify(self, char:str=""):
        if char in self.blankList or char in self.guessedWordList or char=="" : 
            return (self.blankList, self.guessedWordList)
        if char in self.word: 
            for i in range(len(self.word)):
                if self.word[i] == char:
                    self.blankList[i] = char
        else:
            self.guessedWordList.append(char)
            self.lives -= 1
        return (self.blankList, self.guessedWordList)

    def GameOver(self):
        # (GAMEOVER_CONDITION (T/F), WIN/LOSE/CONTINUE)
        # 10 = GameOver and NotGuessedTheWord
        # 11 = GameOver and GuessedTheWord
        # 00 = NotGameOver and NotGuessedTheWord, CONTINUE THE GAME
        if self.lives == 0:
            return "10"
        elif self.word == self.blankList:
            return "11"
        return "00"

    def reveal(self) :
        return "".join(self.word)
        
    def returnlives(self):
        return self.lives
    
if __name__ == "__main__" :
    obj = Hangman()
    gameOver = obj.GameOver()
    guessChar = ""
    while gameOver == "00":
        res = obj.verify(char=guessChar)
        sleep(.5)
        print("Lives remaining :", obj.returnlives())
        # Printing out the list condition one by one
        sleep(.5)
        for x in res[0] :
            print(x, end=" ")
        print()             # NEXT LINE
        print("Guessed List: ", end="")
        for x in res[1] :
            print(x, end=" ")
        print()             # NEXT LINE
        sleep(.5)
        if obj.GameOver()!="00":
            gameOver = obj.GameOver()
            break
        guessChar = input("Guess an alphabet: ")
        if not guessChar.isalpha() :
            print("Invalid alphabet, kindly try again!")
        elif len(guessChar) != 1 : 
            print("1 Alphabet at a time please!")
        sleep(.5)


    if gameOver == "10" :
        print("You lost all your lives! The word is :", obj.reveal())
    else : 
        print(f"You guessed the word correctly! Congrats!! You had {obj.returnlives()} live(s) remaining.")