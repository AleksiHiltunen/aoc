with open("input_data.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
stacks = []

stack_lines = []
instruction_lines = []
instructions = []
reading_stacks = True
for line in lines:
    if reading_stacks:
        stack_lines.append(line)
    else:
        instruction_lines.append(line)
    if len(line) == 0:
        reading_stacks = False

for i in range(9):
    stacks.append([])

stack_lines = stack_lines[:-2]
i = len(stack_lines)
box_length = 4
while i > 0:
    j = 0
    while j < 9:
        part = stack_lines[i-1][j*box_length:j*box_length+box_length]
        if "[" in part:
            stacks[j].append(part[1:2])
        j += 1
    
    i -= 1

for line in instruction_lines:
    if len(line) == 0:
        continue
    line = line.split(" ")
    instruction_item = {}
    instruction_item["how_many"] = line[1]
    instruction_item["from"] = line[3]
    instruction_item["to"] = line[5]
    instructions.append(instruction_item)

for stack in stacks:
    print(stack)

print()
for instruction in instructions:
    item = stacks[int(instruction["from"])-1][-int(instruction["how_many"]):]
    stacks[int(instruction["to"])-1].extend(item)
    stacks[int(instruction["from"])-1] = stacks[int(instruction["from"])-1][:-int(instruction["how_many"])]
    for stack in stacks:
        print(stack)
        
    print()
