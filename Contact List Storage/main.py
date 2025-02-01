class Contact : 
    def __init__(self) :
        self.con_lis = {}
        
    def save(self, number, name) : 
        self.con_lis[number] = name
        
    def delete(self, number) : 
        if number not in self.con_lis.keys() : 
            print("No such number found in the contact list")
        else : 
            del self.con_lis[number]
            
    def contacts(self) : 
        for i, j in self.con_lis.items() : 
            print("-------------------")
            print(f"{i} ({j})")
            print("-------------------")


a=Contact()
while True : 
    while True : 
        b = int(input("Do you want to : \n1. Save a number\n2. Delete a number\n3. Get the contacts list\n4. Exit "))
        if b == 1 : 
            c = input("Enter the phone number : ")
            if not int(c) : 
                print("Why no digits?")
            else : 
                if len(c) == 10 : 
                    d = input("Enter the name with which you want to save the contact number : ")
                    a.save(c, d)
                    break
                else : 
                    print("Not the correct mobile phone number. 10 digits should be there in a phone number.")

        elif b == 2 :
            e = input("Enter the phone number : ")
            if len(e) == 10 : 
                try : 
                    e = int(e)
                    a.delete(e)
                    break
                except : 
                    print("That's not a valid number, I think.")
            else : 
                print("Didn't you know that there are 10 digits in indian phone numbers?")
        elif b == 3 : 
            a.contacts()
            break
        elif b == 4 : 
            print("Closing the application.")
            exit()
        else : 
            print("It's an invalid choice.")
            
    
            
            
        
            
        
        

a.save(987282828, "Rahul")
a.save(9745463229, "Jahul")
a.contacts()
        
              