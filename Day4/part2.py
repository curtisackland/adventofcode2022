f = open("input.txt")
total = 0

for line in f:
    line = line.strip().replace(',', '-')
    sections = line.split('-')
    sum1 = int(sections[0]) - int(sections[2])
    sum2 = int(sections[1]) - int(sections[3])
    if ((int(sections[1]) >= int(sections[2]) and int(sections[0]) <= int(sections[3])) 
    or (int(sections[1]) <= int(sections[2]) and int(sections[0]) >= int(sections[3]))):
        total += 1
    
print(total)