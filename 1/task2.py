with open("input_data.txt", "r") as f:
    data = f.read()

calorie_lines = data.split("\n")
elves = [0]
for line in calorie_lines:
    if line == "":
        elves.append(0)
    else:
        elves[-1] += int(line)

elves = elves[:-1]
print(elves)

total_calories = 0
for i in range(0, 3):
    max_calorie_carrier = 0
    for elf in range(0, len(elves)):
        if elves[elf] > elves[max_calorie_carrier]:
            max_calorie_carrier = elf

    total_calories += elves[max_calorie_carrier]
    elves = elves[:max_calorie_carrier] + elves[max_calorie_carrier+1:]

print(total_calories)