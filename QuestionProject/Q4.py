string = "ababacd"
new_string = []
for i in string :
    if i not in new_string :
        new_string.append(i)
    
print("".join(new_string))
