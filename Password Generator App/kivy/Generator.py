import random

def generate(length): 
    choices = list("abcdefghijklmnopqrstuvwxyz1234567890-=|';?/>.<,[{_+(*&^%$#@!`~\\)}]")
    string = []
    for _ in range(length):
        string.append(random.choice(choices))
    return "".join(string)

if __name__ == "__main__":
    print(generate(4))