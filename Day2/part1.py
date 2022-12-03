VALUES = {"X":1, "Y":2, "Z":3}
LOSS = 0
DRAW = 3
WIN = 6
total = 0
f = open("./input.txt")

for line in f:
    score = VALUES[line[2]]
    if ((line[0] == "A" and line[2] == "X") or (line[0] == "B" and line[2] == "Y") or (line[0] == "C" and line[2] == "Z")):
        score += DRAW
    elif (line[0] == "A"):
        if (line[2] == "Y"):
            score += WIN
        elif (line[2] == "Z"):
            score += LOSS
    elif (line[0] == "B"):
        if (line[2] == "X"):
            score += LOSS
        elif (line[2] == "Z"):
            score += WIN
    elif (line[0] == "C"):
        if (line[2] == "X"):
            score += WIN
        elif (line[2] == "Y"):
            score += LOSS
    total += score

print(total)
