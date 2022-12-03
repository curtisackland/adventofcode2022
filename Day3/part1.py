ITEMS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
f = open("input.txt")

for line in f:
    line = line.strip()
    length = len(line)
    found = False
    for x in range(0, int(length/2)):
        for y in range(int(length/2), length):
            if (line[x] == line[y]):
                found = True
                total += ITEMS.index(line[x]) + 1
                break
        if (found):
            break

print(total)

    
