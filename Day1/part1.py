mostCalories = 0
currentElfCalories = 0
f = open("input.txt")
for line in f:
    if (line == "\n"):
        if (currentElfCalories > mostCalories):
            mostCalories = currentElfCalories
        currentElfCalories = 0
    else:
        currentElfCalories += int(line)

print(mostCalories)