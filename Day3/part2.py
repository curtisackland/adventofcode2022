ITEMS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
f = open("input.txt")

while(True):
    elf1 = f.readline().strip()
    if (elf1 == ""): #if reading has reached eof
        break
    elf2 = f.readline().strip()
    elf3 = f.readline().strip()
    found = False
    for x in elf1:
        for y in elf2:
            for z in elf3:
                if (x == y == z):
                    found = True
                    total += ITEMS.index(x) + 1
                    break
            if (found):
                break
        if (found):
            break

print(total)

    
