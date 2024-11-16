string = "My name is Jessa"
lis = string.split()
for i in range(len(lis)) :
    lis[i] = lis[i][::-1]

print(" ".join(lis))