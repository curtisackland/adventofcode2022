RESULT = {"X":0, "Y":3, "Z":6}
ROCK = 1
PAPER = 2
SCIS = 3
total = 0
f = open("./input.txt")

for line in f:
    score = RESULT[line[2]]

    if (line[2] == "X"): # need to lose
        if (line[0] == "A"):
            score += SCIS 
        elif (line[0] == "B"):
            score += ROCK
        elif (line[0] == "C"):
            score += PAPER
    elif (line[2] == "Y"): # need to draw
        if (line[0] == "A"):
            score += ROCK
        elif (line[0] == "B"):
            score += PAPER
        elif (line[0] == "C"):
            score +=  SCIS
    elif (line[2] == "Z"): # need to win
        if (line[0] == "A"):
            score += PAPER
        elif (line[0] == "B"):
            score += SCIS
        elif (line[0] == "C"):
            score += ROCK

    total += score

print(total)
