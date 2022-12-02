mostCalories1 = 0
mostCalories2 = 0
mostCalories3 = 0
currentElfCalories = 0
f = open("input.txt")
for line in f:
    if (line == "\n"):
        if (currentElfCalories > mostCalories1):
            mostCalories3 = mostCalories2
            mostCalories2 = mostCalories1 
            mostCalories1 = currentElfCalories
        elif (currentElfCalories > mostCalories2):
            mostCalories3 = mostCalories2
            mostCalories2 = currentElfCalories
        elif (currentElfCalories > mostCalories3):
            mostCalories3 = currentElfCalories
        currentElfCalories = 0
    else:
        currentElfCalories += int(line)

print(mostCalories1 + mostCalories2 + mostCalories3)