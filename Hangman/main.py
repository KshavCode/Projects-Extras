import random, time, datetime


class HangMan : 
    def __init__(self, name, length):
        self. name = name 
        self.life = 6
        self.length = length
        
        if self.length == 4 : 
            self.wordlis = ["tree", "bark", "free", "pray", "your", "flow", "flee", "dumb", "save", "kick", "care"]
        elif self.length == 5 : 
            self.wordlis = ["trunk", "year", "hour", "ouija", "sharp", "slice", "price", "shelf", "seize", "jazzy", "lunch", "faith", "other", "about", "maybe", "clown", "cloth", "eager", "abort", "feria", "issue", "match", "mercy", "round", "solid", "scare", "wadge", "track", "today", "stoun", "solid", "algae", "baldy", "board", "burry","bytes",  "cigar", "clang", "cocoa", "conga", "crazy", "draft", "grass", "goofy", "horde", "jelly", "jiggy", "liver", "loser", "mouse", "piano", "plump", "retry", "round", "roughe", "salon", "salsa", "santo", "seedy", "sedge", "shear", "sirup", "smile", "snipe", "snowy", "soupy", "spoil", "teach", "teddy", "union", "verbs", "voter", "vowel", "whale", "while", "whose", "woald", "wodge", "xylem", "yahoo", "yards", "shawl", "yeast", "youth", "xerox", "wrack", "wheat", "vocal", "upbow", "upper", "ankle", "apple", "mango", "boost", "break", "brass", "cheap", "clash"]
        elif self.length == 6 : 
            self.wordlis = ["legend", "monkey", "dexter", "thread", "suburb", "isobar", "saliva", "orphan", "action", "bridge", "hornet", "pistol", "demand", "finger", "puppet", "thrust", "nuzzle", "joyful", "zipper", "chunky", "zygote", "phloem", "aboard", "appear", "animal", "banner", "battle", "basket", "casual", "casino", "cement", "carpet", "endure", "enzyme", "gamble", "farmer", "ginger", "averse","raddle",  "except", "reader", "system", "supper", "detour", "remove", "factor", "luxury", "behind", "asylum", "hybrid", "blonde", "lesson", "reduce", "gentle", "course", "archer", "glance", "outlay", "camera", "beauty", "freeze", "remord", "nymph", "stingy", "byssus", "junior", "wizard", "regret", "tinsel", "pencil", "pencel", "aurora", "stripe", "insult", "feeble", "appear", "driver", "flinch", "groove", "unbent", "misuse", "psyche", "handle", "jacket", "shield", "mammal", "podium", "glycol", "latter", "letter", "common", "router", "church", "agency", "rammel", "winter", "scheme", "disarm", "mizzle", "nectar", "museum"]
        elif self.length == 7 : 
            self.wordlis = ["pickaxe", "qualify", "quality", "showbox", "advance", "cabinet", "careful", "ceiling", "advised", "bedroom", "academy", "accused", "actress", "boulder", "breathe", "chemist", "kickoff", "stomach", "summary", "surgery", "writing", "welfare", "voltage", "tragedy", "tractor", "stature", "spatial", "seismic", "radical", "protein", "physics", "pivotal", "perform", "orchard", "outlook", "between", "against", "another",  "special", "support", "foreign", "society", "present", "chapter", "purpose", "current", "account", "nothing", "private", "medical", "college", "natural", "english", "century", "council", "hundred", "disease", "outside", "payment", "western", "justice", "request", "morning", "machine", "earlier", "ability", "meaning", "circuit", "complex", "supreme", "neither", "revenue", "economy", "culture", "nuclear", "correct", "traffic", "feeling", "husband", "highway", "speaker", "alcohol", "feature", "suppose", "therapy", "utility", "display", "academy", "organic", "drawing", "passage", "monthly", "chinese", "express", "concern", "village", "channel", "quarter", "density", "reality"]
        elif self.length == 8 : 
            self.wordlis = ["national", "evidence", "economic", "research", "interest", "question", "analysis", "together", "addition", "practice", "division", "standard", "pressure", "personal", "security", "approach", "solution", "hospital", "probably", "chairman",  "activity", "industry", "building", "exchange", "behavior", "actually", "computer", "transfer", "southern", "commerce", "seperate", "relative", "presence", "location", "recently", "positive", "negative", "creative", "whatever", "northern", "regional", "maintain", "petition", "reaction", "reaction", "cultural", "medicine", "adequate", "religion", "numerous", "estimate", "employer", "employee", "quantity", "argument", "delivery", "daughter", "mountain", "approval", "document", "republic", "moreover", "external", "straight", "suitable", "opposite", "external", "mortgage", "everyone", "contrast", "variable", "sentence", "accident", "exposure", "emphasis", "criteria", "strategy", "describe", "attitude", "violence", "accurate", "category", "occasion", "branches", "magnetic", "sequence", "customer", "terminal", "duration", "disposal", "moderate", "audience", "frequent", "adoption", "offering", "aluminium", "peculiar", "internet", "colonial", "validity", "township", "drainage", "revision", "specimen", "interval", "historic", "survival", "cylinder", "lightning", "preserve", "producer", "director", "particle", "portland", "overcome", "civilian", "discover", "gasoline", "anterior", "eighteen", "platform", "dominant", "favorite", "darkness", "rational", "imperial", "bacteria", "anywhere", "chloride", "handbook", "maturity", "disaster", "sympathy", "prospect", "shipment", "prisoner", "infantry", "inherent", "somebody", "weakness", "fracture", "potrait", "guardian", "unlawful", "carriage", "junction", "locality"]
        
    def save(self, comp_time) :
        with open("scores.txt", "a") as f : 
            f.write(f"{self.name.title()} completed {self.length}-word hangman game in {comp_time} seconds! {self.life} life(s) were remaining.\n\n") 
        
    def play(self) : 
        now = time.time()

        xyz = ", "
        blankstr = ""
        char = []
        guesses = []
        blanklis = []
        word = random.choice(self.wordlis)
        for wor in word : 
            char.append(wor)
    
        blank1 = "_ "*len(word)

        for blank in blank1 : 
            blanklis.append(blank)
        
        while True : 
            if self.life == 0 : 
                print("Game over! Better luck next time.")
                time.sleep(0.5)
                print(f"The word was '{word}'")
                time.sleep(1)
                break
            
            letgues = xyz.join(guesses)

            if len(letgues) == 0 : 
                letgues = "N/A"
                
            blankhint = blankstr.join(blanklis)
            print(blankhint)
            print(f"Letters guessed : {letgues}")
            guess = input("Enter your guessed alphabet : ")
            guess = guess.lower()
            time.sleep(0.5)
            
            if guess in letgues or guess in blanklis : 
                time.sleep(0.5)
                print("You have already guessed this letter!")
                time.sleep(0.5)
                continue
            
            if guess not in char : 
                self.life = self.life - 1
                print("Wrong guess!")
                time.sleep(0.5)
                guesses.append(guess)
                print(f"{self.life} life(s) left!")
                time.sleep(1)
                
            elif guess in char : 
                print("You guessed it right!")
                tt = [n for n,  h in enumerate(char) if guess == h]
                for z in tt : 
                    blanklis[z*2] = guess
                time.sleep(1)

            if "_" not in blanklis : 
                time.sleep(0.5)
                print(f"You guessed the word! It's '{word}', congrats :D")
                time.sleep(1)
                then = time.time()
                total = int(then - now)
                self.save(total)
                break
    

z1 = 0
while z1 != 5 : 
    time.sleep(1)
    player = input("Enter your name here : ")
    time.sleep(0.5)
    while True : 
        length_wor = input("Enter word length (4, 5, 6, 7, 8) : ")
    
        if int(length_wor) <= 8 : 
            print("Everything's cool. Let's play!")
            time.sleep(2)
            letplay = HangMan(player, int(length_wor))
            letplay.play()
            break
        else : 
            print("Invalid integer brother!")
    break
    
    
                        
                        
                    
            
        

    
        
        