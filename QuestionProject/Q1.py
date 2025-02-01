arr = [1, 2, 3, 6, 3, 6, 1]
n = 7
container = dict()

for i in range(n) :
    if arr[i] not in container :
        container[arr[i]] = 0
    container[arr[i]] += 1

print([x for x in container.keys() if container[x]>1])
    