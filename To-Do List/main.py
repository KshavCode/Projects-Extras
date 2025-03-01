import pandas as pd, os
import random

class ToDo : 
    def __init__(self, username, taskDetails):
        if not os.path.exists("data/tasks.csv") :
            os.mkdir("data")
            df = pd.DataFrame(columns=["username", "task", "uid"])
            df.to_csv("data/tasks.csv", index=False)
        self.uname = username 
        df1 = pd.read_csv("data/tasks.csv")
        if self.checkError() is True : 
            df2 = pd.DataFrame({"username":[self.uname], "task":[taskDetails], "uid":[self.genran()]})
            df1 = pd.concat([df1, df2], ignore_index=True)
            df1.to_csv("data/tasks.csv", index=False)
        else : 
            print(self.checkError())

    def checkError(self) : 
        if len(self.uname) >= 10 or len(self.uname) <= 3  : 
            return "Username cannot be more than 10 characters or lower than 3 characters."
        else : 
            return True
    
    def genran(self) : 
        lis1 = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "Z", "T", "B", "U", "E", "P", "K"]
        num = random.sample(range(13, 10000), 1)[0]
        unique = str(random.choice(lis1)) + str(num)
        df = pd.read_csv("data/tasks.csv")
        if unique in df["uid"] : 
            num = random.sample(range(4444, 5555), 1)[0]
            unique = unique + str(num)
        return unique
    
    def viewTask(self) :
        df1 = pd.read_csv("data/tasks.csv")
        if self.uname not in list(df1["username"]) :
            return "You don't have any tasks pending right now!"
        else : 
            database = df1[df1["username"]==self.uname]
            for i in range(len(database)) :
                print(database.iloc[i, 1], f"id : {database.iloc[i, 2]}", "\n", "-"*40)
            return f"{'_'*8}END{'_'*9}"
    
    def deleteTask(self, taskId) : 
        df1 = pd.read_csv("data/tasks.csv")
        lis = list(df1["uid"])
        if taskId not in lis : 
            return "Task with this id doesn't exist!"
        else : 
            place = lis.index(taskId)
            df = df1.drop(place, axis="index")
            df.to_csv("data/tasks.csv", index=False)
            return "Deleted successfully!"


    



print("___________________LOGIN_________________________")
a = input("Enter your username : ")
b = input("Provide a detail for your task : ")
print("_________________________________________________")
ob = ToDo(a, b)

while True : 
    print("Enter number of your choice : 1) Delete Task\n2) View Tasks\n3) End")
    choice = int(input())
    print("-"*45)
    if choice == 1 :
        i = input("Enter task ID to delete : ")
        print(ob.deleteTask(i))
    elif choice == 2 : 
        print(ob.viewTask())
    elif choice == 3 : 
        print("Logging off............")
        exit()
    else : 
        print("Wrong input!")




