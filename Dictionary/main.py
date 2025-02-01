import requests 
import win32com.client
import time

word = input("Enter a word to search it's meaning : ")

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
speaker = win32com.client.Dispatch("SAPI.SpVoice")
r = requests.get(url)
#print(r.json())

while True : 
    print("--------------------------------------------------------------------------------------------")
    print("1. Pronounciation")
    print("2. Meaning")
    print("3. Exit")
    b = int(input("Enter the number of option : "))
    time.sleep(1)
    
    if b == 1 : 
        print("Speaking.....")
        speaker.speak(word)
    elif b == 2 : 
        try: 
            examp = r.json()[0]["meanings"][0]["definitions"][0]["example"]
        except :
            examp = "<No Example to show>"
        meann = r.json()[0]["meanings"][0]["definitions"] 
        me = 1
        for i in meann:     
            for x in i : 
                if x == "definition" : 
                    mean = i[x]
                    print(f"Meaning {me}: {mean}")
                    me += 1
                    time.sleep(0.5)

        time.sleep(1)
        print(f"Example : '{examp}'")
    
    elif b == 3 :
        exit()
        
        


